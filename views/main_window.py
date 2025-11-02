from PyQt6.QtWidgets import (
    QMainWindow, QWidget,
    QStackedLayout, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from utils.window_utils import center_on_screen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sales = None
        self.inventory = None
        self.purchase = None
        self.sales_history = None
        self.status_bar = None
        self.main_layout = None
        self.setup_ui()

    def setup_ui(self):
        self.setup_window()
        self.setup_central_widget()
        self.setup_toolbar()
        self.setup_status_bar()

    def setup_window(self):
        self.setWindowTitle("La Super Tienda")
        self.setFixedSize(1024, 700)
        center_on_screen(self)

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
        self.sales_history = QAction(self)
        self.sales_history.setText("Historial")
        self.sales_history.setStatusTip("Consultar ventas realizadas")

        toolbar.addAction(self.sales)
        toolbar.addAction(self.inventory)
        toolbar.addAction(self.purchase)
        toolbar.addAction(self.sales_history)
        toolbar.setMovable(False)

    def setup_status_bar(self):
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Principal")
        self.setStatusBar(self.status_bar)

    def add_widget(self, widget):
        self.main_layout.addWidget(widget)

    def set_index(self, index: int):
        self.main_layout.setCurrentIndex(index)
