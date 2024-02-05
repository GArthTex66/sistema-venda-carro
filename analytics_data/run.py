from models.connection_options.connection import DBConnectionHandler
from models.repository.analytics_brand_collection_repository import AnalyticsBrandCollectionRepository


db_handler = DBConnectionHandler()
db_handler.connect_to_db()
connection = db_handler.get_db_connection()
analytics_brand_collection_repository = AnalyticsBrandCollectionRepository(connection)

#analytics_brand_collection_repository.insert_document({'brand': 'minha marca', 'count': 1})

brandsCount = analytics_brand_collection_repository.select_by_band('minha marca')

print(brandsCount)

analytics_brand_collection_repository.update_document('count', 2, {'brand': 'minha marca'})

brandsCount = analytics_brand_collection_repository.select_by_band('minha marca')

print(brandsCount)