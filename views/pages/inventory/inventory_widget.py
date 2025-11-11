from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QHBoxLayout, QTableWidget,
    QHeaderView, QLabel, QLineEdit, QPushButton, QFormLayout, QSizePolicy
)


class InventoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tbl_inventory = None
        self.txt_search = None
        self.btn_add = None
        self.btn_edit = None
        self.btn_delete = None
        self.btn_clear = None
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.addWidget(self.setup_search_section())
        main_layout.addWidget(self.setup_table_section())
        main_layout.addLayout(self.setup_footer_buttons())

        self.setLayout(main_layout)

    def setup_search_section(self):
        box = QGroupBox("Buscar Producto")
        layout = QFormLayout()

        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("Ingrese nombre o código...")

        layout.addRow(QLabel("Búsqueda:"), self.txt_search)
        box.setLayout(layout)
        return box

    def setup_table_section(self):
        box = QGroupBox("Inventario Actual")
        layout = QVBoxLayout()

        self.tbl_inventory = QTableWidget()
        self.tbl_inventory.setColumnCount(5)
        self.tbl_inventory.setHorizontalHeaderLabels(
            ["Código", "Producto", "Precio (Q)", "Stock", "Unidad"]
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

        self.btn_add = QPushButton("➕ Agregar")
        self.btn_edit = QPushButton("✏️ Editar")
        self.btn_delete = QPushButton("🗑️ Eliminar")
        self.btn_clear = QPushButton("🧹 Limpiar")

        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_clear)

        return btn_layout
