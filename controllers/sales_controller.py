from models.mock_data_model import MockDataModel
from PyQt6.QtWidgets import QTableWidgetItem


class SalesController:
    def __init__(self, view):
        self.view = view
        self.model = MockDataModel()
        self.connect_signals()
        self.load_initial_data()

    def load_initial_data(self):
        self.load_clients()
        self.load_products()

    def load_clients(self):
        self.view.cmb_client.clear()
        for client in self.model.clients:
            self.view.cmb_client.addItem(client["nombre"], client)

        self.view.cmb_client.currentIndexChanged.connect(self.update_client_info)

    def load_products(self):
        self.view.tbl_products.setRowCount(0)
        for p in self.model.products:
            row = self.view.tbl_products.rowCount()
            self.view.tbl_products.insertRow(row)
            self.view.tbl_products.setItem(row, 0, QTableWidgetItem(p["nombre"]))
            self.view.tbl_products.setItem(row, 1, QTableWidgetItem(p["unidad"]))
            self.view.tbl_products.setItem(row, 2, QTableWidgetItem("1"))
            self.view.tbl_products.setItem(row, 3, QTableWidgetItem(f"{p['precio']:.2f}"))
            subtotal = p["precio"] * 1
            self.view.tbl_products.setItem(row, 4, QTableWidgetItem(f"{subtotal:.2f}"))

    def update_client_info(self):
        client = self.view.cmb_client.currentData()
        if client:
            self.view.txt_nit.setText(client.get("nit", ""))
            self.view.txt_phone.setText(client.get("telefono", ""))
            self.view.txt_address.setText(client.get("direccion", ""))

    def connect_signals(self):
        self.view.btn_save.clicked.connect(self.save_sale)
        self.view.btn_cancel.clicked.connect(self.cancel_sale)
        self.view.btn_add.clicked.connect(self.add_product)
        self.view.btn_delete.clicked.connect(self.delete_product)
        self.view.btn_clear.clicked.connect(self.clear_products)

    def save_sale(self):
        print("Venta registrada.")

    def cancel_sale(self):
        print("Venta cancelada.")

    def add_product(self):
        print("Agregar producto.")

    def delete_product(self):
        print("Eliminar producto seleccionado.")

    def clear_products(self):
        self.view.tbl_products.setRowCount(0)
        print("Lista de productos limpiada.")
