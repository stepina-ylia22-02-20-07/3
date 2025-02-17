import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow


class Espresso(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 30, 780, 560))
        self.table.setObjectName("table")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Эспрессо")


class MainWindow(QMainWindow, Espresso):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        if not db.open():
            print("Ошибка подключения к базе данных")
            return

        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        model.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "Название")
        model.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Степень обжарки")
        model.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "Тип кофе")
        model.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Описание")
        model.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "Цена")
        model.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "Объём")
        self.table.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Espresso()
    window.show()
    sys.exit(app.exec())
