"""
Silnik generowania raportu w formacie Markdown z rozszerzonymi statystykami kwantylowymi RCN Warszawa:
Wyświetla FAKTYCZNIE ZASTOSOWANE KRYTERIA WYSZUKIWANIA odczytane z pliku kryteria.md dla pełnej audytowalności.
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
        timestamp_str = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        filename = f"{timestamp_str}-oferty.md"
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
        md_lines.append(f"# Raport Ofert Nieruchomości - Warszawa ({timestamp_str})")
        md_lines.append("")
        md_lines.append(f"**Wygenerowano**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md_lines.append(f"**Przeanalizowano unikalnych ofert**: {len(processed_listings)}")
        md_lines.append(f"**Źródło danych transakcyjnych**: Rejestr Cen Nieruchomości m.st. Warszawy (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/)")
        md_lines.append(f"**Okres transakcyjny bazy RCN**: `{self.rcn_client.date_range}`")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        md_lines.append("## ⚙️ Faktycznie Zastosowane Kryteria Wyszukiwania")
        md_lines.append(f"- **Ścieżka pliku kryteriów**: `{self.config.filepath}`")
        md_lines.append(f"- **Miasto**: {self.config.city}")
        md_lines.append(f"- **Wybrane Dzielnice**: {', '.join(self.config.districts)}")
        md_lines.append(f"- **Zakres cenowy (PLN)**: {self.config.min_price:,} zł - {self.config.max_price:,} zł")
        md_lines.append(f"- **Maksymalna cena za m²**: {self.config.max_price_per_m2:,} zł/m²")
        md_lines.append(f"- **Powierzchnia (m²)**: {self.config.min_area} m² - {self.config.max_area} m²")
        md_lines.append(f"- **Liczba pokoi**: {self.config.min_rooms} - {self.config.max_rooms}")
        md_lines.append(f"- **Typ ogłoszeniodawcy**: {self.config.seller_type}")
        md_lines.append(f"- **Stan prawny**: {self.config.legal_status}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        md_lines.append("## 📊 Rozkład Cen Transakcyjnych RCN Warszawa (N, Średnia, P10, P25, P50, P75, P90)")
        md_lines.append(f"Statystyki z zarejestrowanych aktów notarialnych zgromadzonych w bazie RCN m.st. Warszawy za okres **{self.rcn_client.date_range}**.")
        md_lines.append("")

        for district in self.config.districts:
            d_stats = self.rcn_client.get_district_stats(district)
            a_stats = self.rcn_client.get_area_stats(district)
            
            md_lines.append(f"### 📍 Dzielnica: {district} (N = {d_stats['n']:,} transakcji)")
            md_lines.append(f"- **Średnia cena transakcyjna**: **{d_stats['avg']:,} PLN/m²**")
            md_lines.append(f"- **Rozkład kwantylowy**: P10 = **{d_stats['p10']:,} PLN** | P25 = **{d_stats['p25']:,} PLN** | Mediana (P50) = **{d_stats['p50']:,} PLN** | P75 = **{d_stats['p75']:,} PLN** | P90 = **{d_stats['p90']:,} PLN**")
            md_lines.append("")

            if a_stats:
                md_lines.append(f"#### Rozkład Statystyczny w Obszarach / Osiedlach MSI w Dzielnicy {district}:")
                md_lines.append("| Obszar / Osiedle MSI | Transakcje (N) | Średnia (PLN/m²) | 10. Centyl (P10) | 1. Kwartyl (P25) | Mediana (P50) | 3. Kwartyl (P75) | 90. Centyl (P90) | Status |")
                md_lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
                for area_name, area_d in a_stats.items():
                    diff_pct = round(((area_d['avg'] - d_stats['avg']) / d_stats['avg']) * 100, 1)
                    status = "PREMIUM" if diff_pct > 3 else ("POPULARNY" if diff_pct >= -3 else "BUDŻETOWY")
                    md_lines.append(
                        f"| **{area_name}** | N = {area_d['n']:,} | {area_d['avg']:,} PLN | {area_d['p10']:,} PLN | {area_d['p25']:,} PLN | **{area_d['p50']:,} PLN** | {area_d['p75']:,} PLN | {area_d['p90']:,} PLN | {status} |"
                    )
                md_lines.append("")
            else:
                md_lines.append(f"- *Brak wyodrębnionych mikrolokalizacji w bazie RCN dla dzielnicy {district}.*")
                md_lines.append("")

        md_lines.append("---")
        md_lines.append("")
        md_lines.append("## 🏠 Wyselekcjonowane Oferty Rynkowe")
        md_lines.append("")
        md_lines.append("| Tytuł Ogłoszenia | Dzielnica | Pow. (m²) | Pokoje | Cena (PLN) | PLN/m² | Średnia RCN | Mediana (P50) | Odchylenie RCN (%) | Typ | Źródło | Link |")
        md_lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

        for item in processed_listings:
            delta_str = f"+{item['rcn_delta_pct']}%" if item['rcn_delta_pct'] > 0 else f"{item['rcn_delta_pct']}%"
            badge = "🟢 " if item['rcn_delta_pct'] < 5 else "🟡 "
            md_lines.append(
                f"| {item['title']} | {item['district']} | {item['area_m2']} | {item['rooms']} | {item['price_pln']:,} zł | {item['price_per_m2']:,} | {item['rcn_avg_price_m2']:,} | {item['rcn_p50_m2']:,} | {badge}{delta_str} | {item['seller_type']} | {item['source']} | [Zobacz]({item['url']}) |"
            )

        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        md_lines.append("## 💡 Rekomendacje & Analiza Opłacalności AI")
        md_lines.append("")

        if processed_listings:
            top3 = processed_listings[:3]
            md_lines.append("### 🏆 Top 3 Najbardziej Opłacalne Nieruchomości (Wskaźnik Cena / RCN / Bezpośrednio)")
            for i, top in enumerate(top3, 1):
                md_lines.append(f"#### {i}. {top['title']} ({top['district']})")
                md_lines.append(f"- **Cena całkowita**: {top['price_pln']:,} PLN ({top['price_per_m2']:,} PLN/m²)")
                md_lines.append(f"- **Porównanie do RCN**: Średnia RCN = {top['rcn_avg_price_m2']:,} PLN/m², Mediana P50 = {top['rcn_p50_m2']:,} PLN/m², 1. Kwartyl P25 = {top['rcn_p25_m2']:,} PLN/m².")
                md_lines.append(f"- **Ocena rynkowa**: Cena oferty to **{top['rcn_status']}** ({top['rcn_delta_pct']}% vs średnia RCN).")
                md_lines.append(f"- **Ogłoszeniodawca**: {top['seller_type']} (źródło: {top['source']})")
                if top['seller_type'] == "Bezpośrednio":
                    md_lines.append(f"- **Zysk na braku prowizji**: Brak opłaty dla agencji (~2-3% ceny, tj. zaoszczędzone ok. {round(top['price_pln']*0.025):,} PLN).")
                md_lines.append("")

            md_lines.append("### 🤝 Strategia Negocjacyjna z Wykorzystaniem Rozkładu Kwantylowego RCN")
            md_lines.append("1. **Próg 10. Centyla (P10)**: Przedstawia dolne 10% cen transakcyjnych (stan do remontu / rynkowy okazje). Celuj w P10 przy wykończeniu deweloperskim lub do generelnego remontu.")
            md_lines.append("2. **Próg 1. Kwartyla (P25)**: Wyznacza dolny podział rynku transakcyjnego. Ceny zbliżone do P25 są uznawane za bardzo okazyjne rynkowo.")
            md_lines.append("3. **Próg Medianowy (P50)**: Mediana transakcyjna RCN stanowi najstabilniejszy punkt odniesienia negocjacyjnego.")
            md_lines.append("4. **Próg 3. Kwartyla (P75) i 90. Centyla (P90)**: Wysokie ceny transakcyjne charakterystyczne dla apartamentowców premium i wykończenia 'pod klucz' z klimatyzacją i garażem.")
            md_lines.append("")
            md_lines.append("### ⚠️ Ryzyka i Punkty Do Weryfikacji (Checklist)")
            md_lines.append("- [ ] **Stan Prawny**: Zweryfikuj numer Księgi Wieczystej (Dział III - roszczenia i hipoteki w Dziale IV).")
            md_lines.append("- [ ] **Czynsz**: Dopytaj o dokładny wymiar czynszu administracyjnego i zaliczki na fundusz remontowy.")
            md_lines.append("- [ ] **Miejsce Parkingowe**: Sprawdź czy miejsce w garażu podziemnym jest na odrębnej KW, czy jako udział w lokalu garażowym.")
        else:
            md_lines.append("Brak ofert spełniających podane kryteria.")

        content = "\n".join(md_lines)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return filepath
