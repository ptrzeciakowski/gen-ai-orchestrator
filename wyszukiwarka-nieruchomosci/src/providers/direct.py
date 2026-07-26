"""
Provider ogłoszeń bezpośrednich (Zaślepka na Etap 1: Prace skoncentrowane wyłącznie na weryfikacji i stabilności Otodom.pl).
"""
class DirectProvider:
    def __init__(self, config):
        self.config = config

    def fetch_listings(self):
        # W Etapie 1 skupiamy się w 100% na idealnym działaniu Otodom.pl
        return []
