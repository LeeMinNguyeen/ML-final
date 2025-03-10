import sys, os

for folder in os.listdir('./UI'):
    sys.path.append(os.path.abspath('./UI/'+folder))

from PyQt6 import QtWidgets
from LoginWindow import Ui_Form
from SignInWindow import Ui_SignInWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())