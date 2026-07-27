# Eksploracja Architektoniczna: SKILL.md jako Single Source of Truth dla Wszystkich Skilli OpenSpec

**Kod Zmiany**: `orchestrator-skill-single-source-of-true`  
**Data**: 27 Lipca 2026  
**Status**: W trakcie eksploracji (OpenSpec Explore - Wzbogacona wersja 01)  
**Dokumenty Referencyjne**: 
- `.ai/guidelines/brutally-honest-rules.md`
- `openspec-agy-init.sh`
- `openspec/changes/archive/changes-summary.md`
- Pliki skilli: `.ai/skills/opsx-*/SKILL.md`

---

## 1. Cel i Kontekst Zmiany

Celem zmiany jest ujednolicenie i uproszczenie zarządzania wszystkimi skryptami i skillami pakietu OpenSpec (`opsx-explore`, `opsx-design`, `opsx-tasks`, `opsx-implement`, `opsx-archive`) w interfejsie Google Antigravity (AGY).

Dotychczas instrukcje dla poszczególnych komend były rozproszone pomiędzy 3 miejscami:
1. Pliki narzędziowe w `.ai/tools/opsx-*.json`,
2. Pliki `SKILL.md` w `.ai/skills/` (zawierające jedynie odwołania do plików `.json`),
3. Skrypt `openspec-agy-init.sh` (posiadający zahardkodowane szablony tekstowe w Bashu).

**Nowa Kanoniczna Architektura (Single Source of Truth)**:
Ustanawiamy pliki **`SKILL.md`** w katalogu repozytorium `.ai/skills/` (zlinkowanym z `.agents/skills/`) jako **Jedyne Źródło Prawdy** dla całego cyklu życiowego OpenSpec:
- **`opsx-explore`**: Kanoniczna instrukcja wprowadzająca obowiązek zapisu analiz w podfolderze `explore/` pod nazwą w konwencji `NNN-nazwa-zmiany-MM.<ext>` (gdzie NNN to numer eksploracji, MM to wersja, plik główny `.md` + opcjonalne skrypty `.sql`, `.json`, `.py`), wraz z nakazem stosowania Zasad Brutalnej Szczerości.
- **`opsx-design`**: Samodzielna instrukcja architektoniczna określająca zasady tworzenia `design.md` na podstawie materiałów w `explore/`, punktowania słabości, prezentowania alternatywnych wariantów (trade-offs) i Akumulacyjnego Wzbogacania.
- **`opsx-tasks`**: Samodzielna instrukcja dekompozycji wdrożeniowej na atomowe, testowalne zadania z checkboxami `- [ ]` w `tasks.md`, zawierające dokładne ścieżki do plików oraz kryteria akceptacji.
- **`opsx-implement`**: Samodzielna instrukcja wykonania wdrożenia kolejnego nieodznaczonego zadania z `tasks.md`, z **bezwzględnym nakazem empirycznej weryfikacji** (uruchomienia testów/komend) przed zgłoszeniem sukcesu i oznaczaniem `- [x]`.
- **`opsx-archive`**: Samodzielna instrukcja archiwizacji z wygenerowaniem dwutabelowego `summary.md` (wycena estymacji vs metryki sesji AI), przeniesieniem do folderu `YYYY-MM-DD-HHMM-<change-name>` oraz aktualizacją centralnego rejestru `changes-summary.md`.

Skrypt **`openspec-agy-init.sh`** został zrefaktoryzowany tak, aby dynamicznie kopiował pliki z `.ai/skills/*` bezpośrednio do globalnego katalogu wtyczek AGY (`~/.gemini/config/plugins/openspec/skills/`), bez powielania stringów tekstowych w Bashu.

Równolegle uporządkowano i zmieniono nazwy katalogów archiwalnych w `openspec/changes/archive/`:
- `2026-07-26-1914-explore-orchestrator-setup` ➔ `2026-07-26-1914-orchestrator-initial-setup`
- `2026-07-26-2052-orch-constructive-criticizm` ➔ `2026-07-26-2052-orchestrator-constructive-criticizm`
- Aktualizacja rejestru zbiorczego w `openspec/changes/archive/changes-summary.md`.

---

## 2. Nazywanie Niepewności i Ograniczeń (Brutally Honest Analysis)

- **Zalety natywne AGY**: System Google Antigravity czyta natywnie pliki `SKILL.md`. Umieszczenie w nich pełnej wiedzy eliminuje niepotrzebny krok odczytu zewnętrznych schematów JSON.
- **[Hipoteza/Domysł]**: Pliki w `.ai/tools/*.json` zostają zachowane jako bardzo lekkie wskaźniki (nakładki) informujące agenta o odesłaniu do odpowiedniego pliku `SKILL.md`, co zapewnia wsteczną kompatybilność z dowolnymi skryptami CLI bazującymi na `.ai/tools/`.

---

## 3. Szczegółowe Mapowanie Zakresu Refaktoryzacji dla Skilli OpenSpec

| Komenda / Skill | Plik Źródła Prawdy (`SKILL.md`) | Kluczowe Nowe Zasady i Konwencje Zdefiniowane w SKILL.md |
| :--- | :--- | :--- |
| **`/opsx-explore`** | `.ai/skills/opsx-explore/SKILL.md` | Zapis analiz w podfolderze `explore/`, nazwy `NNN-nazwa-zmiany-MM.<ext>`, nakaz ładowania `.ai/guidelines/brutally-honest-rules.md`, etykietowanie domysłów jako `[Hipoteza/Domysł]`. |
| **`/opsx-design`** | `.ai/skills/opsx-design/SKILL.md` | Przetwarzanie materiałów z `explore/`, tworzenie `design.md`, punktowanie słabości, prezentowanie 2-3 wariantów architektonicznych z trade-offami, Akumulacyjne Wzbogacanie. |
| **`/opsx-tasks`** | `.ai/skills/opsx-tasks/SKILL.md` | Dekompozycja architektury z `design.md` na atomowe zadania w `tasks.md` z checkboxami `- [ ]`, precyzyjne ścieżki plików i kryteria akceptacji. |
| **`/opsx-implement`** | `.ai/skills/opsx-implement/SKILL.md` | Realizacja pierwszego wolnego zadania z `tasks.md`, **obowiązkowa weryfikacja empiryczna** (uruchomienie testu/komendy) przed oznaczeniem `- [x]`. |
| **`/opsx-archive`** | `.ai/skills/opsx-archive/SKILL.md` | Tworzenie dwutabelowego `summary.md` (estymacja vs tokeny/wall-clock), zmiana nazwy na `YYYY-MM-DD-HHMM-<change-name>`, aktualizacja centralnego rejestru `changes-summary.md`. |

---

## 4. Przeprowadzona Weryfikacja

1. Wszystkie 5 plików `SKILL.md` w `.ai/skills/` zostały w pełni zaktualizowane i sprawdzone.
2. Skrypt `openspec-agy-init.sh` został zrefaktoryzowany do kopiowania plików via `cp -r`.
3. Skrypt został wykonany pomyślnie, synchronizując nową strukturę z wtyczką globalną `~/.gemini/config/plugins/openspec/skills/`.
