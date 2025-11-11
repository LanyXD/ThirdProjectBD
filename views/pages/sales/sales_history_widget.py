from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QPushButton, QHeaderView, QLabel, QSizePolicy
)


class SalesHistoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tbl_sales = None
        self.btn_refresh = None
        self.btn_delete = None
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        title = QLabel("Historial de Ventas")
        title.setObjectName("titulo")
        main_layout.addWidget(title)

        self.tbl_sales = QTableWidget()
        self.tbl_sales.setColumnCount(6)
        self.tbl_sales.setHorizontalHeaderLabels(
            ["ID Venta", "Cliente", "Fecha", "Total", "Pago", "Cambio"]
        )
        self.tbl_sales.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_sales.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(self.tbl_sales)

        main_layout.addLayout(self.setup_buttons())

        self.setLayout(main_layout)

    def setup_buttons(self):
        btn_layout = QHBoxLayout()

        self.btn_refresh = QPushButton("🔄 Actualizar")
        self.btn_delete = QPushButton("🗑️ Eliminar Venta")
        self.btn_refresh.setFixedHeight(35)
        self.btn_delete.setFixedHeight(35)

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_refresh)
        btn_layout.addWidget(self.btn_delete)
        return btn_layout
