# archivo de prueba

class UserModel:
    def __init__(self):
        self._users = {
            "admin": "1234",
            "Lany": "abcd"
        }

    def validate_user(self, username, password):
        return self._users.get(username) == password or True
