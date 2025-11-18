from PyQt6.QtWidgets import QMessageBox
from models.inventory_model import InventoryModel


class ProductController:
    def __init__(self, view):
        self.view = view
        self.model = InventoryModel()
        self.selected_product_id = None
        self.connect_signals()
        self.load_products()

    def connect_signals(self):
        self.view.btn_save.clicked.connect(self.save_product)
        self.view.btn_delete.clicked.connect(self.delete_product)
        self.view.btn_clear.clicked.connect(self.clear_form)

        self.view.tbl_products.itemSelectionChanged.connect(self.on_row_selected)

        self.view.txt_search.textChanged.connect(self.search_products)

    def load_products(self):
        products = self.model.get_all(200)
        self.view.fill_table(products)

    def save_product(self):
        data = self.view.get_form_data()

        if not data["code"] or not data["name"]:
            QMessageBox.warning(self.view, "Error", "Código y Nombre son obligatorios")
            return

        try:
            data["price"] = float(data["price"])
        except ValueError:
            QMessageBox.warning(self.view, "Error", "Precio inválido")
            return

        if self.selected_product_id:
            existing = self.model.get_by_id(self.selected_product_id)
            new_data = {
                "code": data["code"],
                "name": data["name"],
                "category": data["category"],
                "price": data["price"],
                "attributes": existing.get("attributes", {}),
            }
            self.model.update_item(self.selected_product_id, new_data)
            QMessageBox.information(self.view, "Actualizado", "Producto actualizado.")
        else:
            new_product = {
                "code": data["code"],
                "name": data["name"],
                "category": data["category"],
                "price": data["price"],
                "attributes": {},
            }
            self.model.create_item(**new_product)
            QMessageBox.information(self.view, "Creado", "Producto registrado.")

        self.clear_form()
        self.load_products()

    def delete_product(self):
        if not self.selected_product_id:
            QMessageBox.warning(self.view, "Eliminar", "Selecciona un producto primero.")
            return

        confirm = QMessageBox.question(
            self.view,
            "Confirmar",
            "¿Deseas eliminar este producto?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            self.model.delete_item(self.selected_product_id)
            self.clear_form()
            self.load_products()

    def clear_form(self):
        self.view.clear_form()
        self.selected_product_id = None
        self.view.tbl_products.clearSelection()

    def on_row_selected(self):
        indexes = self.view.tbl_products.selectedIndexes()
        if not indexes:
            return

        row = indexes[0].row()
        code = self.view.tbl_products.item(row, 0).text()

        product = self.model.get_by_code(code)
        if product:
            self.selected_product_id = str(product["_id"])
            self.view.load_to_form(product)

    def search_products(self):
        text = self.view.txt_search.text().strip()

        if text == "":
            self.load_products()
            return

        products = self.model.search(text)
        self.view.fill_table(products)
