from bson.objectid import ObjectId
from typing import Dict, List
from datetime import timedelta

class CollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = 'analytics_brand'
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection[self.__collection_name]
        time = datetime.now() - timedelta(hours=3)
        document.created_at = time
        document.updated_at = time
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection[self.__collection_name]
        collection.insert_many(documents)
        return documents
    
    def select_many(self, filter, returnOptions) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            filter, 
            returnOptions
        )
        return list(data)
    
    def patch_registry(self, key, value, id) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        time = datetime.now() - timedelta(hours=3)
        data = collection.update_one(
            { "_id": ObjectId(id) }, #Filtro
            { "$set": { key: value } } # Campo de edição
        )
        print(data.modified_count)