from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QInputDialog, QMessageBox, QTableWidgetItem
from datetime import datetime
from models.sales_model import SalesModel
from models.inventory_model import InventoryModel


class NewSalesController:
    def __init__(self, view, user: dict):
        self.view = view
        self.sales_model = SalesModel()
        self.inventory_model = InventoryModel()
        self.user = user

        self.connect_signals()

    def connect_signals(self):
        self.view.btn_add.clicked.connect(self.add_product)
        self.view.btn_delete.clicked.connect(self.delete_selected)
        self.view.btn_clear.clicked.connect(self.clear_table)
        self.view.btn_save.clicked.connect(self.save_sale)
        self.view.btn_cancel.clicked.connect(self.cancel_sale)

        self.view.txt_payment.textChanged.connect(self.update_change)

    def add_product(self):
        code, ok = QInputDialog.getText(self.view, "Código", "Ingrese el código del producto:")
        if not ok or not code.strip():
            return

        product = self.inventory_model.get_by_code(code.strip())
        if not product:
            self.show("Producto no encontrado.")
            return

        amount, ok = QInputDialog.getInt(self.view, "Cantidad", "Cantidad:", 1, 1, 9999)
        if not ok:
            return

        name = product["name"]
        price = float(product["price"])
        subtotal = price * amount

        row = self.view.tbl_products.rowCount()
        self.view.tbl_products.insertRow(row)
        self.view.tbl_products.setItem(row, 0, self.new_item(name))

        color = product["attributes"].get("color", "-")
        self.view.tbl_products.setItem(row, 1, self.new_item(color))

        self.view.tbl_products.setItem(row, 2, self.new_item(str(amount)))
        self.view.tbl_products.setItem(row, 3, self.new_item(f"{price:.2f}"))
        self.view.tbl_products.setItem(row, 4, self.new_item(f"{subtotal:.2f}"))

        self.update_total()

    def delete_selected(self):
        row = self.view.tbl_products.currentRow()
        if row < 0:
            self.show("Seleccione un producto.")
            return

        self.view.tbl_products.removeRow(row)
        self.update_total()

    def clear_table(self):
        self.view.tbl_products.setRowCount(0)
        self.update_total()

    def update_total(self):
        total = 0
        rows = self.view.tbl_products.rowCount()

        for i in range(rows):
            subtotal = float(self.view.tbl_products.item(i, 4).text())
            total += subtotal

        self.view.txt_total.setText(f"{total:.2f}")
        self.update_change()

    def update_change(self):
        try:
            total = float(self.view.txt_total.text())
            given = float(self.view.txt_payment.text())
            change = given - total
            if change < 0:
                change = 0
            self.view.txt_change.setText(f"{change:.2f}")
        except:
            self.view.txt_change.setText("0.00")

    def save_sale(self):
        client = {
            "name": self.view.txt_client_name.text().strip(),
            "nit": self.view.txt_nit.text().strip(),
            "phone": self.view.txt_phone.text().strip(),
            "address": self.view.txt_address.text().strip()
        }

        if not client["name"]:
            self.show("Ingrese el nombre del cliente.")
            return

        details = []
        rows = self.view.tbl_products.rowCount()

        if rows == 0:
            self.show("Debe agregar al menos un producto.")
            return

        for i in range(rows):
            details.append({
                "product": self.view.tbl_products.item(i, 0).text(),
                "color": self.view.tbl_products.item(i, 1).text(),
                "quantity": int(self.view.tbl_products.item(i, 2).text()),
                "unit_price": float(self.view.tbl_products.item(i, 3).text()),
                "subtotal": float(self.view.tbl_products.item(i, 4).text())
            })

        sale_total = float(self.view.txt_total.text())
        payment_given = float(self.view.txt_payment.text() or 0)
        payment_change = float(self.view.txt_change.text())

        payment = {
            "given": payment_given,
            "change": payment_change
        }

        self.sales_model.create_sale(
            user=self.user,
            client=client,
            total=sale_total,
            payment=payment,
            details=details,
            date=datetime.utcnow().isoformat()
        )

        self.show("Venta realizada con éxito.")
        self.clear_all()

    def cancel_sale(self):
        self.clear_all()

    def clear_all(self):
        self.view.txt_client_name.clear()
        self.view.txt_nit.clear()
        self.view.txt_phone.clear()
        self.view.txt_address.clear()
        self.view.txt_payment.clear()
        self.view.txt_total.setText("0.00")
        self.view.txt_change.setText("0.00")
        self.clear_table()

    def show(self, text):
        QMessageBox.information(self.view, "Info", text)

    def new_item(self, text):
        item = QTableWidgetItem(str(text))
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        return item
