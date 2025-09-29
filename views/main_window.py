from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QStackedLayout, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sales = None
        self.inventory = None
        self.purchase = None
        self.status_bar = None
        self.main_layout = None
        self.setup_ui()

    def setup_ui(self):
        self.setup_window()
        self.setup_central_widget()
        self.setup_toolbar()
        self.setup_status_bar()

    def setup_window(self):
        self.setWindowTitle("Ventana Principal")
        self.setFixedSize(1024, 700)
        self.center_on_screen()

    def setup_central_widget(self):
        central_widget = QWidget(self)
        self.main_layout = QStackedLayout()

        # Page 0
        self.main_layout.setCurrentIndex(0)

        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def setup_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.sales = QAction(self)
        self.sales.setText("Ventas")
        self.sales.setStatusTip("Realizar venta")
        self.inventory = QAction(self)
        self.inventory.setText("Inventario")
        self.inventory.setStatusTip("Vizualizar inventario")
        self.purchase = QAction(self)
        self.purchase.setText("Compras")
        self.purchase.setStatusTip("Realizar compra")

        toolbar.addAction(self.sales)
        toolbar.addAction(self.inventory)
        toolbar.addAction(self.purchase)
        toolbar.setMovable(False)

    def setup_status_bar(self):
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Principal")
        self.setStatusBar(self.status_bar)

    def center_on_screen(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def add_widget(self, widget):
        self.main_layout.addWidget(widget)

    def set_index(self, index: int):
        self.main_layout.setCurrentIndex(index)
