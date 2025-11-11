import sys
from PyQt6.QtWidgets import QApplication
from controllers.login_controller import LoginController


def main():
    app = QApplication(sys.argv)
    with open("./rsc/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    login_controller = LoginController()
    login_controller.view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
