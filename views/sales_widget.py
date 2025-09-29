from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QComboBox, QTableWidget,
    QLineEdit, QPushButton)


class SalesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cmb_client = None
        self.tbl_products = None
        self.txt_total = None
        self.btn_add = None
        self.btn_save = None

        self.setup_ui()

    def setup_ui(self):
        self.setup_window()
        self.setup_centra_ui()

    def setup_window(self):
        self.setWindowTitle("Ventas")

    def setup_centra_ui(self):
        layout = QVBoxLayout()

        client_layout = QHBoxLayout()
        client_layout.addWidget(QLabel("Cliente:"))
        self.cmb_client = QComboBox()
        client_layout.addWidget(self.cmb_client)
        layout.addLayout(client_layout)

        self.tbl_products = QTableWidget()
        self.tbl_products.setColumnCount(5)
        self.tbl_products.setHorizontalHeaderLabels(["Producto", "Unidad", "Cantidad", "Precio Unitario", "Subtotal"])
        layout.addWidget(self.tbl_products)

        total_layout = QHBoxLayout()
        total_layout.addWidget(QLabel("Total:"))
        self.txt_total = QLineEdit("0.00")
        self.txt_total.setReadOnly(True)
        total_layout.addWidget(self.txt_total)
        layout.addLayout(total_layout)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Agregar Producto")
        self.btn_save = QPushButton("Realizar Venta")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_save)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
