from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox,
    QTableWidget, QLineEdit, QPushButton, QGroupBox, QFormLayout,
    QHeaderView, QSizePolicy, QToolButton, QAbstractItemView
)


class NewSaleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.txt_client_name = None
        self.txt_nit = None
        self.txt_phone = None
        self.txt_address = None
        self.tbl_products = None
        self.txt_total = None
        self.txt_payment = None
        self.txt_change = None

        self.btn_add = None
        self.btn_delete = None
        self.btn_clear = None

        self.btn_save = None
        self.btn_cancel = None
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

        self.txt_client_name = QLineEdit()
        self.txt_client_name.setPlaceholderText("Nombre del cliente")

        self.txt_nit = QLineEdit()
        self.txt_phone = QLineEdit()
        self.txt_address = QLineEdit()

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("NIT:"))
        row1.addWidget(self.txt_nit)
        row1.addWidget(QLabel("Teléfono:"))
        row1.addWidget(self.txt_phone)
        row1.addWidget(QLabel("Dirección:"))
        row1.addWidget(self.txt_address)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Cliente:"))
        layout.addWidget(self.txt_client_name)
        layout.addSpacing(8)
        layout.addLayout(row1)

        box.setLayout(layout)
        return box

    def setup_product_section(self):
        box = QGroupBox("Productos")
        layout = QVBoxLayout()

        # Tabla
        self.tbl_products = QTableWidget()
        self.tbl_products.setColumnCount(6)
        self.tbl_products.setHorizontalHeaderLabels(
            ["Código", "Producto", "Color", "Cantidad", "Precio Unitario", "Subtotal"]
        )
        header = self.tbl_products.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.tbl_products.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_products.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_products.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
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
        layout = QHBoxLayout()

        self.txt_total = QLineEdit("0.00")
        self.txt_total.setReadOnly(True)
        total_box = QVBoxLayout()
        total_box.addWidget(QLabel("Total:"))
        total_box.addWidget(self.txt_total)

        self.txt_payment = QLineEdit()
        self.txt_payment.setPlaceholderText("Pago del cliente")
        payment_box = QVBoxLayout()
        payment_box.addWidget(QLabel("Pago:"))
        payment_box.addWidget(self.txt_payment)

        self.txt_change = QLineEdit("0.00")
        self.txt_change.setReadOnly(True)
        change_box = QVBoxLayout()
        change_box.addWidget(QLabel("Cambio:"))
        change_box.addWidget(self.txt_change)

        layout.addLayout(total_box)
        layout.addLayout(payment_box)
        layout.addLayout(change_box)

        box.setLayout(layout)

        return box

    def setup_footer_buttons(self):
        btn_layout = QHBoxLayout()
        self.btn_cancel = QPushButton("❌ Cancelar Venta")
        self.btn_cancel.setFixedHeight(40)
        self.btn_cancel.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.btn_save = QPushButton("💾 Realizar Venta")
        self.btn_save.setFixedHeight(40)
        self.btn_save.setStyleSheet("font-size: 14px; font-weight: bold;")

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_cancel)
        btn_layout.addWidget(self.btn_save)
        btn_layout.addStretch()

        return btn_layout
