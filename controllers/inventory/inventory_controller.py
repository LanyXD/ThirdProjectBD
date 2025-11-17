from PyQt6.QtWidgets import QTableWidgetItem, QInputDialog, QMessageBox
from models.inventory_model import InventoryModel


class InventoryController:
    def __init__(self, view):
        self.view = view
        self.model = InventoryModel()

        self.view.txt_search.textChanged.connect(self.refresh_table)

        # btn
        self.view.btn_input.clicked.connect(self.input_stock)
        self.view.btn_output.clicked.connect(self.output_stock)
        self.view.btn_update.clicked.connect(self.refresh_table)

        # chk
        self.view.chk_all.stateChanged.connect(self.refresh_table)
        self.view.chk_stock_low.stateChanged.connect(self.refresh_table)
        self.view.chk_barbecue.stateChanged.connect(self.refresh_table)

        self.refresh_table()

    def refresh_table(self):
        search_text = self.view.txt_search.text().strip()
        show_all = self.view.chk_all.isChecked()
        stock_low = self.view.chk_stock_low.isChecked()
        barbecue = self.view.chk_barbecue.isChecked()

        if show_all:
            self.view.chk_stock_low.setEnabled(False)
            self.view.chk_barbecue.setEnabled(False)
            self.view.chk_stock_low.setChecked(False)
            self.view.chk_barbecue.setChecked(False)
        else:
            self.view.chk_stock_low.setEnabled(True)
            self.view.chk_barbecue.setEnabled(True)
        if search_text:
            items = self.model.search(search_text)
        else:
            items = self.model.get_all()

        # Filtros adicionales
        filtered = []
        for item in items:
            if not show_all:
                # State
                if not item.get("state") or item.get("stock") is None:
                    continue
                # Stock bajo
                if stock_low and item.get("stock", 0) > 20:
                    continue
                # Barbacoa
                if barbecue and not item.get("attributes", {}).get("barbecue", False):
                    continue
            filtered.append(item)

        # Llenar tabla
        tbl = self.view.tbl_inventory
        tbl.setRowCount(len(filtered))
        for row, item in enumerate(filtered):
            tbl.setItem(row, 0, self.make_item(item.get("code")))
            tbl.setItem(row, 1, self.make_item(item.get("name")))
            color = item.get("attributes", {}).get("color", "")
            tbl.setItem(row, 2, self.make_item(color))
            tbl.setItem(row, 3, self.make_item(str(item.get("stock", 0))))
            tbl.setItem(row, 4, self.make_item(str(item.get("price", 0))))

    def make_item(self, text):
        return QTableWidgetItem(text)

    def input_stock(self):
        row = self.view.tbl_inventory.currentRow()
        if row < 0:
            self.show_message("Selecciona un producto primero.")
            return

        code = self.view.tbl_inventory.item(row, 0).text()
        item = self.model.get_by_code(code)
        if not item:
            self.show_message("Producto no encontrado.")
            return

        amount, ok = QInputDialog.getInt(
            self.view, "Ingreso de stock", f"Ingrese cantidad a agregar para {item['name']}:"
        )
        if ok and amount > 0:
            new_stock = item.get("stock", 0) + amount
            self.model.update_item(str(item["_id"]), {"stock": new_stock})
            self.refresh_table()

    def output_stock(self):
        row = self.view.tbl_inventory.currentRow()
        if row < 0:
            self.show_message("Selecciona un producto primero.")
            return

        code = self.view.tbl_inventory.item(row, 0).text()
        item = self.model.get_by_code(code)
        if not item:
            self.show_message("Producto no encontrado.")
            return

        amount, ok = QInputDialog.getInt(
            self.view, "Salida de stock", f"Ingrese cantidad a retirar para {item['name']}:"
        )

        if not ok:
            return

        if amount <= 0:
            self.show_message("La cantidad debe ser mayor a 0.")
            return

        current_stock = item.get("stock", 0)

        if amount > current_stock:
            self.show_message(
                f"No puedes retirar {amount}. Solo hay {current_stock} en existencia."
            )
            return

        nuevo_stock = current_stock - amount
        self.model.update_item(str(item["_id"]), {"stock": nuevo_stock})
        self.refresh_table()

    def show_message(self, text):
        QMessageBox.information(self.view, "Inventario", text)
