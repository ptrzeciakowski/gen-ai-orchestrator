"""
Pakiet providerów danych nieruchomości dla architektury ELT.
"""
from src.providers.commercial import CommercialProvider
from src.providers.direct import DirectProvider
from src.providers.adresowo import AdresowoProvider
from src.providers.gratka import GratkaProvider
from src.providers.morizon import MorizonProvider
from src.providers.nieruchomosci_online import NieruchomosciOnlineProvider
from src.providers.olx import OLXProvider

__all__ = [
    "CommercialProvider",
    "DirectProvider",
    "AdresowoProvider",
    "GratkaProvider",
    "MorizonProvider",
    "NieruchomosciOnlineProvider",
    "OLXProvider"
]
