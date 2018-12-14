# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatrice.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculatrice(object):
    def setupUi(self, Calculatrice):
        Calculatrice.setObjectName("Calculatrice")
        Calculatrice.resize(273, 44)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Calculatrice)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBoxNombre1 = QtWidgets.QSpinBox(Calculatrice)
        self.spinBoxNombre1.setObjectName("spinBoxNombre1")
        self.horizontalLayout.addWidget(self.spinBoxNombre1)
        self.comboBoxOperation = QtWidgets.QComboBox(Calculatrice)
        self.comboBoxOperation.setObjectName("comboBoxOperation")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxOperation)
        self.spinBoxNombre2 = QtWidgets.QSpinBox(Calculatrice)
        self.spinBoxNombre2.setObjectName("spinBoxNombre2")
        self.horizontalLayout.addWidget(self.spinBoxNombre2)
        self.pushButtonEgal = QtWidgets.QPushButton(Calculatrice)
        self.pushButtonEgal.setObjectName("pushButtonEgal")
        self.horizontalLayout.addWidget(self.pushButtonEgal)
        self.labelResultat = QtWidgets.QLabel(Calculatrice)
        self.labelResultat.setObjectName("labelResultat")
        self.horizontalLayout.addWidget(self.labelResultat)

        self.retranslateUi(Calculatrice)
        QtCore.QMetaObject.connectSlotsByName(Calculatrice)

    def retranslateUi(self, Calculatrice):
        _translate = QtCore.QCoreApplication.translate
        Calculatrice.setWindowTitle(_translate("Calculatrice", "Form"))
        self.comboBoxOperation.setItemText(0, _translate("Calculatrice", "+"))
        self.comboBoxOperation.setItemText(1, _translate("Calculatrice", "-"))
        self.comboBoxOperation.setItemText(2, _translate("Calculatrice", "*"))
        self.comboBoxOperation.setItemText(3, _translate("Calculatrice", "/"))
        self.pushButtonEgal.setText(_translate("Calculatrice", "="))
        self.labelResultat.setText(_translate("Calculatrice", "12"))

