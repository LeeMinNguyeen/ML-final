# Form implementation generated from reading ui file 'D:\Uni\Nam3\Ki2\MLBA\Final\ML-final\UI\SignUpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(1279, 852)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        SignUpWindow.setFont(font)
        SignUpWindow.setStyleSheet("")
        self.label = QtWidgets.QLabel(parent=SignUpWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 1279, 852))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Images/SignUpBg.png"))
        self.label.setObjectName("label")
        self.pushButtonLoginSignIn = QtWidgets.QPushButton(parent=SignUpWindow)
        self.pushButtonLoginSignIn.setGeometry(QtCore.QRect(770, 660, 62, 19))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLoginSignIn.setFont(font)
        self.pushButtonLoginSignIn.setStyleSheet("background-color: rgb(248, 230, 255)")
        self.pushButtonLoginSignIn.setObjectName("pushButtonLoginSignIn")
        self.label_3 = QtWidgets.QLabel(parent=SignUpWindow)
        self.label_3.setGeometry(QtCore.QRect(830, 90, 441, 261))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditEmailAddress = QtWidgets.QLineEdit(parent=SignUpWindow)
        self.lineEditEmailAddress.setGeometry(QtCore.QRect(750, 420, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditEmailAddress.setFont(font)
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.lineEditUserNameSignUp = QtWidgets.QLineEdit(parent=SignUpWindow)
        self.lineEditUserNameSignUp.setGeometry(QtCore.QRect(750, 330, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditUserNameSignUp.setFont(font)
        self.lineEditUserNameSignUp.setObjectName("lineEditUserNameSignUp")
        self.label_6 = QtWidgets.QLabel(parent=SignUpWindow)
        self.label_6.setGeometry(QtCore.QRect(750, 490, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(parent=SignUpWindow)
        self.label_2.setGeometry(QtCore.QRect(750, 310, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=SignUpWindow)
        self.label_5.setGeometry(QtCore.QRect(750, 660, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditPassWordSignUp = QtWidgets.QLineEdit(parent=SignUpWindow)
        self.lineEditPassWordSignUp.setGeometry(QtCore.QRect(750, 510, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPassWordSignUp.setFont(font)
        self.lineEditPassWordSignUp.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassWordSignUp.setObjectName("lineEditPassWordSignUp")
        self.pushButtonCreateNewAccount = QtWidgets.QPushButton(parent=SignUpWindow)
        self.pushButtonCreateNewAccount.setGeometry(QtCore.QRect(750, 580, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCreateNewAccount.setFont(font)
        self.pushButtonCreateNewAccount.setStyleSheet("\n"
"background-color: rgb(219, 211, 255)")
        self.pushButtonCreateNewAccount.setObjectName("pushButtonCreateNewAccount")
        self.label_4 = QtWidgets.QLabel(parent=SignUpWindow)
        self.label_4.setGeometry(QtCore.QRect(750, 400, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(SignUpWindow)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "Form"))
        self.pushButtonLoginSignIn.setText(_translate("SignUpWindow", "Login"))
        self.label_3.setText(_translate("SignUpWindow", "Forex Trading &\n"
"Backtesting system\n"
""))
        self.label_6.setText(_translate("SignUpWindow", "Password"))
        self.label_2.setText(_translate("SignUpWindow", "User Name"))
        self.label_5.setText(_translate("SignUpWindow", "or "))
        self.pushButtonCreateNewAccount.setText(_translate("SignUpWindow", "Create New Account"))
        self.label_4.setText(_translate("SignUpWindow", "Email Address"))
