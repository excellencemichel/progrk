# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Other1(object):
    def setupUi(self, Other1):
        Other1.setObjectName("Other1")
        Other1.resize(683, 396)
        self.centralwidget = QtWidgets.QWidget(Other1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(116, 39, 361, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QtCore.QSize(7, 7))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(210, 200, 171, 25))
        self.btn_open.setObjectName("btn_open")
        Other1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Other1)
        self.statusbar.setObjectName("statusbar")
        Other1.setStatusBar(self.statusbar)

        self.retranslateUi(Other1)
        QtCore.QMetaObject.connectSlotsByName(Other1)

    def retranslateUi(self, Other1):
        _translate = QtCore.QCoreApplication.translate
        Other1.setWindowTitle(_translate("Other1", "MainWindow"))
        self.label.setText(_translate("Other1", "Click to open window"))
        self.btn_open.setText(_translate("Other1", "Open window"))

