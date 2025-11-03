from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGraphicsOpacityEffect
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.logo = None
        self.title = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.addStretch()
        self.create_logo()
        layout.addWidget(self.logo)
        self.edit_title()
        layout.addWidget(self.title)
        layout.addStretch()

    def create_logo(self):
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = QPixmap("rsc/icons/sol.png").scaled(
            200, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logo.setPixmap(pixmap)

        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(0.5)
        self.logo.setGraphicsEffect(opacity)

    def edit_title(self):
        self.title = QLabel("La Súper Tienda")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("titulo")
