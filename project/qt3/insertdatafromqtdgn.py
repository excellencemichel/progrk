# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertdatafromqtdgn.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import psycopg2 as mdb
from pprint import  pprint


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_insertDataFromQtDgn(object):

    def insertData(self):
        name = [self.tableWidget.item(row,0).text() for row in range(self.tableWidget.rowCount())]
        email = [self.tableWidget.item(row,1).text() for row in range(self.tableWidget.rowCount())]
        phone = [self.tableWidget.item(row,2).text() for row in range(self.tableWidget.rowCount())]


        try:
            #Connection à la base de données avec les paramètres nécésaaires
            connection = mdb.connect("dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' ")
            
            #C'est ça qui autorise la cr&tion des tbale sinon les fonction vont 100 fois s'exécuter rien ne va se passer
            connection.autocommit = True
            with connection:
                cusor = connection.cursor()
                cusor.execute("INSERT INTO mydb(name, email, phone) "
                                "VALUES('%s', '%s', '%s')"%(''.join(name) ,
                                                             ''.join(email),
                                                             ''.join(phone)))

                pprint("Successfully connected")
                # QtWidgets.QMessageBox.about(self, "Connection", "Successfully connected to DB")





        except mdb.Error as e:
            pprint("Cant connect dadabase because : {}".format(e))
            # QtWidgets.QMessageBox.about(self, "Connection", "Not connected Successfully {}".format(e))




    def setupUi(self, insertDataFromQtDgn):
        insertDataFromQtDgn.setObjectName("insertDataFromQtDgn")
        insertDataFromQtDgn.resize(331, 394)
        self.centralwidget = QtWidgets.QWidget(insertDataFromQtDgn)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 0, 321, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 350, 89, 25))
        self.pushButton.setObjectName("pushButton")

        ########" connection signal" #####################""
        self.pushButton.clicked.connect(self.insertData)


        insertDataFromQtDgn.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(insertDataFromQtDgn)
        self.statusbar.setObjectName("statusbar")
        insertDataFromQtDgn.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(insertDataFromQtDgn)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menuBar.setObjectName("menuBar")
        insertDataFromQtDgn.setMenuBar(self.menuBar)

        self.retranslateUi(insertDataFromQtDgn)
        QtCore.QMetaObject.connectSlotsByName(insertDataFromQtDgn)

    def retranslateUi(self, insertDataFromQtDgn):
        _translate = QtCore.QCoreApplication.translate
        insertDataFromQtDgn.setWindowTitle(_translate("insertDataFromQtDgn", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("insertDataFromQtDgn", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("insertDataFromQtDgn", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("insertDataFromQtDgn", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("insertDataFromQtDgn", "Phone"))
        self.pushButton.setText(_translate("insertDataFromQtDgn", "Insert Data"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_insertDataFromQtDgn()

    ui.setupUi(window)

    window.show()


    sys.exit(app.exec_())
