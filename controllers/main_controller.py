from PyQt6.QtWidgets import QLabel
from views.main_window import MainWindow
# views
from views.pages.home_widget import HomeWidget
from views.pages.sales_widget import SalesWidget
from views.pages.inventory_widget import InventoryWidget
from views.pages.purchase_widget import PurchaseWidget
from views.pages.sales_history_widget import SalesHistoryWidget
# controllers
from controllers.sales_controller import SalesController


class MainController:
    def __init__(self):
        self.view = MainWindow()

        self.home_widget = HomeWidget()
        self.sales_widget = SalesWidget()
        self.inventory_widget = InventoryWidget()
        self.purchase_widget = PurchaseWidget()
        self.sales_history_widget = SalesHistoryWidget()

        self.sales_controller = SalesController(self.sales_widget)

        self.view.add_widget(self.home_widget)
        self.view.add_widget(self.sales_widget)
        self.view.add_widget(self.inventory_widget)
        self.view.add_widget(self.purchase_widget)
        self.view.add_widget(self.sales_history_widget)

        self.view.sales.triggered.connect(lambda: self.page_sales())
        self.view.inventory.triggered.connect(lambda: self.page_inventory())
        self.view.purchase.triggered.connect(lambda: self.page_purchase())
        self.view.sales_history.triggered.connect(lambda: self.page_sales_history())

        self.sales_widget.btn_cancel.clicked.connect(self.page_principal)

    def page_principal(self):
        self.view.set_index(0)

    def page_sales(self):
        self.view.set_index(1)

    def page_inventory(self):
        self.view.set_index(2)

    def page_purchase(self):
        self.view.set_index(3)

    def page_sales_history(self):
        self.view.set_index(4)
