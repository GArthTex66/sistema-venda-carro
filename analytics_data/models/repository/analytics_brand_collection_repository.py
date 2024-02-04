from typing import Dict, List
from .collection_repository import CollectionRepository

class AnalyticsBrandCollectionRepository(CollectionRepository):
    def __init__(self, db_connection) -> None:
        super().__init__(db_connection)

    def select_by_branch(self, brandName) -> List[Dict]:
        return self.select_many({'brand': brandName}, {'_id': 0})
    
    def select_by_count(self, countNum) -> List[Dict]:
        return self.select_many({'count': countNum}, {'_id': 0})
    
    def select_all(self) -> List[Dict]:
        return self.select_many({}, {'_id': 0})
    
    def select_all_ordered_by_count(self) -> List[Dict]:
        return self.select_many({}, {'_id': 0}).sort('count', -1)
    