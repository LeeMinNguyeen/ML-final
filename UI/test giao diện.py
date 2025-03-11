from UI.LoginWindow import Ui_LoginWindow

if __name__ == "__main__":
    import sys, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())