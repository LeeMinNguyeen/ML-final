from predict import LSTM_model
import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from LoginWindow import Ui_LoginWindow
from SignUpWindow import Ui_SignUpWindow
from connect_database import connector
from MainWindow import Ui_MainWindow
from DataObject import ForexData

from datetime import datetime
from Backtesting import TrendFollow


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MongoDatabase(connector):
    def __init__(self):
        super().__init__()
        self.connects()
        
    def disconnect(self):
        self.connector.client.close()
        
class Backtest():
    pass

class MainScreen(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.db = MongoDatabase()
        self.MainWindow = MainWindow

        self.GetDateTime()
        self.GetCurrencyPairs()
        self.GetGrainularity()
        
        self.setUpSignals()
        
    def setUpSignals(self):
        self.comboBox_select_currency.currentIndexChanged.connect(self.UpdateCurrencyPairs)
        self.comboBox_select_currency_2.currentIndexChanged.connect(self.UpdateCurrencyPairs2)
        self.comboBox_select_currency_5.currentIndexChanged.connect(self.UpdateCurrencyPairs5)
        
        self.comboBox_select_granularity.currentIndexChanged.connect(self.UpdateGrainularity)
        self.comboBox_select_granularity_2.currentIndexChanged.connect(self.UpdateGrainularity2)
        
        self.pushButton_load.clicked.connect(self.LoadGraph)
        self.pushButton_StartBacktest.clicked.connect(self.StartBacktest)
        self.pushButtonSaveResult.clicked.connect(self.SaveBacktest)
        
        self.pushButton_Predict.clicked.connect(self.StartPrediction)
        self.pushButton_SavePrediction.clicked.connect(self.SavePrediction)
        
        self.StartdateTimeEdit.dateTimeChanged.connect(self.GetDateTime)
        self.EnddateTimeEdit.dateTimeChanged.connect(self.GetDateTime)
        
        self.StartdateTimeEdit_2.dateTimeChanged.connect(self.GetDateTime2)
        self.EnddateTimeEdit_2.dateTimeChanged.connect(self.GetDateTime2)
        
        self.StartdateTimeEdit_5.dateTimeChanged.connect(self.GetDateTime3)
        self.EnddateTimeEdit_5.dateTimeChanged.connect(self.GetDateTime3)
    
    def GetGrainularity(self):
        self.Grainularity = []
        for collection in self.db.db.list_collection_names():
            if collection != "Users":
                grain = collection.split('_')[1]
                if grain not in self.Grainularity:
                    self.Grainularity.append(grain)
        self.comboBox_select_granularity.addItems(self.Grainularity)
        self.comboBox_select_granularity_2.addItems(self.Grainularity)
        self.comboBox_select_granularity_5.addItems(self.Grainularity)
    def GetCurrencyPairs(self):
        self.CurrencyPairs = []
        for collection in self.db.db.list_collection_names():
            if collection != "Users":
                pair = collection[:3] + "/" + collection[3:6]
                if pair not in self.CurrencyPairs:
                    self.CurrencyPairs.append(pair)
        self.comboBox_select_currency.addItems(self.CurrencyPairs)
        self.comboBox_select_currency_2.addItems(self.CurrencyPairs)
        self.comboBox_select_currency_5.addItems(self.CurrencyPairs)
    
    def UpdateCurrencyPairs(self):
        self.currency_pair = self.comboBox_select_currency.currentText()
        self.comboBox_select_currency.setCurrentText(self.currency_pair)
        self.comboBox_select_currency_2.setCurrentText(self.currency_pair)
        self.comboBox_select_currency_5.setCurrentText(self.currency_pair)
    def UpdateCurrencyPairs2(self):
        self.currency_pair = self.comboBox_select_currency_2.currentText()
        self.comboBox_select_currency.setCurrentText(self.currency_pair)
        self.comboBox_select_currency_2.setCurrentText(self.currency_pair)
        self.comboBox_select_currency_5.setCurrentText(self.currency_pair)
    def UpdateCurrencyPairs5(self):
        self.currency_pair = self.comboBox_select_currency_5.currentText()
        self.comboBox_select_currency.setCurrentText(self.currency_pair)
        self.comboBox_select_currency_2.setCurrentText(self.currency_pair)
        self.comboBox_select_currency_5.setCurrentText(self.currency_pair)
        
    def UpdateGrainularity(self):
        self.grainularity = self.comboBox_select_granularity.currentText()
        self.comboBox_select_granularity.setCurrentText(self.grainularity)
        self.comboBox_select_granularity_2.setCurrentText(self.grainularity)
    def UpdateGrainularity2(self):
        self.grainularity = self.comboBox_select_granularity_2.currentText()
        self.comboBox_select_granularity.setCurrentText(self.grainularity)
        self.comboBox_select_granularity_2.setCurrentText(self.grainularity)
    
    def GetDateTime(self):
        self.StartDate = datetime.strptime(self.StartdateTimeEdit.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        self.EndDate = datetime.strptime(self.EnddateTimeEdit.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        
        self.StartdateTimeEdit_2.setDateTime(self.StartdateTimeEdit.dateTime())
        self.EnddateTimeEdit_2.setDateTime(self.EnddateTimeEdit.dateTime())
        
        self.StartdateTimeEdit_5.setDateTime(self.StartdateTimeEdit.dateTime())
        self.EnddateTimeEdit_5.setDateTime(self.EnddateTimeEdit.dateTime())
    def GetDateTime2(self):
        self.StartDate = datetime.strptime(self.StartdateTimeEdit_2.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        self.EndDate = datetime.strptime(self.EnddateTimeEdit_2.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        
        self.StartdateTimeEdit.setDateTime(self.StartdateTimeEdit_2.dateTime())
        self.EnddateTimeEdit.setDateTime(self.EnddateTimeEdit_2.dateTime())
        
        self.StartdateTimeEdit_5.setDateTime(self.StartdateTimeEdit_2.dateTime())
        self.EnddateTimeEdit_5.setDateTime(self.EnddateTimeEdit_2.dateTime())
    def GetDateTime3(self):
        self.StartDate = datetime.strptime(self.StartdateTimeEdit_5.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        self.EndDate = datetime.strptime(self.EnddateTimeEdit_5.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        
        self.StartdateTimeEdit.setDateTime(self.StartdateTimeEdit_5.dateTime())
        self.EnddateTimeEdit.setDateTime(self.EnddateTimeEdit_5.dateTime())
        
        self.StartdateTimeEdit_2.setDateTime(self.StartdateTimeEdit_5.dateTime())
        self.EnddateTimeEdit_2.setDateTime(self.EnddateTimeEdit_5.dateTime())
    
    def LoadData(self, currency_pair = None, grainularity = None):
        self.data = ForexData(currency_pair = currency_pair, grainularity = grainularity)
        self.data.GetData()
    
    def LoadGraph(self):
        self.currency_pair = self.comboBox_select_currency.currentText()
        self.grainularity = self.comboBox_select_granularity.currentText()
        
        self.LoadData(currency_pair = self.currency_pair, grainularity = self.grainularity)
        
        if not(self.verticalLayout.isEmpty()):
            self.verticalLayout.removeWidget(self.canvas)
        fig = self.data.CandlePlot(startdate = self.StartDate, enddate = self.EndDate)
        self.canvas = FigureCanvas(fig)
        self.verticalLayout.addWidget(self.canvas)
        
    def StartBacktest(self):
        self.currency_pair = self.comboBox_select_currency_2.currentText()
        self.grainularity = self.comboBox_select_granularity_2.currentText()
        StartMoney = float(self.StartMoney.text())
        MaxPosition = int(self.MaxPosition.text())
        Slippage = float(self.Slippage.text())
        MA_Length = int(self.MA_Length.text())
        self.StartDate = datetime.strptime(self.StartdateTimeEdit_2.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        self.EndDate = datetime.strptime(self.EnddateTimeEdit_2.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        
        self.LoadData(currency_pair = self.currency_pair, grainularity = self.grainularity)
        
        self.backtest = TrendFollow(data = self.data.df, start = self.StartDate, end = self.EndDate)
        self.backtest_result = self.backtest.trade(length = MA_Length, money = StartMoney, slippage = Slippage, max_position = MaxPosition)
        self.stats = self.backtest.CalculateStats()
        
        action_table = self.backtest_result[["Action", "position_count", "equity"]]
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(action_table.columns)
        self.tableWidget.setRowCount(len(action_table))
        self.tableWidget.setColumnCount(len(action_table.columns))
        for i in range(len(action_table)):
            for j in range(len(action_table.columns)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(action_table.iloc[i, j])))
                
        self.DrawBackTestGraph()
        self.ShowStats()
    
    def DrawBackTestGraph(self):
        if not(self.verticalLayout_Output.isEmpty()):
            self.verticalLayout_Output.removeWidget(self.canvas_2)
        plot_result = self.backtest_result[["equity"]]
        ax = plot_result.plot(logy=True)
        fig = ax.get_figure()
        self.canvas_2 = FigureCanvas(fig)
        self.verticalLayout_Output.addWidget(self.canvas_2)
    
    def ShowStats(self):
        stats_dialog = QtWidgets.QMessageBox()
        stats_dialog.setWindowTitle("Backtest Statistics")
        stats_dialog.setText(self.stats)
        stats_dialog.exec()
        
    def SaveBacktest(self):
        folder = "backend/data/Backtest/"
        self.backtest_result.to_csv(f"{folder}Backtest_Result.csv")
        with open(f"{folder}Backtest_Stats.csv", "w") as file:
            file.write(self.stats)
        
        success_dialog = QtWidgets.QMessageBox()
        success_dialog.setWindowTitle("Save Successful")
        success_dialog.setText("Backtest results and statistics have been saved successfully.")
        success_dialog.exec()

    def StartPrediction(self):
        self.currency_pair = self.comboBox_select_currency_5.currentText()
        self.StartDate = datetime.strptime(self.StartdateTimeEdit_5.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        self.EndDate = datetime.strptime(self.EnddateTimeEdit_5.dateTime().toString("yyyy/MM/dd hh:mm:ss"), '%Y/%m/%d %H:%M:%S')
        
        self.LoadData(currency_pair = self.currency_pair, grainularity = "H4")
        
        self.predict = LSTM_model(data = self.data.df, start = self.StartDate, end = self.EndDate)
        self.predict.GetModel("LSTM")
        self.predict.Predict()
        print("Predicted")
        self.DrawPredictionGraph()
        
    def DrawPredictionGraph(self):
        if not(self.verticalLayout_4.isEmpty()):
            self.verticalLayout_4.removeWidget(self.canvas_3)
        fig = self.predict.DrawResultGraph()
        self.canvas_3 = FigureCanvas(fig)
        self.verticalLayout_4.addWidget(self.canvas_3)
    
    def SavePrediction(self):
        self.predict.SaveModel(self.predict.model, "LSTM")

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