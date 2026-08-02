"""
Provider ogłoszeń bezpośrednich (Warstwa Bronze).
"""
from src.db import DatabaseManager

class DirectProvider:
    def __init__(self, config, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()

    def fetch_listings(self, run_id=None):
        # W Etapie 1 skupiamy się w 100% na pobieraniu i przetwarzaniu w strukturze Bronze/Silver/Gold
        return 0
