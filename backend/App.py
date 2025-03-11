import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from backend.UI import LoginUI, SignInUI, MainScreen, MongoDatabase

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

display = LoginUI()
display.setupUi(MainWindow)
display.showWindow()

sys.exit(app.exec())