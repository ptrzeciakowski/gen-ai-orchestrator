import os
import re

class CriteriaConfig:
    def __init__(self, criteria_filepath=None):
        if not criteria_filepath:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            criteria_filepath = os.path.join(base_dir, "kryteria.md")
        
        self.filepath = criteria_filepath
        self.raw_content = ""
        self.city = "Warszawa"
        self.districts = ["Mokotów", "Ursynów", "Wilanów"]
        self.max_metro_dist_m = 1200
        self.property_type = "Mieszkanie"
        self.seller_type = "Dowolny"
        self.market_type = "Dowolny"
        self.min_price = 800000
        self.max_price = 1200000
        self.max_price_per_m2 = None
        self.min_area = None
        self.max_area = None
        self.min_rooms = 3
        self.max_rooms = 3
        self.min_floor = 1
        self.max_floor = 8
        self.exclude_ground_floor = True
        self.exclude_top_floor = False
        self.min_build_year = 2000
        self.elevator = True
        self.balcony = True
        self.parking = False
        self.finish_status = "Dowolny"
        self.legal_status = "Dowolny"

        self.load_from_file()

    def is_any_value(self, val_str):
        if not val_str:
            return True
        val_clean = str(val_str).strip().lower()
        any_keywords = ['dowolny', 'dowolna', 'dowolne', 'brak', 'brak limitu', 'brak ograniczenia', 'dowolnie', 'any', 'all', 'none']
        return val_clean in any_keywords

    def load_from_file(self):
        if not os.path.exists(self.filepath):
            return

        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.raw_content = f.read()

        content = self.raw_content

        # Parsowanie dzielnic
        districts_match = re.search(r'\*\*Dzielnice\*\*:\s*\[(.*?)\]', content)
        if districts_match:
            self.districts = [d.strip() for d in districts_match.group(1).split(',')]

        def parse_int_or_none(pattern, default=None):
            match = re.search(pattern, content)
            if match:
                val_raw = match.group(1).split('#')[0].strip()
                if self.is_any_value(val_raw):
                    return None
                try:
                    return int(re.sub(r'[^\d]', '', val_raw))
                except ValueError:
                    return default
            return default

        def parse_str(pattern, default):
            match = re.search(pattern, content)
            if match:
                val = match.group(1).split('#')[0].strip()
                return val if val else default
            return default

        self.min_price = parse_int_or_none(r'\*\*Cena minimalna \(PLN\)\*\*:\s*([^\n]+)', self.min_price)
        self.max_price = parse_int_or_none(r'\*\*Cena maksymalna \(PLN\)\*\*:\s*([^\n]+)', self.max_price)
        self.max_price_per_m2 = parse_int_or_none(r'\*\*Maksymalna cena za m² \(PLN/m²\)\*\*:\s*([^\n]+)', self.max_price_per_m2)
        self.min_area = parse_int_or_none(r'\*\*Powierzchnia minimalna \(m²\)\*\*:\s*([^\n]+)', self.min_area)
        self.max_area = parse_int_or_none(r'\*\*Powierzchnia maksymalna \(m²\)\*\*:\s*([^\n]+)', self.max_area)
        self.min_rooms = parse_int_or_none(r'\*\*Minimalna liczba pokoi\*\*:\s*([^\n]+)', self.min_rooms)
        self.max_rooms = parse_int_or_none(r'\*\*Maksymalna liczba pokoi\*\*:\s*([^\n]+)', self.max_rooms)
        self.seller_type = parse_str(r'\*\*Typ ogłoszeniodawcy\*\*:\s*([^\n]+)', self.seller_type)
        self.market_type = parse_str(r'\*\*Rynek\*\*:\s*([^\n]+)', self.market_type)
        self.legal_status = parse_str(r'\*\*Stan prawny\*\*:\s*([^\n]+)', self.legal_status)

    def to_dict(self):
        return {
            "city": self.city,
            "districts": self.districts,
            "min_price": self.min_price,
            "max_price": self.max_price,
            "max_price_per_m2": self.max_price_per_m2,
            "min_area": self.min_area,
            "max_area": self.max_area,
            "min_rooms": self.min_rooms,
            "max_rooms": self.max_rooms,
            "seller_type": self.seller_type,
            "market_type": self.market_type,
            "legal_status": self.legal_status
        }
