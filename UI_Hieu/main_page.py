import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_page_new.ui", self)  # Load file UI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
