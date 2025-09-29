from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout,
    QScrollArea, QMenu, QToolBar, QLabel, QPushButton
)
from PyQt6.QtGui import QAction, QIcon


def _wrap_layout(layout: QVBoxLayout | QHBoxLayout | QGridLayout) -> QWidget:
    widget = QWidget()
    widget.setLayout(layout)
    return widget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        #  build the base structer of the app
        self.setup_window()
        self.setup_central_widget()
        self.setup_menubar()
        self.setup_toolbar()
        self.setup_status_bar()
        # self.setup_connections()

    def setup_window(self):
        # basic characteristics of the window
        self.setWindowTitle("Log My Run")
        self.setWindowIcon(QIcon("assets/pngZapato.png"))
        self.setFixedSize(1280, 780)
        self.center_on_screen()


    def setup_menubar(self):
        menubar = self.menuBar()
        self.setMenuBar(menubar)

        options_menu = menubar.addMenu("&Options")
        opt_item_1 = QAction("Option 1", self)
        opt_item_1.triggered.connect(self.on_opt1_clicked)
        options_menu.addAction(opt_item_1)

        opt_item_2 = QAction("Option 2", self)
        opt_item_2.triggered.connect(self.on_opt2_clicked)
        options_menu.addAction(opt_item_2)

        help_menu = menubar.addMenu("&Help")
        h_item_1 = QAction("Help 1", self)
        h_item_1.triggered.connect(self.on_h1_clicked)
        help_menu.addAction(h_item_1)

        h_item_2 = QAction("Help 2", self)
        h_item_2.triggered.connect(self.on_h2_clicked)
        help_menu.addAction(h_item_2)

    def setup_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        plans_act = QAction("Plans", self)
        plans_act.triggered.connect(self.on_plans_clicked)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.on_about_clicked)

        toolbar.addAction(plans_act)
        toolbar.addAction(about_action)

        toolbar.setMovable(False)

    def setup_status_bar(self):
        self.statusBar().showMessage("Pantalla principal")



# Functions toolbar
    def on_about_clicked(self):
        self.statusBar().showMessage("Options")

    def on_plans_clicked(self):
        self.statusBar().showMessage("Plans")

