# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1279, 852)
        Form.setStyleSheet("")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1279, 852))
        self.graphicsView.setStyleSheet("border-image: url(:/Background/LoginBg.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(840, 140, 411, 161))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(720, 610, 348, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.pushButtonSignUp = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSignUp.setFont(font)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        self.horizontalLayout.addWidget(self.pushButtonSignUp)
        spacerItem = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(720, 340, 351, 261))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditUserName = QtWidgets.QLineEdit(self.splitter)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditPassWord = QtWidgets.QLineEdit(self.splitter)
        self.lineEditPassWord.setObjectName("lineEditPassWord")
        self.pushButtonLogin = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setObjectName("pushButtonLogin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Forex trading &\n"
"back testing system\n"
""))
        self.label_5.setText(_translate("Form", "or "))
        self.pushButtonSignUp.setText(_translate("Form", "Sign up"))
        self.label_2.setText(_translate("Form", "User Name"))
        self.label_4.setText(_translate("Form", "Password"))
        self.pushButtonLogin.setText(_translate("Form", "Login"))
import LoginWindow_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
