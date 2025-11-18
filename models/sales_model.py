from models.database import Database
from bson import ObjectId
from datetime import datetime


class SalesModel:
    def __init__(self):
        self.db = Database()
        self.collection = self.db.get_collection("sales")

    def create_sale(self,
                    user: dict,
                    client: dict,
                    total: float,
                    payment: dict,
                    details: list,
                    date: str = None):

        sale = {
            "user": user,                    # { username: 'admin' }
            "client": client,                # { name, nit, phone, address }
            "date": date or datetime.utcnow().isoformat(),
            "total": total,
            "payment": payment,              # { given, change }
            "details": details               # lista de productos vendidos
        }

        return self.collection.insert_one(sale).inserted_id

    def get_all(self, limit: int = 100):
        return list(self.collection.find().sort("date", -1).limit(limit))

    def get_by_id(self, sale_id: str):
        return self.collection.find_one({"_id": ObjectId(sale_id)})

    def search_by_client(self, text: str):
        filtro = {
            "$or": [
                {"client.name": {"$regex": text, "$options": "i"}},
                {"client.nit": {"$regex": text, "$options": "i"}},
                {"client.phone": {"$regex": text, "$options": "i"}}
            ]
        }
        return list(self.collection.find(filtro).sort("date", -1))

    def search_by_user(self, username: str):
        return list(self.collection.find({"user.username": username}).sort("date", -1))

    def filter_by_date(self, start: datetime, end: datetime):
        return list(
            self.collection.find(
                {
                    "date": {
                        "$gte": start.isoformat(),
                        "$lte": end.isoformat()
                    }
                }
            ).sort("date", -1)
        )

    def update_sale(self, sale_id: str, new_data: dict):
        return self.collection.update_one(
            {"_id": ObjectId(sale_id)},
            {"$set": new_data}
        )

    def delete_sale(self, sale_id: str):
        result = self.collection.delete_one({"_id": ObjectId(sale_id)})
        return result.deleted_count > 0
