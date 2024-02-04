import os
from dotenv import load_dotenv

load_dotenv()
mongo_db_infos = {
    "HOST": os.getenv("MONGO_DB_HOST"),
    "USERNAME": os.getenv("MONGO_DB_USER"),
    "PASSWORD": os.getenv("MONGO_DB_PASSWORD"),
    "DB_NAME": "analytics_data"
}