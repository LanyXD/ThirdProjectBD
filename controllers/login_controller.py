from models.user_model import UserModel
from views.login_window import LoginWindow
from controllers.main_controller import MainController
from pymongo.errors import PyMongoError


class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginWindow()
        self.principal = None

        self.view.login_button.clicked.connect(self.login)
        self.view.user_input.textChanged.connect(self.clear_error)
        self.view.password_input.textChanged.connect(self.clear_error)

    def clear_error(self):
        self.view.error_text.setText("")

    def login(self):
        username = self.view.user_input.text().strip()
        password = self.view.password_input.text().strip()

        if not username or not password:
            self.view.error_text.setText("Ingrese usuario y contraseña")
            return

        try:
            if self.model.validate_user(username, password):
                self.principal = MainController(user={'username': username})
                self.principal.view.show()
                self.view.close()
            else:
                self.view.error_text.setText("Credenciales incorrectas")

        except PyMongoError:
            self.view.error_text.setText("Error: no se pudo conectar a la base de datos.")

