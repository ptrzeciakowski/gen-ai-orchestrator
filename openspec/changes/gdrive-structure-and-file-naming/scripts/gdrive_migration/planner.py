"""Read-only migration planning. Never invokes Drive mutation methods."""
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

FOLDER = 'application/vnd.google-apps.folder'
SHORTCUT = 'application/vnd.google-apps.shortcut'
DOCS = Path(__file__).resolve().parents[2]


def norm(value):
    return unicodedata.normalize('NFC', value)


def my_drive(files, root_id):
    """Only proven descendants of the actual My Drive root; ignore shortcuts."""
    children = defaultdict(list)
    for item in files:
        if not item.get('driveId'):
            for parent in item.get('parents', []):
                children[parent].append(item)
    found = {}
    pending = [root_id]
    visited = set()
    while pending:
        parent = pending.pop()
        if parent in visited:
            continue
        visited.add(parent)
        for item in children[parent]:
            if item['id'] == root_id:
                continue
            found[item['id']] = item
            if item['mimeType'] == FOLDER:
                pending.append(item['id'])
    return list(found.values())


def file_mapping():
    """Exact table entries from 07, with conservative corrections from 09.

    Google native names may omit the desktop pseudo-extension. No fuzzy or
    substring matches: shortened names in the document must be reviewed.
    """
    mappings = []
    for line in (DOCS / 'analysis' / '07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md').read_text().splitlines():
        cells = [cell.strip() for cell in line.split('|')]
        if len(cells) != 9 or not cells[1].isdigit():
            continue
        name = cells[2].strip('`')
        target = cells[5].strip('`').rstrip('/')
        if not target.startswith(('00-', '01-', '02-', '03-', '04-', '05-', '07-', '10-', '12-', '20-', '24-', '99-')):
            continue
        target = target.replace('01-Wazne-Dokumenty', 'Wazne-Dokumenty').replace('02-Natalka', 'Natalka')
        target = target.replace('Samochod-Drugi', 'VW-Golf-Opole')
        target = target.replace('10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia', '10-🏠-Mieszkanie-i-Nieruchomosci/Do-Przypisania/Energia-z-Root')
        target = target.replace('10-🏠-Mieszkanie-i-Nieruchomosci/02-Remonty-i-Wyposazenie', '10-🏠-Mieszkanie-i-Nieruchomosci/Do-Przypisania/Pomysly-z-Root')
        target = target.replace('2026-Biezace', 'Projekty/Do-Przypisania')
        reason = None
        if 'Tozsamosc' in target:
            reason = 'Sensitive document: permissions and encryption require manual review'
        elif 'CAMP DRAWA' in name:
            reason = 'Confirm which child the school document concerns'
        elif target == '99-🗑️-Do-Usuniecia':
            target = '00-📥-Inbox/Do-Przejrzenia/Pliki-z-Root'
        if 'WEiTI' in name:
            target += '/WEiTI'
        mappings.append({'source': name, 'target': target, 'review': reason})
    if len(mappings) != 52:
        raise ValueError('Expected exactly 52 file mappings in document 07')
    return mappings


def folder_mapping():
    """Preserve all decisions from review 09, including conditional mappings."""
    text = (DOCS / 'analysis' / '09-review-katalogow-i-mapowania-gdrive.md').read_text()
    section = text.split('## 5. Skorygowana mapa')[1].split('## 7. Reguły')[0]
    result = []
    for line in section.splitlines():
        cells = [cell.strip() for cell in line.split('|')]
        if len(cells) != 5 or not cells[1].startswith('`'):
            continue
        source = re.search(r'`([^`]+)`', cells[1]).group(1)
        result.append({'source': source, 'proposed_target': cells[2], 'decision': cells[3], 'parent_source': '25📄 Paweł - dokumenty' if '## 6.' in section[:section.index(line)] else None})
    return result


