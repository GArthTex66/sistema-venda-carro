from typing import Dict, List
from .collection_repository import CollectionRepository

class AnalyticsCarPriceRepository(CollectionRepository):
    def __init__(self, db_connection) -> None:
        super().__init__(db_connection)

    def select_by_price(self, price) -> List[Dict]:
        return self.select_many