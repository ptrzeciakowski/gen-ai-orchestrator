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
        self.max_metro_dist_m = None
        self.property_type = "Mieszkanie"
        self.seller_type = "Dowolny"
        self.market_type = "Dowolny"
        self.min_price = None
        self.max_price = None
        self.max_price_per_m2 = None
        self.min_area = None
        self.max_area = None
        self.min_rooms = None
        self.max_rooms = None
        self.min_floor = None
        self.max_floor = None
        self.exclude_ground_floor = False
        self.exclude_top_floor = False
        self.min_build_year = None
        self.elevator = False
        self.balcony = False
        self.parking = False
        self.finish_status = "Dowolny"
        self.legal_status = "Dowolny"

        self.load_from_file()

    def is_any_value(self, val_str):
        if not val_str:
            return True
        val_clean = str(val_str).strip()
        # Elastyczny regex wyłapujący dowolne odmiany: dowolny, dowolna, dowolnie, brak, brak limitu, n/a, brak preferencji
        return bool(re.search(r'^(dowoln|brak|any|all|none|n/a)', val_clean, re.IGNORECASE))

    def load_from_file(self):
        if not os.path.exists(self.filepath):
            return

        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.raw_content = f.read()

        content = self.raw_content

        # Parsowanie Dzielnic (elastyczne: w nawiasach kwadratowych lub po dwukropku)
        districts_match = re.search(r'(?i)\*\*Dzielnice\*\*:\s*\[?(.*?)\]?$', content, re.MULTILINE)
        if districts_match:
            d_raw = districts_match.group(1).strip()
            if not self.is_any_value(d_raw):
                self.districts = [d.strip() for d in d_raw.split(',') if d.strip()]

        def parse_val(pattern):
            match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
            if match:
                val = match.group(1).split('#')[0].strip()
                return val
            return None

        def parse_number(pattern, is_float=False):
            val_str = parse_val(pattern)
            if not val_str or self.is_any_value(val_str):
                return None
            num_match = re.search(r'(\d+([.,]\d+)?)', val_str)
            if num_match:
                n_str = num_match.group(1).replace(',', '.')
                return float(n_str) if is_float else int(float(n_str))
            return None

        def parse_bool(pattern):
            val_str = parse_val(pattern)
            if not val_str or self.is_any_value(val_str):
                return False
            return val_str.strip().lower() in ['tak', 'true', 'yes', '1', 'wymagane']

        def parse_string(pattern, default="Dowolny"):
            val_str = parse_val(pattern)
            if not val_str or self.is_any_value(val_str):
                return "Dowolny"
            return val_str

        # Parsowanie wszystkich parametrów z kryteria.md
        self.min_price = parse_number(r'(?i)\*\*Cena minimalna \(PLN\)\*\*:\s*(.*)')
        self.max_price = parse_number(r'(?i)\*\*Cena maksymalna \(PLN\)\*\*:\s*(.*)')
        self.max_price_per_m2 = parse_number(r'(?i)\*\*Maksymalna cena za m² \(PLN/m²\)\*\*:\s*(.*)', is_float=True)
        self.min_area = parse_number(r'(?i)\*\*Powierzchnia minimalna \(m²\)\*\*:\s*(.*)', is_float=True)
        self.max_area = parse_number(r'(?i)\*\*Powierzchnia maksymalna \(m²\)\*\*:\s*(.*)', is_float=True)
        self.min_rooms = parse_number(r'(?i)\*\*Minimalna liczba pokoi\*\*:\s*(.*)')
        self.max_rooms = parse_number(r'(?i)\*\*Maksymalna liczba pokoi\*\*:\s*(.*)')
        self.min_floor = parse_number(r'(?i)\*\*Piętro minimalne\*\*:\s*(.*)')
        self.max_floor = parse_number(r'(?i)\*\*Piętro maksymalne\*\*:\s*(.*)')
        self.exclude_ground_floor = parse_bool(r'(?i)\*\*Wyklucz parter\*\*:\s*(.*)')
        self.exclude_top_floor = parse_bool(r'(?i)\*\*Wyklucz ostatnie piętro\*\*:\s*(.*)')
        self.min_build_year = parse_number(r'(?i)\*\*Minimalny rok budowy\*\*:\s*(.*)')
        self.elevator = parse_bool(r'(?i)\*\*Winda\*\*:\s*(.*)')
        self.balcony = parse_bool(r'(?i)\*\*Balkon / Taras / Ogródek\*\*:\s*(.*)')
        self.parking = parse_bool(r'(?i)\*\*Miejsce garażowe / parkingowe\*\*:\s*(.*)')
        self.seller_type = parse_string(r'(?i)\*\*Typ ogłoszeniodawcy\*\*:\s*(.*)')
        self.market_type = parse_string(r'(?i)\*\*Rynek\*\*:\s*(.*)')
        self.finish_status = parse_string(r'(?i)\*\*Stan wykończenia\*\*:\s*(.*)')
        self.legal_status = parse_string(r'(?i)\*\*Stan prawny\*\*:\s*(.*)')

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
            "min_floor": self.min_floor,
            "max_floor": self.max_floor,
            "exclude_ground_floor": self.exclude_ground_floor,
            "exclude_top_floor": self.exclude_top_floor,
            "min_build_year": self.min_build_year,
            "elevator": self.elevator,
            "balcony": self.balcony,
            "parking": self.parking,
            "seller_type": self.seller_type,
            "market_type": self.market_type,
            "legal_status": self.legal_status
        }
