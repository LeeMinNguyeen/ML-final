# Form implementation generated from reading ui file 'D:\Uni\Nam3\Ki2\MLBA\Final\ML-final\UI\LoginWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1279, 852)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        LoginWindow.setFont(font)
        LoginWindow.setStyleSheet("")
        self.Background = QtWidgets.QLabel(parent=LoginWindow)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1279, 852))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("./Images/LoginBg.png"))
        self.Background.setObjectName("Background")
        self.label_6 = QtWidgets.QLabel(parent=LoginWindow)
        self.label_6.setGeometry(QtCore.QRect(710, 340, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=LoginWindow)
        self.label_7.setGeometry(QtCore.QRect(710, 430, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=LoginWindow)
        self.pushButtonLogin.setGeometry(QtCore.QRect(710, 520, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.label_8 = QtWidgets.QLabel(parent=LoginWindow)
        self.label_8.setGeometry(QtCore.QRect(710, 600, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButtonSignIn = QtWidgets.QPushButton(parent=LoginWindow)
        self.pushButtonSignIn.setGeometry(QtCore.QRect(730, 600, 62, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSignIn.setFont(font)
        self.pushButtonSignIn.setObjectName("pushButtonSignIn")
        self.lineEditPassWordLogin = QtWidgets.QLineEdit(parent=LoginWindow)
        self.lineEditPassWordLogin.setGeometry(QtCore.QRect(710, 450, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassWordLogin.setFont(font)
        self.lineEditPassWordLogin.setObjectName("lineEditPassWordLogin")
        self.lineEditUserNameLogin = QtWidgets.QLineEdit(parent=LoginWindow)
        self.lineEditUserNameLogin.setGeometry(QtCore.QRect(710, 361, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditUserNameLogin.setFont(font)
        self.lineEditUserNameLogin.setObjectName("lineEditUserNameLogin")
        self.label = QtWidgets.QLabel(parent=LoginWindow)
        self.label.setGeometry(QtCore.QRect(830, 160, 441, 151))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Form"))
        self.label_6.setText(_translate("LoginWindow", "User Name"))
        self.label_7.setText(_translate("LoginWindow", "Password"))
        self.pushButtonLogin.setText(_translate("LoginWindow", "Login"))
        self.label_8.setText(_translate("LoginWindow", "or "))
        self.pushButtonSignIn.setText(_translate("LoginWindow", "Sign up"))
        self.label.setText(_translate("LoginWindow", "Forex trading &\n"
"back testing system\n"
""))
