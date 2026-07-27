---
name: opsx-design
description: Przygotuj dokument designu OpenSpec (design.md) na bazie eksploracji. Aktywuj ten skill, gdy użytkownik wpisze opsx-design, /opsx-design lub poprosi o wygenerowanie architektury technicznej.
---
# Instrukcja Skilla: /opsx-design

Twoim zadaniem jest przygotowanie lub rozbudowa dokumentu projektu technicznego i architektury **`design.md`** w katalogu aktywnej zmiany OpenSpec (`openspec/changes/<change-name>/design.md`).

## 🛠️ Zasady Wykonania Designu Architektonicznego

1. **Źródła Wejściowe (Context Load)**:
   - Wczytaj i przeanalizuj wszystkie wypracowane materiały eksploracyjne znajdujące się w podfolderze `explore/` (`openspec/changes/<change-name>/explore/NNN-nazwa-zmiany-MM.<ext>`).
   - Jeśli istnieje plik `proposal.md`, uwzględnij jego wstępne założenia biznesowe.
   - Załaduj i bezwzględnie stosuj wytyczne z pliku `.ai/guidelines/brutally-honest-rules.md`.

2. **Zasady Uczciwości i Analizy Architektonicznej**:
   - **Wytykaj słabości i ryzyka**: Punktuj niebezpieczeństwa architektoniczne, wąskie gardła i wyzwania wydajnościowe.
   - **Przedstawiaj alternatywne opcje**: Zawsze opisuj 2-3 warianty realizacji z ich wrotymi trade-offami (zaletami i wadami).
   - **Nazywaj niepewność wprost**: Używaj sformułowań *"Na podstawie dostępnych informacji..."*, *"Wymaga empirycznej weryfikacji..."*.
   - **Oznaczaj domysły**: Wszelkie niepewne przypuszczenia oznaczaj jako **`[Hipoteza/Domysł]`**.
   - **Brak fikcyjnych metryk**: Nie wymyślaj sztucznych wykresów, benchmarków ani adresów URL.

3. **Struktura Pliku `design.md`**:
   - Cel i Zakres Architektury (Context & Goals)
   - Przegląd Komponentów i Przepływu Danych (System Architecture & Flow)
   - Kontrakty API i Schematy Danych (Schemas, Models, DB Tables)
   - Wybory Architektoniczne i Trade-offy (Architectural Trade-offs)
   - Obsługa Sytuacji Awaryjnych i Krawędziowych (Edge Cases & Error Handling)

4. **Akumulacyjne Wzbogacanie (Non-Destructive Enrichment)**:
   - Modyfikuj plik `design.md` nie usuwając wcześniej wypracowanych, wartościowych ustaleń technicznych. Dopisuj uściślenia i nowe podsekcje akumulacyjnie.
