from PyQt6.QtWidgets import QApplication


def center_on_screen(self):
    screen = QApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())
