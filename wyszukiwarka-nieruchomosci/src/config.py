import os
import re

class CriteriaConfig:
    def __init__(self, criteria_filepath=None):
        if not criteria_filepath:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            criteria_filepath = os.path.join(base_dir, "kryteria.md")
        
        self.filepath = criteria_filepath
        self.city = "Warszawa"
        self.districts = ["Mokotów", "Ursynów", "Ochota", "Wola", "Żoliborz", "Śródmieście", "Bemowo"]
        self.max_metro_dist_m = 1200
        self.property_type = "Mieszkanie"
        self.seller_type = "Dowolny"
        self.market_type = "Dowolny"
        self.min_price = 450000
        self.max_price = 950000
        self.max_price_per_m2 = 17500
        self.min_area = 40
        self.max_area = 75
        self.min_rooms = 2
        self.max_rooms = 3
        self.min_floor = 1
        self.max_floor = 8
        self.exclude_ground_floor = True
        self.exclude_top_floor = False
        self.min_build_year = 1995
        self.elevator = True
        self.balcony = True
        self.parking = True
        self.finish_status = "Dowolny"
        self.legal_status = "Pełna własność"

        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.filepath):
            return

        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parsowanie prostych kluczy z markdown
        districts_match = re.search(r'\*\*Dzielnice\*\*:\s*\[(.*?)\]', content)
        if districts_match:
            self.districts = [d.strip() for d in districts_match.group(1).split(',')]

        def parse_int(pattern, default):
            match = re.search(pattern, content)
            if match:
                try:
                    return int(re.sub(r'[^\d]', '', match.group(1)))
                except ValueError:
                    return default
            return default

        def parse_str(pattern, default):
            match = re.search(pattern, content)
            if match:
                val = match.group(1).split('#')[0].strip()
                return val if val else default
            return default

        def parse_bool(pattern, default):
            match = re.search(pattern, content)
            if match:
                val = match.group(1).split('#')[0].strip().lower()
                return val in ['tak', 'true', 'yes', '1']
            return default

        self.min_price = parse_int(r'\*\*Cena minimalna \(PLN\)\*\*:\s*(\d+)', self.min_price)
        self.max_price = parse_int(r'\*\*Cena maksymalna \(PLN\)\*\*:\s*(\d+)', self.max_price)
        self.max_price_per_m2 = parse_int(r'\*\*Maksymalna cena za m² \(PLN/m²\)\*\*:\s*(\d+)', self.max_price_per_m2)
        self.min_area = parse_int(r'\*\*Powierzchnia minimalna \(m²\)\*\*:\s*(\d+)', self.min_area)
        self.max_area = parse_int(r'\*\*Powierzchnia maksymalna \(m²\)\*\*:\s*(\d+)', self.max_area)
        self.min_rooms = parse_int(r'\*\*Minimalna liczba pokoi\*\*:\s*(\d+)', self.min_rooms)
        self.max_rooms = parse_int(r'\*\*Maksymalna liczba pokoi\*\*:\s*(\d+)', self.max_rooms)
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
