import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from LoginUI import LoginUI, SignInUI
from connect_database import connector

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
db = connector()
db.connects()

display = LoginUI()
display.setupUi(MainWindow)
display.showWindow()

sys.exit(app.exec())