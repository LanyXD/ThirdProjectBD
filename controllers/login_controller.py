from models.user_model import UserModel
from views.login_window import LoginWindow
from views.main_window import MainWindow


class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginWindow()
        self.main_controller = None

        self.view.login_button.clicked.connect(self.login)

    def login(self):
        username = self.view.user_input.text()
        password = self.view.password_input.text()

        if self.model.validate_user(username, password):
            self.main_controller = MainWindow()
            self.main_controller.show()
            self.view.close()
        else:
            self.view.error_text.setText("Credenciales incorrectos")
