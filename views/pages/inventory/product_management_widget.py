from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QTableWidget,
    QHeaderView, QLabel, QLineEdit, QPushButton, QFormLayout,
    QAbstractItemView, QTableWidgetItem,
    QComboBox
)


class ProductManagementWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.tbl_products = None
        self.txt_code = None
        self.txt_name = None
        self.txt_price = None
        self.txt_category = None
        self.txt_search = None

        self.btn_save = None
        self.btn_delete = None
        self.btn_clear = None

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)

        layout.addWidget(self.setup_form_section())
        layout.addWidget(self.setup_table_section())
        layout.addLayout(self.setup_footer_buttons())

        self.setLayout(layout)

    def setup_form_section(self):
        box = QGroupBox("Datos del Producto")
        form = QFormLayout()

        self.txt_code = QLineEdit()
        self.txt_name = QLineEdit()
        self.txt_price = QLineEdit()

        # Category
        self.txt_category = QComboBox()
        self.txt_category.addItems([
            "General", "Fritura", "Bebidas", "Tortillas", "Otro"
        ])

        form.addRow(QLabel("Código:"), self.txt_code)
        form.addRow(QLabel("Nombre:"), self.txt_name)
        form.addRow(QLabel("Precio (Q):"), self.txt_price)
        form.addRow(QLabel("Categoría:"), self.txt_category)

        box.setLayout(form)
        return box

    def setup_table_section(self):
        box = QGroupBox("Lista de Productos")
        layout = QVBoxLayout()

        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("Buscar por código o nombre...")
        layout.addWidget(self.txt_search)

        self.tbl_products = QTableWidget()
        self.tbl_products.setColumnCount(4)
        self.tbl_products.setHorizontalHeaderLabels(
            ["Código", "Nombre", "Categoría", "Precio (Q)"]
        )

        header = self.tbl_products.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.tbl_products.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_products.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_products.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        layout.addWidget(self.tbl_products)
        box.setLayout(layout)

        return box

    def setup_footer_buttons(self):
        layout = QHBoxLayout()

        self.btn_save = QPushButton("💾 Guardar / Actualizar")
        self.btn_delete = QPushButton("🗑 Eliminar")
        self.btn_clear = QPushButton("🧹 Limpiar")

        layout.addWidget(self.btn_save)
        layout.addWidget(self.btn_delete)
        layout.addWidget(self.btn_clear)

        return layout

    def get_form_data(self):
        return {
            "code": self.txt_code.text().strip(),
            "name": self.txt_name.text().strip(),
            "price": float(self.txt_price.text()) if self.txt_price.text() else 0,
            "category": self.txt_category.currentText()
        }

    def clear_form(self):
        self.txt_code.clear()
        self.txt_name.clear()
        self.txt_price.clear()
        self.txt_category.setCurrentIndex(0)

    def load_to_form(self, product: dict):
        self.txt_code.setText(product["code"])
        self.txt_name.setText(product["name"])
        self.txt_price.setText(str(product["price"]))
        self.txt_category.setCurrentText(product["category"])

    def fill_table(self, products: list):
        self.tbl_products.setRowCount(len(products))

        for row, p in enumerate(products):
            self.tbl_products.setItem(row, 0, QTableWidgetItem(p["code"]))
            self.tbl_products.setItem(row, 1, QTableWidgetItem(p["name"]))
            self.tbl_products.setItem(row, 2, QTableWidgetItem(p["category"]))
            self.tbl_products.setItem(row, 3, QTableWidgetItem(str(p["price"])))
