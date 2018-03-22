# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from database import create_db

class Ui_data_Window(object):
    def setupUi(self, data_Window):
        data_Window.setObjectName("data_Window")
        data_Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(data_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.id_db_create = QtWidgets.QLineEdit(self.centralwidget)
        self.id_db_create.setGeometry(QtCore.QRect(270, 110, 111, 25))
        self.id_db_create.setMinimumSize(QtCore.QSize(12, 12))
        self.id_db_create.setObjectName("id_db_create")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 111, 20))
        self.label.setObjectName("label")
        self.btn_db_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_db_create.setGeometry(QtCore.QRect(260, 170, 121, 25))
        self.btn_db_create.setObjectName("btn_db_create")

        ####################################################

        #########################################""
        self.btn_db_create.clicked.connect( lambda :  create_db(self.id_db_create.text()))
        ####################################################

        ###########################################################""
        data_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(data_Window)
        self.statusbar.setObjectName("statusbar")
        data_Window.setStatusBar(self.statusbar)

        self.retranslateUi(data_Window)
        QtCore.QMetaObject.connectSlotsByName(data_Window)

    def retranslateUi(self, data_Window):
        _translate = QtCore.QCoreApplication.translate
        data_Window.setWindowTitle(_translate("data_Window", "MainWindow"))
        self.id_db_create.setText(_translate("data_Window", "Database Name"))
        self.label.setText(_translate("data_Window", "PyQt DataBase"))
        self.btn_db_create.setText(_translate("data_Window", "Create"))





if __name__=="__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    data_Window = QtWidgets.QMainWindow()

    ui  = Ui_data_Window()

    ui.setupUi(data_Window)

    data_Window.show()


    sys.exit(app.exec_())