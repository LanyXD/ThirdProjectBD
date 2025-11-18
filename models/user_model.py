from models.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.collection = self.db.get_collection("sales")
        self.users_doc_id = "users_root"

        if not self.collection.find_one({"_id": self.users_doc_id}):
            self.collection.insert_one({
                "_id": self.users_doc_id,
                "users": []
            })

    def create_user(self, username, password, role="empleado"):
        return self.collection.update_one(
            {"_id": self.users_doc_id},
            {"$push": {"users": {
                "username": username,
                "password": password,
                "role": role
            }}}
        )

    def get_user(self, username):
        doc = self.collection.find_one(
            {"_id": self.users_doc_id, "users.username": username},
            {"users.$": 1}
        )
        if doc and "users" in doc:
            return doc["users"][0]
        return None

    def validate_user(self, username, password):
        user = self.get_user(username)
        if not user:
            return False
        return user["password"] == password
