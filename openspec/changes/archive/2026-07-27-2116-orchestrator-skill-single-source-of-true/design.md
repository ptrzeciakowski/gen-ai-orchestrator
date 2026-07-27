# OpenSpec Design: Orchestrator Skill Single Source of Truth

**Zmiana**: `orchestrator-skill-single-source-of-true`  
**Data**: 27 Lipca 2026  
**Status**: Projekt Techniczny (Design)  
**Dokumenty Referencyjne**: 
- `openspec/changes/orchestrator-skill-single-source-of-true/proposal.md`
- `openspec/changes/orchestrator-skill-single-source-of-true/explore/001-orchestrator-skill-single-source-of-true-01.md`
- `.ai/guidelines/brutally-honest-rules.md`

---

## 1. Architektura i Przepływ Danych (System Architecture)

System opiera się na natywnym mechanizmie ładowania wtyczek i skilli w interfejsie **Google Antigravity (AGY)** oraz strukturze katalogów repozytorium `gen-ai-orchestrator`.

```
[ .ai/skills/ ] (Single Source of Truth)
       │
       ├── opsx-explore/SKILL.md
       ├── opsx-design/SKILL.md
       ├── opsx-tasks/SKILL.md
       ├── opsx-implement/SKILL.md
       └── opsx-archive/SKILL.md
       │
       ├── [ ./openspec-agy-init.sh ] (Kopiuje za pomocą cp -r)
       │          │
       │          ▼
       └── [ ~/.gemini/config/plugins/openspec/skills/ ] (Globalna wtyczka AGY)
```

---

## 2. Kanoniczne Zasady Poszczególnych Komend

### 2.1. `/opsx-explore`
- Wymaga zapisu artefaktów w podfolderze `explore/` (`openspec/changes/<change-name>/explore/`).
- Format nazwy: `NNN-nazwa-zmiany-MM.<ext>` (np. `001-moja-zmiana-01.md`).
- Nakazuje bezwzględne stosowanie `.ai/guidelines/brutally-honest-rules.md`.

### 2.2. `/opsx-design`
- Przetwarza dane wyjściowe z `explore/` i `proposal.md`.
- Generuje/modyfikuje `design.md`, stosując Akumulacyjne Wzbogacanie i prezentując trade-offy z oznaczaniem `[Hipoteza/Domysł]`.

### 2.3. `/opsx-tasks`
- Przekształca projekt z `design.md` na atomowe zadania z checkboxami `- [ ]` w `tasks.md`.

### 2.4. `/opsx-implement`
- Wykonuje kolejne niezakończone zadania z `tasks.md`.
- **Wymusza weryfikację empiryczną** (uruchomienie testów/skryptu) przed oznaczeniem `- [x]`.

### 2.5. `/opsx-archive`
- Wylicza dwutabelowe metryki w `summary.md`.
- Przenosi katalog do `openspec/changes/archive/YYYY-MM-DD-HHMM-<change-name>`.
- Aktualizuje zbiorczy plik `changes-summary.md`.

---

## 3. Analiza Alternatyw Architektonicznych i Trade-offy (Brutally Honest Analysis)

| Wymiar | Opcja 1: Zahardkodowane szablony w Bashu (`openspec-agy-init.sh`) | Opcja 2 (Wdrożona): `SKILL.md` w `.ai/skills` jako Single Source of Truth + `cp -r` |
| :--- | :--- | :--- |
| **Utrzymanie (Maintainability)** | Bardzo trudne – edycja wymaga modyfikowania uciekających znaków w stringach Bash. | Bardzo łatwe – czysty Markdown edytowany wprost w repozytorium. |
| **Zgodność z DRY** | Złamanie zasady DRY (powielanie treści w 3 miejscach). | Pełna zgodność z DRY. |
| **Integracja z AGY** | Dobre, ale generuje ryzyko desynchronizacji wersji. | Natywne i natychmiastowe kopiowanie z repozytorium. |
| **[Hipoteza/Domysł]** | Zachowanie lekkich plików `.json` w `.ai/tools/` zapobiega ewentualnemu wyłamaniu starszych narzędzi CLI, gdyby odwoływały się do nich bezpośrednio. |

---

## 4. Weryfikacja Techniczna

Instalacja oraz poprawność działania zostały potwierdzone poprzez uruchomienie `./openspec-agy-init.sh` i weryfikację fizycznych plików w `~/.gemini/config/plugins/openspec/skills/`.
