from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QComboBox, QTableWidget,
    QLineEdit, QPushButton)


class PurchaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cmb_provider = None
        self.tbl_products = None
        self.txt_total = None
        self.btn_add = None
        self.btn_save = None

        self.setup_ui()

    def setup_ui(self):
        self.setup_window()
        self.setup_central_iu()

    def setup_window(self):
        self.setWindowTitle("Compras")

    def setup_central_iu(self):
        layout = QVBoxLayout()

        provider_layout = QHBoxLayout()
        provider_layout.addWidget(QLabel("Proveedor:"))
        self.cmb_provider = QComboBox()
        provider_layout.addWidget(self.cmb_provider)
        layout.addLayout(provider_layout)

        self.tbl_products = QTableWidget()
        self.tbl_products.setColumnCount(5)
        self.tbl_products.setHorizontalHeaderLabels(["Producto", "Unidad", "Cantidad", "Costo Unitario", "Subtotal"])
        layout.addWidget(self.tbl_products)

        total_layout = QHBoxLayout()
        total_layout.addWidget(QLabel("Total:"))
        self.txt_total = QLineEdit("0.00")
        self.txt_total.setReadOnly(True)
        total_layout.addWidget(self.txt_total)
        layout.addLayout(total_layout)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Agregar Producto")
        self.btn_save = QPushButton("Realizar Compra")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_save)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
