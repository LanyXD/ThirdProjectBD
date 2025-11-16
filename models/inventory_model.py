from models.database import Database
from bson import ObjectId


class InventoryModel:
    def __init__(self):
        self.db = Database()
        self.collection = self.db.get_collection("products")

    def create_item(self,
                    code: str,
                    category: str,
                    name: str,
                    price: float,
                    attributes: dict):
        new_item = {
            "code": code,
            "category": category,
            "name": name,
            "stock": 0,
            "price": price,
            "state": True,
            "attributes": attributes
        }
        return self.collection.insert_one(new_item).inserted_id

    def get_all(self, limit: int = 100):
        return list(self.collection.find().sort("code", 1).limit(limit))

    def get_by_id(self, item_id: str):
        return self.collection.find_one({"_id": ObjectId(item_id)})

    def get_by_code(self, code: str):
        return self.collection.find_one({"code": code})

    def search(self, text: str):
        filtro = {
            "$or": [
                {"name": {"$regex": text, "$options": "i"}},
                {"category": {"$regex": text, "$options": "i"}},
                {"code": {"$regex": text, "$options": "i"}}
            ]
        }
        return list(self.collection.find(filtro).sort("code", 1))

    def filter(self, category: str = None, min_price: float = None, max_price: float = None):
        query = {}

        if category:
            query["category"] = category

        if min_price is not None or max_price is not None:
            query["price"] = {}
            if min_price is not None:
                query["price"]["$gte"] = min_price
            if max_price is not None:
                query["price"]["$lte"] = max_price

        return list(self.collection.find(query))

    def update_item(self, item_id: str, new_data: dict):
        return self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": new_data}
        )

    def delete_item(self, item_id: str):
        return self.collection.delete_one({"_id": ObjectId(item_id)})

