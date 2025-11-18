from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from models.inventory_model import InventoryModel
from models.sales_model import SalesModel


class NewSalesController:
    def __init__(self, view, user: dict):
        self.view = view
        self.user = user
        self.products = None

        self.inventory = InventoryModel()
        self.sales = SalesModel()

        self.connect_signals()
        self.load_initial_data()

    def load_initial_data(self):
        self.load_clients()
        self.load_products()
        self.view.txt_total.setText("0.00")
        self.view.txt_change.setText("0.00")

    def load_clients(self):
        clients = [
            {"name": "Consumidor Final", "nit": "C/F", "phone": "", "address": ""},
            {"name": "Miguel Castillo", "nit": "12345678321", "phone": "78985623", "address": "Calle 18 AV"}
        ]

        self.view.cmb_client.clear()

        for c in clients:
            self.view.cmb_client.addItem(c["name"], c)

        self.view.cmb_client.currentIndexChanged.connect(self.update_client_info)

    def update_client_info(self):
        client = self.view.cmb_client.currentData()
        if client:
            self.view.txt_nit.setText(client.get("nit", ""))
            self.view.txt_phone.setText(client.get("phone", ""))
            self.view.txt_address.setText(client.get("address", ""))

    def load_products(self):
        self.products = self.inventory.get_all()

    def add_product(self):
        if not self.products:
            return

        p = self.products[0]  # cambiar a un selector real.

        row = self.view.tbl_products.rowCount()
        self.view.tbl_products.insertRow(row)

        self.view.tbl_products.setItem(row, 0, QTableWidgetItem(p["name"]))
        self.view.tbl_products.setItem(row, 1, QTableWidgetItem(p["attributes"].get("color", "")))
        self.view.tbl_products.setItem(row, 2, QTableWidgetItem("1"))
        self.view.tbl_products.setItem(row, 3, QTableWidgetItem(f"{p['price']:.2f}"))

        subtotal = p["price"] * 1
        self.view.tbl_products.setItem(row, 4, QTableWidgetItem(f"{subtotal:.2f}"))

        self.update_totals()

    def delete_product(self):
        row = self.view.tbl_products.currentRow()
        if row >= 0:
            self.view.tbl_products.removeRow(row)
            self.update_totals()

    def clear_products(self):
        self.view.tbl_products.setRowCount(0)
        self.update_totals()

    def update_totals(self):
        total = 0
        for row in range(self.view.tbl_products.rowCount()):
            subtotal = float(self.view.tbl_products.item(row, 4).text())
            total += subtotal

        self.view.txt_total.setText(f"{total:.2f}")

        payment_text = self.view.txt_payment.text()
        if payment_text:
            self.update_change()

    def update_change(self):
        try:
            payment = float(self.view.txt_payment.text())
            total = float(self.view.txt_total.text())
            change = payment - total
            self.view.txt_change.setText(f"{change:.2f}")
        except ValueError:
            self.view.txt_change.setText("0.00")

    def save_sale(self):
        # Validación
        if self.view.tbl_products.rowCount() == 0:
            QMessageBox.warning(None, "Error", "Debe agregar al menos un producto.")
            return

        client = self.view.cmb_client.currentData()

        if not client:
            QMessageBox.warning(None, "Error", "Debe seleccionar un cliente.")
            return

        # Construir detalles
        details = []
        for row in range(self.view.tbl_products.rowCount()):
            details.append({
                "product": self.view.tbl_products.item(row, 0).text(),
                "color": self.view.tbl_products.item(row, 1).text(),
                "quantity": int(self.view.tbl_products.item(row, 2).text()),
                "unit_price": float(self.view.tbl_products.item(row, 3).text()),
                "subtotal": float(self.view.tbl_products.item(row, 4).text())
            })

        # Pago
        payment = {
            "given": float(self.view.txt_payment.text()),
            "change": float(self.view.txt_change.text())
        }

        total = float(self.view.txt_total.text())

        # inserción
        sale_id = self.sales.create_sale(
            user=self.user,
            client=client,
            total=total,
            payment=payment,
            details=details
        )

        QMessageBox.information(None, "Venta registrada", f"Venta guardada con ID:\n{sale_id}")

        # Limpiar vista
        self.clear_products()
        self.view.txt_payment.setText("")
        self.view.txt_change.setText("0.00")

    def cancel_sale(self):
        self.clear_products()
        self.view.txt_payment.setText("")
        self.view.txt_change.setText("0.00")
        QMessageBox.information(None, "Cancelado", "Venta cancelada.")

    def connect_signals(self):
        self.view.btn_add.clicked.connect(self.add_product)
        self.view.btn_delete.clicked.connect(self.delete_product)
        self.view.btn_clear.clicked.connect(self.clear_products)

        self.view.txt_payment.textChanged.connect(self.update_change)

        self.view.btn_save.clicked.connect(self.save_sale)
        self.view.btn_cancel.clicked.connect(self.cancel_sale)
