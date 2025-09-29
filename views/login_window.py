from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.user_input = None
        self.password_input = None
        self.login_button = None
        self.error_text = None

        self.setup_ui(self)

    def setup_ui(self, ui):
        self.setup_window()
        self.setup_central_widget()

    def setup_window(self):
        self.setWindowTitle("Login")
        self.setFixedSize(400, 250)
        self.center_on_screen()

    def setup_central_widget(self):
        main_layout = QVBoxLayout()

        user_label = QLabel("Usuario:")
        main_layout.addWidget(user_label)

        self.user_input = QLineEdit()
        main_layout.addWidget(self.user_input)

        pass_label = QLabel("Contraseña:")
        main_layout.addWidget(pass_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        main_layout.addWidget(self.password_input)

        self.login_button = QPushButton("Ingresar")
        main_layout.addWidget(self.login_button)

        self.error_text = QLabel("")
        self.error_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.error_text)

        self.setLayout(main_layout)

    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
