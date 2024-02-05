from bson.objectid import ObjectId
from typing import Dict, List
from datetime import datetime

class CollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = 'analytics_brand'
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection[self.__collection_name]
        time = datetime.now()
        document["created_at"] = time.strftime("%d/%m/%Y %H:%M:%S")
        document["updated_at"] = time.strftime("%d/%m/%Y %H:%M:%S")
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
    
    def update_by_id(self, id, key, value) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = collection.update_one(
            {"_id": ObjectId(id)}, #Filtro
            { "$set": { key: value , "updated_at":time} } # Campo de edição
        )
        print(data.modified_count)
    
    def update_document(self, key, value, filter) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = collection.update_one(
            filter, #Filtro
            { "$set": { key: value , "updated_at":time} } # Campo de edição
        )
        print(data.modified_count)

    def delete_many_registries(self, filter) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(filter)
        print(data.deleted_count)

    