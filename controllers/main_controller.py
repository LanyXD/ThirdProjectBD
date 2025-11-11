from views.main_window import MainWindow
# views
from views.pages.home_widget import HomeWidget
from views.pages.sales.new_sale_widget import NewSaleWidget
from views.pages.sales.sales_history_widget import SalesHistoryWidget
from views.pages.inventory.inventory_widget import InventoryWidget
from views.pages.inventory.stock_history_widget import StockHistoryWidget
from views.pages.inventory.product_management import ProductManagement

# controllers
from controllers.sales.new_sale_controller import NewSalesController


class MainController:
    def __init__(self):
        self.view = MainWindow()

        self.home_widget = HomeWidget()
        self.new_sale_widget = NewSaleWidget()
        self.sales_history_widget = SalesHistoryWidget()
        self.inventory_widget = InventoryWidget()
        self.stock_history_widget = StockHistoryWidget()
        self.product_management_widget = ProductManagement()

        self.new_sale_controller = NewSalesController(self.new_sale_widget)

        self.view.add_widget(self.home_widget)
        self.view.add_widget(self.new_sale_widget)
        self.view.add_widget(self.sales_history_widget)
        self.view.add_widget(self.inventory_widget)
        self.view.add_widget(self.stock_history_widget)
        self.view.add_widget(self.product_management_widget)

        self.view.sales.triggered.connect(lambda: self.page_new_sale())
        self.view.sales_history.triggered.connect(lambda: self.page_sales_history())
        self.view.inventory.triggered.connect(lambda: self.page_inventory())
        self.view.stock_history.triggered.connect(lambda: self.page_stock_history())
        self.view.product_management.triggered.connect(lambda: self.page_product_management())

        self.new_sale_widget.btn_cancel.clicked.connect(self.page_principal)

    def page_principal(self):
        self.view.set_index(0)

    def page_new_sale(self):
        self.view.set_index(1)

    def page_sales_history(self):
        self.view.set_index(2)

    def page_inventory(self):
        self.view.set_index(3)

    def page_stock_history(self):
        self.view.set_index(4)

    def page_product_management(self):
        self.view.set_index(5)