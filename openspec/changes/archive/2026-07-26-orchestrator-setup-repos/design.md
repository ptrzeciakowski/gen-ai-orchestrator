## Context
Nasza warstwa orkiestracji potrzebuje zdolności do zarządzania i nanoszenia modyfikacji w zewnętrznych, niespokrewnionych ze sobą lokalnych repozytoriach dewelopera. Zmiana konfiguruje to środowisko za pomocą symlinków oraz oddelegowuje prace wersjonujące (VCS) do podmiotu określanego mianem `git-agenta`. 

## Goals / Non-Goals
**Goals:**
- Stworzenie ustandaryzowanego obszaru `.ai/repositories/` dla symlinków z zewnętrznymi projektami (oraz jego kompatybilnych symlinków `/.repositories/`).
- Wymuszenie twardego procesu opartego na "Feature Branches & Pull Requests" zamiast modyfikowania środowisk bezpośrednio.
- Definicja zakresu pracy dla eksperckiego `git-agenta`.

**Non-Goals:**
- Izolacja agentów w wirtualnych środowiskach czy tymczasowych klonach repozytoriów (Opcje A/B odrzucone z powodu wyboru szybszej we wdrożeniu Opcji C).

## Decisions
- **Wybór Lokalnych Symlinków (Opcja C)**: Podjęto decyzję o symlinkowaniu repozytoriów wprost z lokalnego systemu plików twórcy. Rozwiązanie zapewnia największą prostotę działania kosztem bezpieczeństwa na poziomie zderzeń `index.lock`.
- **Delegacja kompetencji do Git Agenta**: Główny agent obsługujący wywołanie zmiany nie będzie samodzielnie bawił się systemem kontroli wersji; ma to zrzucić na wydzielonego Skilla / Agenta wyspecjalizowanego w odczytywaniu drzewa plików Git i wysyłaniu Pull Requestów.
- **Push Policy**: Hard-coded ograniczenie w logice `git-agenta`, które nigdy nie wywołuje `git commit && git push origin main` a zawsze kreuje i przepycha unikalny branch deweloperski.

## Risks / Trade-offs
- [Risk] Użytkownik i autonomiczny agent wchodzą sobie w paradę próbując zaktualizować status pliku/repo symultanicznie -> Mitigation: `git-agent` zostanie zaprojektowany by rozpoznawać zablokowany `.git/index.lock` i zgłaszać awarię użytkownikowi bez destrukcji historii.
- [Risk] Pętle symlinków niszczące zasoby -> Mitigation: Silna walidacja w skryptach systemowych zabraniająca agentowi rekurencyjnego schodzenia poniżej wyznaczonego dla konkretnego repozytorium root directory.
