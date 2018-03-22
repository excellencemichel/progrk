# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatrice.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_calculatrice(object):
    def setupUi(self, calculatrice):
        calculatrice.setObjectName("calculatrice")
        calculatrice.resize(520, 87)
        self.spinBoxNombre1 = QtWidgets.QSpinBox(calculatrice)
        self.spinBoxNombre1.setGeometry(QtCore.QRect(20, 10, 71, 41))
        self.spinBoxNombre1.setObjectName("spinBoxNombre1")
        self.comboBoxOperation = QtWidgets.QComboBox(calculatrice)
        self.comboBoxOperation.setGeometry(QtCore.QRect(120, 10, 86, 41))
        self.comboBoxOperation.setObjectName("comboBoxOperation")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.spinBoxNombre2 = QtWidgets.QSpinBox(calculatrice)
        self.spinBoxNombre2.setGeometry(QtCore.QRect(240, 10, 48, 41))
        self.spinBoxNombre2.setObjectName("spinBoxNombre2")
        self.pushButtonEgal = QtWidgets.QPushButton(calculatrice)
        self.pushButtonEgal.setGeometry(QtCore.QRect(310, 10, 89, 41))
        self.pushButtonEgal.setObjectName("pushButtonEgal")
        self.labelResultat = QtWidgets.QLabel(calculatrice)
        self.labelResultat.setGeometry(QtCore.QRect(420, 10, 67, 41))
        self.labelResultat.setObjectName("labelResultat")

        self.retranslateUi(calculatrice)
        QtCore.QMetaObject.connectSlotsByName(calculatrice)

    def retranslateUi(self, calculatrice):
        _translate = QtCore.QCoreApplication.translate
        calculatrice.setWindowTitle(_translate("calculatrice", "Form"))
        self.comboBoxOperation.setItemText(0, _translate("calculatrice", "+"))
        self.comboBoxOperation.setItemText(1, _translate("calculatrice", "-"))
        self.comboBoxOperation.setItemText(2, _translate("calculatrice", "*"))
        self.comboBoxOperation.setItemText(3, _translate("calculatrice", "/"))
        self.pushButtonEgal.setText(_translate("calculatrice", "="))
        self.labelResultat.setText(_translate("calculatrice", "0"))

