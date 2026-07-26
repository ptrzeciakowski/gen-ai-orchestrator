"""
Silnik generowania raportu w formacie Markdown z rozszerzonymi rekomendacjami AI.
Plik zapisywany w katalogu historia/ w formacie YYYY-MM-DD-HH24MISS-oferty.md.
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
        md_lines.append(f"**Źródło cen transakcyjnych**: Rejestr Cen Nieruchomości m.st. Warszawy (RCN)")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        md_lines.append("## ⚙️ Domyślne Kryteria Wyszukiwania")
        md_lines.append(f"- **Miasto**: {self.config.city}")
        md_lines.append(f"- **Dzielnice**: {', '.join(self.config.districts)}")
        md_lines.append(f"- **Zakres cenowy**: {self.config.min_price:,} zł - {self.config.max_price:,} zł (max {self.config.max_price_per_m2:,} zł/m²)")
        md_lines.append(f"- **Powierzchnia**: {self.config.min_area} m² - {self.config.max_area} m² ({self.config.min_rooms}-{self.config.max_rooms} pokoi)")
        md_lines.append(f"- **Typ ogłoszeniodawcy**: {self.config.seller_type}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")
        md_lines.append("## 🏠 Wyselekcjonowane Oferty")
        md_lines.append("")
        md_lines.append("| Tytuł Ogłoszenia | Dzielnica | Pow. (m²) | Pokoje | Cena (PLN) | PLN/m² | Średnia RCN (PLN/m²) | Odchylenie RCN (%) | Typ | Źródło | Link |")
        md_lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")

        for item in processed_listings:
            delta_str = f"+{item['rcn_delta_pct']}%" if item['rcn_delta_pct'] > 0 else f"{item['rcn_delta_pct']}%"
            badge = "🟢 " if item['rcn_delta_pct'] < 5 else "🟡 "
            md_lines.append(
                f"| {item['title']} | {item['district']} | {item['area_m2']} | {item['rooms']} | {item['price_pln']:,} zł | {item['price_per_m2']:,} | {item['rcn_avg_price_m2']:,} | {badge}{delta_str} | {item['seller_type']} | {item['source']} | [Zobacz]({item['url']}) |"
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
                md_lines.append(f"- **Stosunek do bazy RCN**: Cena zalicza się jako **{top['rcn_status']}** (odchylenie {top['rcn_delta_pct']}% względem ceny transakcyjnej w {top['district']}).")
                md_lines.append(f"- **Ogłoszeniodawca**: {top['seller_type']} (źródło: {top['source']})")
                if top['seller_type'] == "Bezpośrednio":
                    md_lines.append(f"- **Zysk na braku prowizji**: Brak opłaty dla agencji (~2-3% ceny, tj. zaoszczędzone ok. {round(top['price_pln']*0.025):,} PLN).")
                md_lines.append("")

            md_lines.append("### 🤝 Strategia Negocjacyjna na Podstawie Danych RCN Warszawa")
            md_lines.append("1. **Próg odniesienia (Benchmark RCN)**: Ceny transakcyjne zawarte w aktach notarialnych w wybranych dzielnicach są średnio o 4-8% niższe niż pierwotne ceny ofertowe na portalach.")
            md_lines.append("2. **Sugestia dla ofert z dodatnim odchyleniem RCN**: Składając ofertę zakupu, powołaj się na średnią cenę transakcyjną z RCN Warszawa i celuj w wynegocjowanie obniżki do poziomu średniej transakcyjnej danej dzielnicy.")
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
