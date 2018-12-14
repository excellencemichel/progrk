# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectingdata.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
import psycopg2 as mdb

class Ui_SelectingData(object):



    def LoadData(self):
        try:
            conn = mdb.connect(
                                "dbname= 'formation' user='michel' host='localhost' port='5432' password ='SaintMichel'  " 
                                )


            with conn:
                cur = conn.cursor()

                cur.execute("SELECT * FROM mydb")

                for i in range(cur.rowcount):
                    result = cur.fetchall()

                    for row in result:
                        self.cursor = QTextCursor(self.textEdit.document())
                        self.cursor.insertText(str(row[1] + " " +  row[2] + " " + row[3] + " \n " ))  # oninsert l'antislash pour faire un retour à la ligne, les espaces autour sont nécéssaires

            print("La connection s'est bien passée")

        except mdb.Error as e:
            print("La connection a échouée voici le mobile : {}".format(e))


    def setupUi(self, SelectingData):
        SelectingData.setObjectName("SelectingData")
        SelectingData.resize(547, 444)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        SelectingData.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SelectingData)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 60, 541, 321))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 390, 89, 25))
        self.pushButton.setObjectName("pushButton")

        ############ signal #################
        self.pushButton.clicked.connect(self.LoadData)


        SelectingData.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SelectingData)
        self.statusbar.setObjectName("statusbar")
        SelectingData.setStatusBar(self.statusbar)

        self.retranslateUi(SelectingData)
        QtCore.QMetaObject.connectSlotsByName(SelectingData)

    def retranslateUi(self, SelectingData):
        _translate = QtCore.QCoreApplication.translate
        SelectingData.setWindowTitle(_translate("SelectingData", "MainWindow"))
        self.label.setText(_translate("SelectingData", "Select Data form Database PostGres SQl"))
        self.pushButton.setText(_translate("SelectingData", "Load Data"))




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_SelectingData()

    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())