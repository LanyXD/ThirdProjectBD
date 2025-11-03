from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class InventoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Pantalla de Inventario"))
        self.setLayout(layout)
