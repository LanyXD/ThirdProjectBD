from pymongo import MongoClient


class Database:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="super_tienda"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name: str):
        return self.db[name]
