import sys, os

sys.path.append(os.path.abspath('./UI'))

from PyQt6 import QtWidgets
from LoginWindow import Ui_Form
from SignInWindow import Ui_SignInWindow
from connect_database import connector

class MongoDatabase():
    def __init__(self):
        self.connector = connector()
        self.connector.connect()

app = QtWidgets.QApplication(sys.argv)
db = MongoDatabase()