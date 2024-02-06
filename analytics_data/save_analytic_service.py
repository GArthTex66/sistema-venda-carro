import pandas as pd
import json as json
from models.connection_options.connection import DBConnectionHandler
from models.repository.analytics_brand_collection_repository import AnalyticsBrandCollectionRepository


class SaveAnalyticService:

    def __init__(self) -> None:
        db_handler = DBConnectionHandler()
        db_handler.connect_to_db()
        connection = db_handler.get_db_connection()
        self.__analytics_brand_collection_repository = AnalyticsBrandCollectionRepository(connection)

    def __saveBrandAnalytics(self,data):
        json_data = json.loads(data)
        brand = json_data['brand']
        
        brand_data = self.__analytics_brand_collection_repository.select_by_brand(brand)

        if len(brand_data) == 0:
            self.__analytics_brand_collection_repository.insert_document({'brand': brand, 'count': 1})
        elif len(brand_data) > 1:
            print('Error: More than one brand with the same name')
        else:
            count = brand_data[0]['count'] +1
            brandFilter = {'brand': brand}
            self.__analytics_brand_collection_repository.update_document('count', count, brandFilter)

    def saveDataAnalytics(self,data):
        self.__saveBrandAnalytics(data)
       


   
        