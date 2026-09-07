---
name: sandbox-explore
description: Zapisz sesję do folderu sandbox/YYYY-MM-DD-nazwa-explore z historią sesji w plikach NNN-tytul-sesji.md (np. 001-analiza-trendu-narciarskiego.md). Aktywuj ten skill, gdy użytkownik wpisze sandbox-explore, /sandbox-explore, sandbox lub poprosi o zapisanie sesji do sandboxa.
---
# Instrukcja Skilla: /sandbox-explore

Twoim zadaniem jako Agenta jest utrwalenie historii konwersacji i analizy w dedykowanym katalogu `sandbox/` w ramach repozytorium.

## 📁 Zasady Wykonania Eksploracji w Sandboxie

1. **Lokalizacja i Konwencja Folderu**:
   - Wszystkie materiały trafiają do katalogu: `sandbox/YYYY-MM-DD-nazwa-explore/`.
   - `YYYY-MM-DD` – bieżąca data w formacie ISO.
   - `nazwa-explore` – zwięzła, czytelna nazwa tematyczna (np. `narty-austria-ferie-2027-explore`).

2. **Obowiązkowe Pytanie o Nazwę (Zasada Konsultacji)**:
   - **ZAWSZE zaproponuj nazwę explore-a i ZAWSZE zapytaj o to użytkownika** (rekomendowane użycie narzędzia interaktywnego `ask_question`).
   - Przedstaw 2-3 konkretne propozycje nazwy folderu (oznaczając rekomendowaną) i pozwól użytkownikowi wybrać lub podać własną.

3. **Numeracja i Konwencja Plików Sesji**:
   - Wewnątrz folderu `sandbox/YYYY-MM-DD-nazwa-explore/` pliki sesji posiadają 3-cyfrowy prefiks numeryczny oraz 3-5 wyrazowy tytuł w formacie kebab-case: **`NNN-tytul-sesji.md`**.
   - Każdy plik oprócz numeru zawiera 3-5 wyrazowy tytuł opisujący główny temat sesji (np. `001.md` – `001-analiza-trendu-narciarskiego.md`).
   - Każdy plik odpowiada kolejnej sesji / transzy prac w ramach danego explore-a (`001-...md`, `002-...md` itd.).
   - Do wyznaczenia kolejnego pliku można posłużyć się skryptem `./.ai/tools/sandbox-explore.sh <folder_name> <session_id> <title> [slug]`.

4. **Wymagana Zawartość i Dokładna Treść Czatu**:
   - **Nagłówek metadanych**:
     - Data i godzina sesji (np. `YYYY-MM-DD HH:MM:SS TZ`)
     - ID sesji (`Conversation ID`)
     - Tytuł sesji
   - **Dokładna Treść Konwersacji**:
     - W pliku sesji musi znaleźć się **dokładna, pełna treść czatu**, a nie skrótowe streszczenie czy syntetyczny raport.
     - **Zasada Jednego Wątku**: W przypadku jednego wątku tematycznego cała konwersacja musi być ujęta w ramach **jednego rozdziału** (np. `# Rozdział 1: <Tytuł wątku>`).
     - Poszczególne wypowiedzi muszą odzwierciedlać strukturę dialogu za pomocą nagłówków drugiego stopnia:
       - `## Użytkownik` (dokładna treść zapytania / promptu użytkownika)
       - `## Asystent` (dokładna, pełna odpowiedź asystenta wraz z tabelami, linkami i szczegółami)

5. **Zgodność z Zasadami Repozytorium**:
   - Stosuj wytyczne z `.ai/guidelines/brutally-honest-rules.md` (zakaz zmyślania linków i liczb, precyzyjne oznaczanie niepewności).
   - Przestrzegaj zasady nieniszczącego wzbogacania wiedzy (Non-Destructive Spec Enrichment).
