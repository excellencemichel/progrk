# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import sys


from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_DialogSignup(object):

    def setupUi(self, DialogSignup):
        DialogSignup.setObjectName("DialogSignup")
        DialogSignup.resize(597, 403)
        self.username_label = QtWidgets.QLabel(DialogSignup)
        self.username_label.setGeometry(QtCore.QRect(120, 130, 91, 21))
        self.username_label.setObjectName("username_label")
        self.email_label = QtWidgets.QLabel(DialogSignup)
        self.email_label.setGeometry(QtCore.QRect(120, 190, 91, 31))
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(DialogSignup)
        self.password_label.setGeometry(QtCore.QRect(120, 250, 91, 31))
        self.password_label.setObjectName("password_label")
        self.username_lineEdit = QtWidgets.QLineEdit(DialogSignup)
        self.username_lineEdit.setGeometry(QtCore.QRect(220, 130, 191, 25))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(DialogSignup)
        self.email_lineEdit.setGeometry(QtCore.QRect(220, 190, 191, 25))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(DialogSignup)
        self.password_lineEdit.setGeometry(QtCore.QRect(220, 250, 191, 25))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.signup_btn = QtWidgets.QPushButton(DialogSignup)
        self.signup_btn.setGeometry(QtCore.QRect(260, 320, 131, 25))
        self.signup_btn.setObjectName("signup_btn")


        self.panel_label = QtWidgets.QLabel(DialogSignup)
        self.panel_label.setGeometry(QtCore.QRect(140, 40, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.panel_label.setFont(font)
        self.panel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_label.setObjectName("panel_label")

        self.retranslateUi(DialogSignup)
        QtCore.QMetaObject.connectSlotsByName(DialogSignup)

    def retranslateUi(self, DialogSignup):
        _translate = QtCore.QCoreApplication.translate
        DialogSignup.setWindowTitle(_translate("DialogSignup", "Sign Up form "))
        self.username_label.setText(_translate("DialogSignup", "USERNAME"))
        self.email_label.setText(_translate("DialogSignup", "EMAIL ID"))
        self.password_label.setText(_translate("DialogSignup", "PASSWORD"))
        self.signup_btn.setText(_translate("DialogSignup", "Sign Up"))
        self.panel_label.setText(_translate("DialogSignup", "Create Account"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    ui = Ui_DialogSignup()

    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec_())
