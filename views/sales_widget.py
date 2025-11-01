from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox,
    QTableWidget, QLineEdit, QPushButton, QGroupBox, QFormLayout,
    QHeaderView, QSizePolicy
)


class SalesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cmb_client = None
        self.tbl_products = None
        self.txt_total = None
        self.txt_payment = None
        self.txt_change = None
        self.btn_add = None
        self.btn_save = None
        self.btn_delete = None
        self.btn_clear = None
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.addWidget(self.setup_client_section())
        main_layout.addWidget(self.setup_product_section())
        main_layout.addWidget(self.setup_totals_section())
        main_layout.addLayout(self.setup_footer_buttons())

        self.setLayout(main_layout)

    def setup_client_section(self):
        box = QGroupBox("Información del Cliente")
        layout = QFormLayout()

        self.cmb_client = QComboBox()
        self.cmb_client.setPlaceholderText("Seleccionar cliente...")

        layout.addRow(QLabel("Cliente:"), self.cmb_client)
        box.setLayout(layout)
        return box

    def setup_product_section(self):
        box = QGroupBox("Productos")
        layout = QVBoxLayout()

        # Tabla
        self.tbl_products = QTableWidget()
        self.tbl_products.setColumnCount(5)
        self.tbl_products.setHorizontalHeaderLabels(
            ["Producto", "Unidad", "Cantidad", "Precio Unitario", "Subtotal"]
        )
        header = self.tbl_products.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_products.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        layout.addWidget(self.tbl_products)

        layout.addLayout(self.setup_product_buttons())

        box.setLayout(layout)
        return box

    def setup_product_buttons(self):
        btn_layout = QHBoxLayout()

        self.btn_add = QPushButton("➕ Agregar")
        self.btn_delete = QPushButton("🗑️ Eliminar")
        self.btn_clear = QPushButton("🧹 Limpiar Lista")

        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_clear)

        return btn_layout

    def setup_totals_section(self):
        box = QGroupBox("Totales")
        layout = QFormLayout()

        self.txt_total = QLineEdit("0.00")
        self.txt_total.setReadOnly(True)

        self.txt_payment = QLineEdit()
        self.txt_payment.setPlaceholderText("Pago del cliente")

        self.txt_change = QLineEdit("0.00")
        self.txt_change.setReadOnly(True)

        layout.addRow(QLabel("Total:"), self.txt_total)
        layout.addRow(QLabel("Pago:"), self.txt_payment)
        layout.addRow(QLabel("Cambio:"), self.txt_change)

        box.setLayout(layout)
        return box

    def setup_footer_buttons(self):
        btn_layout = QHBoxLayout()
        self.btn_save = QPushButton("💾 Realizar Venta")
        self.btn_save.setFixedHeight(40)
        self.btn_save.setStyleSheet("font-size: 14px; font-weight: bold;")

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_save)
        btn_layout.addStretch()
        return btn_layout

