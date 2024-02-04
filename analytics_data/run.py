from models.connection_options.connection import DBConnectionHandler

db_handler = DBConnectionHandler()
conn1 = db_handler.get_db_connection()
print(conn1)

db_handler.connect_to_db()
conn2 = db_handler.get_db_connection()
print(conn2)

collection = conn2['analytics_brand']
collection.insert_one({'brand':'Toyota','count':200})

