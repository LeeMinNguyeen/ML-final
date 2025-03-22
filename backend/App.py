from UI import LoginUI
import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

display = LoginUI()
display.setupUi(MainWindow)
display.showWindow()

sys.exit(app.exec())    