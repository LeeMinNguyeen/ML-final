import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from LoginWindow import Ui_Form
from SignInWindow import Ui_SignInWindow
from connect_database import connector
from MainWindow import Ui_MainWindow

class MongoDatabase:
    def init(self):
        self.connector = connector()
        self.connector.connects()
    
    def disconnect(self):
        self.connector.client.close()

class MainScreen(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    
    def showWindow(self):
        self.MainWindow.show()

class SignInUI(Ui_SignInWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonCreateNewAccount.clicked.connect(self.CreateNewAccount)
        self.pushButtonLoginSignIn.clicked.connect(self.openLoginWindow)
        
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
        self.pushButtonLogin.clicked.connect(self.checkLogin)
        self.pushButtonSignIn.clicked.connect(self.openSignInWindow)
        
    def showWindow(self):
        self.MainWindow.show()
        
    def checkLogin(self):
        print("Check Login")
        
        '''
        username = self.label_6.text()
        password = self.label_7.text()
        
        result = connector.login(username, password)
        if result:
            print("Login Successful")
        else:
            print("Login Failed")
        '''
        self.openMainWindow()
        
    def openSignInWindow(self):
        self.MainWindow.hide()
        AltWindow = QtWidgets.QMainWindow()
        self.signInWindow = SignInUI()
        self.signInWindow.setupUi(AltWindow)
        self.signInWindow.showWindow()

    def openMainWindow(self):
        self.MainWindow.hide()
        AltWindow = QtWidgets.QMainWindow()
        self.mainWindow = MainScreen()
        self.mainWindow.setupUi(AltWindow)
        self.mainWindow.showWindow()
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginUI()
    ui.setupUi(MainWindow)
    ui.showWindow()
    
    sys.exit(app.exec())