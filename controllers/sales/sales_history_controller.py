from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from models.sales_model import SalesModel


class SalesHistoryController:
    def __init__(self, view):
        self.view = view
        self.model = SalesModel()

        self.connect_signals()
        self.load_sales()

    def connect_signals(self):
        self.view.btn_refresh.clicked.connect(self.load_sales)
        self.view.btn_delete.clicked.connect(self.delete_selected_sale)

    def load_sales(self):
        self.view.tbl_sales.setRowCount(0)

        sales = self.model.get_all()
        if not sales:
            return

        for sale in sales:
            id_sale = str(sale.get("_id", ""))
            if id_sale == "users_root":
                continue

            row = self.view.tbl_sales.rowCount()
            self.view.tbl_sales.insertRow(row)
            self.view.tbl_sales.setItem(row, 0, QTableWidgetItem(id_sale))
            self.view.tbl_sales.setItem(row, 1, QTableWidgetItem(sale.get("user", {}).get("username", "")))
            self.view.tbl_sales.setItem(row, 2, QTableWidgetItem(sale.get("client", {}).get("name", "")))
            self.view.tbl_sales.setItem(row, 3, QTableWidgetItem(sale.get("date", "")))
            self.view.tbl_sales.setItem(row, 4, QTableWidgetItem(str(sale.get("total", ""))))
            self.view.tbl_sales.setItem(row, 5, QTableWidgetItem(str(sale.get("payment", {}).get("given", ""))))
            self.view.tbl_sales.setItem(row, 6, QTableWidgetItem(str(sale.get("payment", {}).get("change", ""))))

    def delete_selected_sale(self):
        row = self.view.tbl_sales.currentRow()
        if row == -1:
            QMessageBox.warning(self.view, "Error", "Seleccione una venta para eliminar.")
            return

        sale_id = self.view.tbl_sales.item(row, 0).text()

        confirm = QMessageBox.question(
            self.view,
            "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar esta venta? {row + 1}"
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return

        try:
            deleted = self.model.delete_sale(sale_id)
        except Exception:
            QMessageBox.critical(self.view, "Error", "Ocurrió un error al eliminar la venta.")
            return

        if deleted:
            QMessageBox.information(self.view, "Éxito", "Venta eliminada correctamente.")
            self.load_sales()
        else:
            QMessageBox.critical(self.view, "Error", "No se pudo eliminar la venta.")

            print(deleted)
