from .collection_repository import CollectionRepository

class AnalyticsCarModelRepository(CollectionRepository):
    def __init__(self, db_connection) -> None:
        super().__init__(db_connection)
