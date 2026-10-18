import unittest
from unittest.mock import patch
import planner
import migrate


def item(id, name, parent='actual-root', mime=planner.FOLDER, **extra):
    return dict(id=id, name=name, parents=[parent], mimeType=mime, **extra)


class PlannerTests(unittest.TestCase):
    def plan(self, files, renames=None):
        return planner.make_plan(files, 'actual-root', renames or {})

    def test_scope(self):
        files = [item('a', 'A'), item('b', 'B', 'a'), item('external', 'E', 'other'), item('shared', 'S', driveId='shared'), item('shortcut', 'Link', mime=planner.SHORTCUT), item('not-followed', 'N', 'shortcut')]
        self.assertEqual({f['id'] for f in planner.my_drive(files, 'actual-root')}, {'a', 'b', 'shortcut'})

    def test_mapping_coverage(self):
        self.assertEqual(len(planner.file_mapping()), 52)
        mappings = planner.folder_mapping()
        self.assertEqual(sum(not x['parent_source'] for x in mappings), 28)
        self.assertEqual(sum(bool(x['parent_source']) for x in mappings), 13)
        self.assertFalse(any(x['target'].startswith('99-') for x in planner.file_mapping()))

    def test_root_rename(self):
        plan = self.plan([item('a', 'Old')], {'Old': 'New'})
        self.assertEqual(plan['operations'][0]['kind'], 'rename')
        self.assertEqual(plan['operations'][0]['before']['parents'], ['actual-root'])

    def test_rename_collision(self):
        plan = self.plan([item('a', 'Old'), item('b', 'New')], {'Old': 'New'})
        self.assertEqual(plan['operations'], [])
        self.assertTrue(plan['blocked'])

    def test_native_name_and_rename_reuse(self):
        files = [item('domain', 'Old'), item('diary', 'Dziennik', mime='application/vnd.google-apps.document')]
        plan = self.plan(files, {'Old': '04-📄-Dokumenty-Osobiste'})
        creates = [x for x in plan['operations'] if x['kind'] == 'create_folder']
        self.assertEqual(len(creates), 1)
        self.assertEqual(creates[0]['parent_ref'], 'domain')
        self.assertEqual(plan['operations'][-1]['kind'], 'move')

    def test_duplicate_source(self):
        files = [item('a', 'IMG_2312.jpeg', mime='image/jpeg'), item('b', 'IMG_2312.jpeg', mime='image/jpeg')]
        self.assertEqual(self.plan(files)['operations'], [])

    def test_destination_collision(self):
        files = [item('d', '04-📄-Dokumenty-Osobiste'), item('sub', 'Dziennik', 'd'), item('existing', 'Dziennik', 'sub', 'application/vnd.google-apps.document'), item('source', 'Dziennik', mime='application/vnd.google-apps.document')]
        plan = self.plan(files)
        self.assertEqual(plan['operations'], [])
        self.assertTrue(any('collision' in x['reason'] for x in plan['blocked']))

    def test_shortcut_destination(self):
        files = [item('shortcut', '00-📥-Inbox', mime=planner.SHORTCUT), item('source', 'IMG_2312.jpeg', mime='image/jpeg')]
        self.assertEqual(self.plan(files)['operations'], [])

    def test_sensitive_blocked(self):
        files = [item('s', 'Dowód osobisty - mama.pdf', mime='application/pdf')]
        plan = self.plan(files)
        self.assertEqual(plan['operations'], [])
        self.assertTrue(any('Sensitive' in x['reason'] for x in plan['blocked']))

    def test_nfc(self):
        plan = self.plan([item('a', 'Cafe\u0301')], {'Café': 'New'})
        self.assertEqual(plan['operations'][0]['id'], 'a')

    def test_no_apply_even_with_approval(self):
        with patch('sys.argv', ['migrate.py', 'apply', '--approve', 'APPLY']), patch.object(migrate, 'auth') as auth:
            with self.assertRaises(SystemExit):
                migrate.main()
            auth.assert_not_called()
        with self.assertRaises(RuntimeError):
            migrate.apply(None, {})

    def test_scan_pagination_read_only(self):
        class Request:
            def __init__(self, response):
                self.response = response

            def execute(self):
                return self.response

        class ReadOnlyAPI:
            def files(self):
                return self

            def get(self, **kwargs):
                self_test.assertEqual(kwargs['fileId'], 'root')
                return Request({'id': 'actual-root'})

            def list(self, **kwargs):
                if kwargs.get('pageToken'):
                    return Request({'files': [item('child', 'C', 'domain'), item('outside', 'Outside', 'external')]})
                return Request({'files': [item('domain', 'Domain')], 'nextPageToken': 'second'})

        self_test = self
        self.assertEqual({x['id'] for x in migrate.scan(ReadOnlyAPI())}, {'domain', 'child'})


if __name__ == '__main__':
    unittest.main()
