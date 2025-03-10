import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from LoginWindow import Ui_Form
from SignInWindow import Ui_SignInWindow
from connect_database import connector

class SignInUI(Ui_SignInWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonCreateNewAccount.clicked.connect(self.CreateNewAccount)
        
    def showWindow(self):
        self.MainWindow.show()
        
    def CreateNewAccount(self):
        print("Create New Account")
        self.openLoginWindow()
        
    def openLoginWindow(self):
        self.MainWindow.hide()
        AltWindow = QtWidgets.QMainWindow()
        self.loginWindow = LoginUI()
        self.loginWindow.setupUi(AltWindow)
        self.loginWindow.showWindow()
        
class LoginUI(Ui_Form):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonSignIn.clicked.connect(self.checkLogin)
        
    def showWindow(self):
        self.MainWindow.show()
        
    def checkLogin(self):
        print("Check Login")
        self.openSignInWindow()

    def openSignInWindow(self):
        self.MainWindow.hide()
        AltWindow = QtWidgets.QMainWindow()
        self.signInWindow = SignInUI()
        self.signInWindow.setupUi(AltWindow)
        self.signInWindow.showWindow()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginUI()
    ui.setupUi(MainWindow)
    ui.showWindow()
    
    sys.exit(app.exec())