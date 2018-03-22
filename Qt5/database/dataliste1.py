# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataliste1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dataliste(object):
    def setupUi(self, Dataliste):
        Dataliste.setObjectName("Dataliste")
        Dataliste.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dataliste)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 671, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(250, 390, 121, 25))
        self.btn_load.setObjectName("btn_load")
        Dataliste.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Dataliste)
        self.statusbar.setObjectName("statusbar")
        Dataliste.setStatusBar(self.statusbar)

        self.retranslateUi(Dataliste)
        QtCore.QMetaObject.connectSlotsByName(Dataliste)

    def retranslateUi(self, Dataliste):
        _translate = QtCore.QCoreApplication.translate
        Dataliste.setWindowTitle(_translate("Dataliste", "MainWindow"))
        self.btn_load.setText(_translate("Dataliste", "Load"))

