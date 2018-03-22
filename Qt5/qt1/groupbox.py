# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupbox.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(682, 356)
        self.tableWidget = QtWidgets.QTableWidget(GroupBox)
        self.tableWidget.setGeometry(QtCore.QRect(480, 100, 191, 31))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(510, 60, 141, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setGeometry(QtCore.QRect(530, 150, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 200, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 250, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(GroupBox)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 461, 311))
        self.groupBox.setObjectName("groupBox")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        GroupBox.setTitle(_translate("GroupBox", "GroupBox"))
        self.label.setText(_translate("GroupBox", "Texte d\'Affichage"))
        self.pushButton.setText(_translate("GroupBox", "Save"))
        self.pushButton_2.setText(_translate("GroupBox", "New"))
        self.pushButton_3.setText(_translate("GroupBox", "Delete"))
        self.groupBox.setTitle(_translate("GroupBox", "GroupBox"))