def make_plan(files, root_id, root_renames):
    files = my_drive(files, root_id)
    by_parent = defaultdict(list)
    for item in files:
        for parent in item.get('parents', []):
            by_parent[parent].append(item)
    roots = by_parent[root_id]
    operations, blocked, unchanged = [], [], []
    # Virtual index reflects renames and planned creates; this prevents parallel
    # destination trees and catches collisions before any write takes place.
    index = defaultdict(list)
    for item in files:
        for parent in item.get('parents', []):
            index[(parent, norm(item['name']))].append(item)

    def block(source, reason, ids=None):
        blocked.append({'source': source, 'reason': reason, 'ids': ids or []})

    for source, target in root_renames.items():
        # Running and music keep their original activity/package context below
        # a new domain; not flattened by a root rename.
        if source in ('85🏃 Bieganie', '92🎵 Muzyka'):
            continue
        hits = index[(root_id, norm(source))]
        dest = index[(root_id, norm(target))]
        if not hits:
            continue
        if len(hits) != 1 or hits[0]['mimeType'] != FOLDER or dest:
            block(source, 'Ambiguous source or destination exists; do not merge automatically', [x['id'] for x in hits + dest])
            continue
        item = hits[0]
        operations.append({'kind': 'rename', 'id': item['id'], 'source': item['name'], 'target': target, 'before': {'name': item['name'], 'parents': item.get('parents', [])}})
        index[(root_id, norm(target))] = [dict(item, name=target)]
        index[(root_id, norm(source))] = []

    def ensure(path):
        parent = root_id
        prefix = []
        for name in path.split('/'):
            prefix.append(name)
            key = (parent, norm(name))
            hits = index[key]
            if len(hits) > 1 or (hits and hits[0]['mimeType'] != FOLDER):
                block('/'.join(prefix), 'Destination is ambiguous or not a real folder', [x['id'] for x in hits])
                return None
            if hits:
                parent = hits[0]['id']
            else:
                ref = 'planned:' + '/'.join(prefix)
                operations.append({'kind': 'create_folder', 'path': '/'.join(prefix), 'parent_ref': parent, 'ref': ref})
                index[key] = [{'id': ref, 'name': name, 'mimeType': FOLDER}]
                parent = ref
        return parent

    mapped_ids = {op['id'] for op in operations if 'id' in op}
    for mapping in file_mapping():
        source = mapping['source']
        extension = Path(source).suffix
        native = {'.gdoc': 'application/vnd.google-apps.document', '.gsheet': 'application/vnd.google-apps.spreadsheet', '.gslides': 'application/vnd.google-apps.presentation', '.gprj': 'application/vnd.google-apps.project'}
        hits = [f for f in roots if norm(f['name']) == norm(source) or (extension in native and f['mimeType'] == native[extension] and norm(f['name']) == norm(source[:-len(extension)]))]
        if not hits:
            unchanged.append({'source': source, 'reason': 'No exact root match; absent, renamed or abbreviated in source document'})
            continue
        mapped_ids.update(f['id'] for f in hits)
        if len(hits) != 1 or hits[0]['mimeType'] in (FOLDER, SHORTCUT) or mapping['review']:
            block(source, mapping['review'] or 'Ambiguous source or unsupported type', [x['id'] for x in hits])
            continue
        item = hits[0]
        # Inspect before scheduling creates, including planned moves.
        dest = ensure(mapping['target'])
        if dest is None:
            continue
        collisions = index[(dest, norm(item['name']))]
        if collisions:
            block(source, 'Destination filename collision', [x['id'] for x in collisions])
            continue
        operations.append({'kind': 'move', 'id': item['id'], 'name': item['name'], 'target': mapping['target'], 'parent_ref': dest, 'before': {'name': item['name'], 'parents': item.get('parents', [])}})
        index[(dest, norm(item['name']))].append(item)

    for item in roots:
        if item['id'] not in mapped_ids:
            reason = 'Manual mapping required; preserve subtree and application entry points'
            if item['name'] in root_renames.values():
                unchanged.append({'source': item['name'], 'reason': 'Existing destination domain retained'})
            else:
                block(item['name'], reason, [item['id']])
    proposals = folder_mapping()
    for proposal in proposals:
        parents = [root_id]
        if proposal['parent_source']:
            parents = [f['id'] for f in roots if norm(f['name']) == norm(proposal['parent_source'])]
        hits = [f for parent in parents for f in by_parent[parent] if norm(f['name']) == norm(proposal['source'])]
        proposal['matched_ids'] = [f['id'] for f in hits]
        renamed = {op['id'] for op in operations if op['kind'] == 'rename'}
        proposal['status'] = 'rename_planned_subtree_review_required' if hits and all(f['id'] in renamed for f in hits) else ('review_required' if hits else 'no_exact_match')
        # Every unresolved subtree is explicitly a decision, not a promise of
        # complete automated migration based only on the folder name.
        if proposal['parent_source'] and hits:
            block(proposal['parent_source'] + '/' + proposal['source'], proposal['decision'], proposal['matched_ids'])
    return {'schema_version': 2, 'created_at': datetime.now(timezone.utc).isoformat(), 'root_id': root_id, 'scope': 'Proven descendants of My Drive root; no shortcut traversal', 'inventory_count': len(files), 'root_folder_count': sum(f['mimeType'] == FOLDER for f in roots), 'root_file_count': sum(f['mimeType'] != FOLDER for f in roots), 'operations': operations, 'blocked': blocked, 'unmatched_or_unchanged': unchanged, 'folder_mapping_review': proposals, 'execution_enabled': False}


def summary(plan):
    counts = Counter(op['kind'] for op in plan['operations'])
    lines = ['# Dry-run — poprawiony plan', '', f"Wygenerowano: {plan['created_at']}", '', '**Plan wymaga ręcznego zatwierdzenia. Wykonanie apply jest zablokowane.**', '', f"- My Drive: {plan['inventory_count']} pozycji.", f"- Root: {plan['root_folder_count']} folderów i {plan['root_file_count']} pozostałych pozycji.", f'- Operacje: {dict(counts)}.', f"- Pozycje do decyzji: {len(plan['blocked'])}.", '', '## Operacje', '']
    for op in plan['operations']:
        lines.append(f"- `{op['kind']}`: {op.get('source', op.get('name', op.get('path', '')))} → {op.get('target', op.get('path', ''))}")
    lines += ['', '## Ręczne decyzje / konflikty', '']
    for item in plan['blocked']:
        lines.append(f"- {item['source']}: {item['reason']}")
    lines += ['', '## Brak dopasowania / bez zmian', '']
    for item in plan['unmatched_or_unchanged']:
        lines.append(f"- {item['source']}: {item['reason']}")
    lines += ['', '## Mapa folderów z review 09 (propozycje, nie wykonane operacje)', '']
    for item in plan['folder_mapping_review']:
        lines.append(f"- {item['source']} → {item['proposed_target']} [{item['status']}]. {item['decision']}")
    return '\n'.join(lines) + '\n'
