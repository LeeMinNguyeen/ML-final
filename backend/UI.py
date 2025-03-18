import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from LoginWindow import Ui_LoginWindow
from SignUpWindow import Ui_SignUpWindow
from connect_database import connector
from MainWindow import Ui_MainWindow

class MongoDatabase(connector):
    def __init__(self):
        super().__init__()
        self.connects()
        
    def disconnect(self):
        self.connector.client.close()

class MainScreen(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    
    def showWindow(self):
        self.MainWindow.show()

class SignUpUI(Ui_SignUpWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonCreateNewAccount.clicked.connect(self.CreateNewAccount)
        self.pushButtonLoginSignIn.clicked.connect(self.openLoginWindow)
        self.db = MongoDatabase()
        
    def showWindow(self):
        self.MainWindow.show()
        
    def CreateNewAccount(self):
        print("Create New Account")
        email = self.lineEditEmailAddress.text()
        username = self.lineEditUserNameSignUp.text()
        password = self.lineEditPassWordSignUp.text()
        
        # Check for existing user or email
        collection = self.db.db["Users"]
        duplicate_username = collection.find_one({"username": username})
        duplicate_email = collection.find_one({"email": email})
        if duplicate_email:
            print("User already exists")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('User already exists')
            error_dialog.exec()
            return
        elif duplicate_username:
            print("Email already exists")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Email already exists')
            error_dialog.exec()
            return
        
        result = self.db.NewUser(username = username, email = email, password = password)
        if result:
            print("New User Created")
            self.openLoginWindow()
        else:
            print("Failed to create new user")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Failed to create new user')
            error_dialog.exec()
        
    def openLoginWindow(self):
        self.MainWindow.hide()
        AltWindow = QtWidgets.QMainWindow()
        self.loginWindow = LoginUI()
        self.loginWindow.setupUi(AltWindow)
        self.loginWindow.showWindow()
        
class LoginUI(Ui_LoginWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonLogin.clicked.connect(self.checkLogin)
        self.pushButtonSignIn.clicked.connect(self.openSignInWindow)
        self.db = MongoDatabase()
        
    def showWindow(self):
        self.MainWindow.show()
        
    def checkLogin(self):
        username = self.lineEditUserNameLogin.text()
        password = self.lineEditPassWordLogin.text()
        
        result = self.db.login(username = username, password = password)
        if result:
            print("Login Successful")
            self.openMainWindow()
        else:
            print("Login Failed")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setText('Login Failed: Invalid username or password')
            error_dialog.exec()
        
    def openSignInWindow(self):
        self.MainWindow.hide()
        AltWindow = QtWidgets.QMainWindow()
        self.signInWindow = SignUpUI()
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