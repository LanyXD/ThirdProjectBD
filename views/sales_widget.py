from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SalesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Pantalla de Venta"))
        self.setLayout(layout)
