from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QTableWidget,
    QHeaderView, QLabel, QLineEdit, QPushButton, QFormLayout, QSizePolicy, QCheckBox, QStyle
)


class InventoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tbl_inventory = None
        self.txt_search = None

        self.chk_all = None
        self.chk_stock_low = None
        self.chk_barbecue = None

        self.btn_input = None
        self.btn_output = None
        self.btn_update = None
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.addWidget(self.setup_search_section())
        main_layout.addWidget(self.setup_table_section())
        main_layout.addLayout(self.setup_footer_buttons())

        self.setLayout(main_layout)

    def setup_search_section(self):
        box = QGroupBox("Buscar y Filtrar Producto")
        layout = QFormLayout()

        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("Ingrese nombre o código...")

        # Checkboxes de filtro
        filter_layout = QHBoxLayout()
        self.chk_all = QCheckBox("Todos")
        self.chk_stock_low = QCheckBox("Stock Bajo")
        self.chk_barbecue = QCheckBox("Barbacoa")

        filter_layout.addWidget(self.chk_all)
        filter_layout.addWidget(self.chk_stock_low)
        filter_layout.addWidget(self.chk_barbecue)
        filter_layout.addStretch()

        layout.addRow(QLabel("Búsqueda:"), self.txt_search)
        layout.addRow(QLabel("Filtros:"), filter_layout)

        box.setLayout(layout)
        return box

    def setup_table_section(self):
        box = QGroupBox("Inventario Actual")
        layout = QVBoxLayout()

        self.tbl_inventory = QTableWidget()
        self.tbl_inventory.setColumnCount(5)
        self.tbl_inventory.setHorizontalHeaderLabels(
            ["Código", "Producto", "Color", "Existencia", "Precio (Q)"]
        )

        header = self.tbl_inventory.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_inventory.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        layout.addWidget(self.tbl_inventory)
        box.setLayout(layout)
        return box

    def setup_footer_buttons(self):
        btn_layout = QHBoxLayout()

        self.btn_input = QPushButton("➕ Ingreso")
        self.btn_output = QPushButton("➖ Salida")
        self.btn_update = QPushButton("✏️ Actualizar")

        btn_layout.addWidget(self.btn_input)
        btn_layout.addWidget(self.btn_output)
        btn_layout.addWidget(self.btn_update)

        return btn_layout
