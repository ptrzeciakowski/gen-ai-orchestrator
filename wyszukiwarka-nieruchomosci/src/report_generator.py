"""
Silnik generowania raportu w formacie Markdown dla serwisu Wyszukiwarka Nieruchomości Warszawa.
Realizuje pełną strukturę z rozbudowaną próbką surowych transakcji notarialnych RCN Warszawa i tabelą kwantylową dla każdej dzielnicy.
"""
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, config, rcn_client):
        self.config = config
        self.rcn_client = rcn_client
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.history_dir = os.path.join(self.base_dir, "historia")
        os.makedirs(self.history_dir, exist_ok=True)

    def generate_report(self, listings):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_readable = now.strftime("%H:%M:%S")
        timestamp_file_id = now.strftime("%Y-%m-%d-%H%M%S")
        
        filename = f"{timestamp_file_id}-oferty.md"
        filepath = os.path.join(self.history_dir, filename)

        # Wzbogacenie ofert o metryki RCN
        processed_listings = []
        for l in listings:
            metrics = self.rcn_client.calculate_rcn_metrics(l)
            merged = {**l, **metrics}
            processed_listings.append(merged)

        # Sortowanie po odchyleniu RCN (najbardziej okazyjne pierwsze)
        processed_listings.sort(key=lambda x: x["rcn_delta_pct"])

        # Generowanie zawartości Markdown
        md_lines = []
        md_lines.append(f"# Raport Ofert Nieruchomości - Warszawa ({date_str} {time_readable})")
        md_lines.append("")
        md_lines.append(f"- **Wygenerowano**: {date_str} o godzinie `{time_readable}`")
        md_lines.append(f"- **Przeanalizowano unikalnych ofert**: `{len(processed_listings)}`")
        md_lines.append(f"- **Źródło danych transakcyjnych**: Rejestr Cen Nieruchomości m.st. Warszawy (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/)")
        md_lines.append(f"- **Okres transakcyjny bazy RCN**: `{self.rcn_client.date_range}`")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        # 📌 Spis Treści (Table of Contents)
        md_lines.append("## 📌 Spis Treści")
        md_lines.append("- [⚙️ Kryteria Wyszukiwania](#%EF%B8%8F-kryteria-wyszukiwania)")
        md_lines.append("- [🏠 Wyselekcjonowane Oferty Rynkowe](#-wyselekcjonowane-oferty-rynkowe)")
        md_lines.append("- [💡 Rekomendacje & Analiza Opłacalności AI](#-rekomendacje--analiza-op%C5%82acalno%C5%9Bci-ai)")
        md_lines.append("- [📊 Rozkład Cen Transakcyjnych RCN Warszawa](#-rozk%C5%82ad-cen-transakcyjnych-rcn-warszawa-n-%C5%9Brednia-p10-p25-p50-p75-p90-p95-p99)")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        # ⚙️ Kryteria Wyszukiwania
        md_lines.append("## ⚙️ Kryteria Wyszukiwania")
        md_lines.append(f"Poniższe zestawienie stanowi ścisłe odzwierciedlenie pliku parametrów: `{self.config.filepath}`.")
        md_lines.append("")
        md_lines.append("### 📜 Pełny Plik Parametrów Wyszukiwania (`kryteria.md`)")
        md_lines.append("```markdown")
        if self.config.raw_content:
            md_lines.append(self.config.raw_content.strip())
        else:
            md_lines.append("# Kryteria Wyszukiwania Nieruchomości - Warszawa")
            md_lines.append(f"- Miasto: {self.config.city}")
            md_lines.append(f"- Dzielnice: {', '.join(self.config.districts)}")
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        # 🏠 Wyselekcjonowane Oferty Rynkowe
        md_lines.append("## 🏠 Wyselekcjonowane Oferty Rynkowe")
        md_lines.append("")
        md_lines.append("| Tytuł Ogłoszenia | Dzielnica | Pow. (m²) | Pokoje | Cena (PLN) | PLN/m² | Średnia RCN | Mediana (P50) | Odchylenie RCN (%) | Typ | Źródło | Link |")
        md_lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

        for item in processed_listings:
            delta_str = f"+{item['rcn_delta_pct']}%" if item['rcn_delta_pct'] > 0 else f"{item['rcn_delta_pct']}%"
            badge = "🟢 " if item['rcn_delta_pct'] < 5 else "🟡 "
            
            # Czyszczenie znaków podziału | oraz nowej linii \n,\r, które niszczą składnię tabel Markdown
            clean_title = str(item.get('title') or '').replace('|', '/').replace('\n', ' ').replace('\r', ' ').strip()
            clean_district = str(item.get('district') or '').replace('|', '/').replace('\n', ' ').replace('\r', ' ').strip()
            source_val = str(item.get('source', item.get('source_portals_list', 'Otodom'))).replace('|', '/').replace('\n', ' ').strip()
            seller_val = str(item.get('seller_type') or 'Agencja').replace('|', '/').replace('\n', ' ').strip()
            url_val = item.get('url') or '#'

            md_lines.append(
                f"| {clean_title} | {clean_district} | {item['area_m2']} | {item['rooms']} | {item['price_pln']:,} zł | {item['price_per_m2']:,} | {item['rcn_avg_price_m2']:,} | {item['rcn_p50_m2']:,} | {badge}{delta_str} | {seller_val} | {source_val} | [Zobacz]({url_val}) |"
            )

        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        # 💡 Rekomendacje & Analiza Opłacalności AI
        md_lines.append("## 💡 Rekomendacje & Analiza Opłacalności AI")
        md_lines.append("")

        if processed_listings:
            top3 = processed_listings[:3]
            md_lines.append("### 🏆 Top 3 Najbardziej Opłacalne Nieruchomości (Wskaźnik Cena / RCN / Bezpośrednio)")
            for i, top in enumerate(top3, 1):
                clean_top_title = str(top.get('title') or '').replace('|', '/').replace('\n', ' ').replace('\r', ' ').strip()
                clean_top_district = str(top.get('district') or '').replace('|', '/').replace('\n', ' ').strip()
                source_top = str(top.get('source', top.get('source_portals_list', 'Otodom'))).replace('|', '/').strip()
                seller_top = str(top.get('seller_type') or 'Agencja').replace('|', '/').strip()
                md_lines.append(f"#### {i}. {clean_top_title} ({clean_top_district})")
                md_lines.append(f"- **Cena całkowita**: {top['price_pln']:,} PLN ({top['price_per_m2']:,} PLN/m²)")
                md_lines.append(f"- **Porównanie do RCN**: Średnia RCN = {top['rcn_avg_price_m2']:,} PLN/m², Mediana P50 = {top['rcn_p50_m2']:,} PLN/m², 1. Kwartyl P25 = {top['rcn_p25_m2']:,} PLN/m².")
                md_lines.append(f"- **Ocena rynkowa**: Cena oferty to **{top['rcn_status']}** ({top['rcn_delta_pct']}% vs średnia RCN).")
                md_lines.append(f"- **Ogłoszeniodawca**: {seller_top} (źródło: {source_top})")
                if seller_top == "Bezpośrednio":
                    md_lines.append(f"- **Zysk na braku prowizji**: Brak opłaty dla agencji (~2-3% ceny, tj. zaoszczędzone ok. {round(top['price_pln']*0.025):,} PLN).")
                md_lines.append("")

            md_lines.append("### 🤝 Strategia Negocjacyjna z Wykorzystaniem Rozkładu Kwantylowego RCN")
            md_lines.append("1. **Próg 10. Centyla (P10)**: Przedstawia dolne 10% cen transakcyjnych (stan do remontu / okazje). Celuj w P10 przy mieszkaniach do generalnego remontu.")
            md_lines.append("2. **Próg 1. Kwartyla (P25)**: Wyznacza dolne 25% cen transakcyjnych. Ceny równe lub niższe od P25 stanowią bardzo dobrą okazję rynkową.")
            md_lines.append("3. **Próg Medianowy (P50)**: Mediana transakcyjna RCN stanowi najbardziej obiektywny i odporny na skrajności punkt odniesienia negocjacyjnego.")
            md_lines.append("4. **Progi P90, P95 i P99**: Najwyższe ceny transakcyjne (luksusowe apartamenty, wysoki standard wykończenia 'pod klucz', klimatyzacja i podwójny garaż).")
            md_lines.append("")
            md_lines.append("### ⚠️ Ryzyka i Punkty Do Weryfikacji (Checklist)")
            md_lines.append("- [ ] **Stan Prawny**: Zweryfikuj numer Księgi Wieczystej (Dział III - roszczenia i hipoteki w Dziale IV).")
            md_lines.append("- [ ] **Czynsz**: Dopytaj o dokładny wymiar czynszu administracyjnego i zaliczki na fundusz remontowy.")
            md_lines.append("- [ ] **Miejsce Parkingowe**: Sprawdź czy miejsce w garażu podziemnym jest na odrębnej KW, czy jako udział w lokalu garażowym.")
        else:
            md_lines.append("Brak ofert spełniających podane kryteria.")

        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        # 📊 Statystyki Cen Transakcyjnych RCN Warszawa na samym końcu
        md_lines.append("## 📊 Rozkład Cen Transakcyjnych RCN Warszawa (N, Średnia, P10, P25, P50, P75, P90, P95, P99)")
        md_lines.append(f"Statystyki cen z aktów notarialnych zgromadzonych w bazie RCN m.st. Warszawy za okres **{self.rcn_client.date_range}**.")
        md_lines.append("")

        for district in self.config.districts:
            d_stats = self.rcn_client.get_district_stats(district)
            a_stats = self.rcn_client.get_area_stats(district)
            
            md_lines.append(f"### 📍 Dzielnica: {district} (N = {d_stats['n']:,} transakcji)")
            md_lines.append(f"- **Średnia cena transakcyjna**: **{d_stats['avg']:,} PLN/m²**")
            md_lines.append(f"- **Rozkład kwantylowy**: P10 = **{d_stats['p10']:,} PLN** | P25 = **{d_stats['p25']:,} PLN** | Mediana (P50) = **{d_stats['p50']:,} PLN** | P75 = **{d_stats['p75']:,} PLN** | P90 = **{d_stats['p90']:,} PLN** | P95 = **{d_stats['p95']:,} PLN** | P99 = **{d_stats['p99']:,} PLN**")
            md_lines.append("")

            md_lines.append(f"#### Szczegółowy Rozkład Statystyczny w Obszarach / Osiedlach MSI w Dzielnicy {district}:")
            md_lines.append("| Obszar / Osiedle MSI | Transakcje (N) | Średnia | P10 | P25 | Mediana (P50) | P75 | P90 | P95 | P99 | Status |")
            md_lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
            for area_name, area_d in a_stats.items():
                diff_pct = round(((area_d['avg'] - d_stats['avg']) / d_stats['avg']) * 100, 1)
                status = "PREMIUM" if diff_pct > 3 else ("POPULARNY" if diff_pct >= -3 else "BUDŻETOWY")
                md_lines.append(
                    f"| **{area_name}** | N = {area_d['n']:,} | {area_d['avg']:,} | {area_d['p10']:,} | {area_d['p25']:,} | **{area_d['p50']:,}** | {area_d['p75']:,} | {area_d['p90']:,} | {area_d['p95']:,} | {area_d['p99']:,} | {status} |"
                )
            md_lines.append("")

        # 📜 Próbka Zarejestrowanych Transakcji Notarialnych RCN
        sample_txs = self.rcn_client.get_sample_transactions(self.config.districts)
        if sample_txs:
            md_lines.append("### 📜 Próbka Zarejestrowanych Transakcji Notarialnych RCN (Warszawa)")
            md_lines.append("Poniżej przedstawiono autentyczną próbkę wpisów z aktów notarialnych zarejestrowanych w bazie RCN Warszawa dla weryfikacji:")
            md_lines.append("")
            md_lines.append("| Data Aktu | Dzielnica | Lokalizacja / Ulica | Pow. (m²) | Cena Całkowita (PLN) | Cena Transakcyjna (PLN/m²) | Numer Aktu Notarialnego |")
            md_lines.append("| --- | --- | --- | --- | --- | --- | --- |")
            for tx in sample_txs:
                clean_street = str(tx['street']).replace('|', '/').replace('\n', ' ').strip()
                md_lines.append(
                    f"| {tx['date']} | {tx['district']} | **{clean_street}** | {tx['area_m2']} m² | {tx['total_price_pln']:,} zł | **{tx['price_per_m2']:,} PLN/m²** | `{tx['deed_no']}` |"
                )
            md_lines.append("")

        content = "\n".join(md_lines)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return filepath
