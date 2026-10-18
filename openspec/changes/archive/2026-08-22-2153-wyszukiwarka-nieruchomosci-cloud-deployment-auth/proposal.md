# OpenSpec Proposal: Wdrożenie Chmurowe z Uwierzytelnianiem i Dostępem dla Użytkowników (Cloud Deployment & Authentication)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-cloud-deployment-auth`  
**Data**: 22 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
- [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Aplikacja ma zostać udostępniona w internecie dla wielu użytkowników (np. członków rodziny, partnerów biznesowych czy klientów), co rodzi dwa kluczowe wyzwania:
1. **Bezpieczeństwo i Dostęp**: Aplikacja nie może być w 100% publiczna bez żadnego zabezpieczenia, aby zapobiec niekontrolowanemu scrapowaniu czy modyfikacji kryteriów przez nieupoważnione osoby.
2. **Cykliczne Odświeżanie Danych**: W chmurze potrzebny jest automatyczny harmonogram (np. cron o 7:00 i 19:00), który zasila bazę świeżymi ofertami bez konieczności ręcznego klikania.

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Warstwa Uwierzytelniania (Authentication Layer)**:
   - Lekki mechanizm uwierzytelniania w API i UI (np. ochrona hasłem / token sesyjny JWT lub prosty Google OAuth).
   - Ekran logowania w React Web UI z zapamiętywaniem sesji w `localStorage`/`HttpOnly cookie`.
2. **Wdrożenie w Chmurze (Cloud Deployment)**:
   - Wdrożenie na wybranej platformie (np. Google Cloud Run z montowaniem Cloud Storage FUSE / Cloud SQL lub dedykowana instancja VPS z Nginx Reverse Proxy i certyfikatem Let's Encrypt SSL/HTTPS).
3. **Automatyczny Harmonogram (Scheduled Ingestion)**:
   - Konfiguracja cyklicznego uruchamiania potoku scrapingu (np. Cloud Scheduler wywołujący `POST /api/pipeline/refresh` z kluczem API crona).

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Moduł Uwierzytelniania (`src/auth.py`, `ui/src/components/LoginModal.jsx`)**: Logowanie, weryfikacja tokenu/hasła, middleware zabezpieczający endpointy API.
- [ ] **Konfiguracja Wdrożenia (Terraform / Cloud Run / Nginx Config)**: Skrypty wdrożeniowe i konfiguracja HTTPS.
- [ ] **Harmonogramowanie**: Konfiguracja automatycznego crona do cyklicznego odświeżania bazy.
- [ ] **Testy Bezpieczeństwa**: Weryfikacja blokady nieautoryzowanych zapytań (kod 401 Unauthorized).

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🌍 **Dostęp z dowolnego urządzenia**: Możliwość przeglądania ofert na telefonie, tablecie i komputerze bez uruchamiania lokalnego środowiska.
* 🔒 **Pełne bezpieczeństwo**: Dostęp wyłącznie dla uprawnionych użytkowników.
* ⏰ **Zawsze świeże dane**: Automatyczne pobieranie ofert w tle o stałych porach.
