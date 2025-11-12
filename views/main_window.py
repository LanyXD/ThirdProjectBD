from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QStackedLayout, QMenuBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from utils.window_utils import center_on_screen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sales = None
        self.sales_history = None

        self.inventory = None
        self.stock_history = None
        self.product_management = None

        self.status_bar = None
        self.main_layout = None
        self.setup_ui()

    def setup_ui(self):
        self.setup_window()
        self.setup_central_widget()
        self.setup_menu_bar()
        self.setup_status_bar()

    def setup_window(self):
        self.setWindowIcon(QIcon("rsc/icons/sol.png"))
        self.setWindowTitle("La Super Tienda")
        self.setFixedSize(1024, 700)
        center_on_screen(self)

    def setup_central_widget(self):
        central_widget = QWidget(self)
        self.main_layout = QStackedLayout()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def setup_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # --- Menú Ventas ---
        sales_menu = menu_bar.addMenu("Ventas")
        self.sales = QAction("Nueva venta", self)
        self.sales.setStatusTip("Realizar una nueva venta")
        sales_menu.addAction(self.sales)

        self.sales_history = QAction("Historial de ventas", self)
        self.sales_history.setStatusTip("Consultar ventas realizadas")
        sales_menu.addAction(self.sales_history)

        # --- Menú Inventario ---
        inventory_menu = menu_bar.addMenu("Inventario")
        self.inventory = QAction("Ver inventario", self)
        self.inventory.setStatusTip("Visualizar inventario actual")
        inventory_menu.addAction(self.inventory)

        self.stock_history = QAction("Ver movimientos", self)
        self.stock_history.setStatusTip("Visualizar ingresos y egresos de producto")
        inventory_menu.addAction(self.stock_history)

        self.product_management = QAction("Gestion de productos", self)
        self.product_management.setStatusTip("Agregar o eliminar un producto")
        inventory_menu.addAction(self.product_management)

        # --- Menú Ayuda o Sistema ---
        system_menu = menu_bar.addMenu("Ayuda")
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)
        system_menu.addAction(exit_action)

    def setup_status_bar(self):
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Principal")
        self.setStatusBar(self.status_bar)

    def add_widget(self, widget):
        self.main_layout.addWidget(widget)

    def set_index(self, index: int):
        self.main_layout.setCurrentIndex(index)
