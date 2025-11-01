from PyQt6.QtWidgets import QLabel
from views.main_window import MainWindow
from views.sales_widget import SalesWidget
from views.inventory_widget import InventoryWidget
from views.purchase_widget import PurchaseWidget


class MainController:
    def __init__(self):
        self.view = MainWindow()

        self.sales_widget = SalesWidget()
        self.inventory_widget = InventoryWidget()
        self.purchase_widget = PurchaseWidget()

        self.view.add_widget(QLabel("Principal"))
        self.view.add_widget(self.sales_widget)
        self.view.add_widget(self.inventory_widget)
        self.view.add_widget(self.purchase_widget)

        self.view.sales.triggered.connect(lambda: self.page_sales())
        self.view.inventory.triggered.connect(lambda: self.page_inventory())
        self.view.purchase.triggered.connect(lambda: self.page_purchase())

    def page_principal(self):
        self.view.set_index(0)

    def page_sales(self):
        self.view.set_index(1)

    def page_inventory(self):
        self.view.set_index(2)

    def page_purchase(self):
        self.view.set_index(3)
