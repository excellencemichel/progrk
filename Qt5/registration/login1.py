# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        DialogLogin.setObjectName("DialogLogin")
        DialogLogin.resize(661, 403)
        self.username_label = QtWidgets.QLabel(DialogLogin)
        self.username_label.setGeometry(QtCore.QRect(150, 180, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(DialogLogin)
        self.password_label.setGeometry(QtCore.QRect(150, 240, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.username_lineEdit = QtWidgets.QLineEdit(DialogLogin)
        self.username_lineEdit.setGeometry(QtCore.QRect(280, 180, 211, 25))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(DialogLogin)
        self.password_lineEdit.setGeometry(QtCore.QRect(280, 240, 211, 25))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_btn = QtWidgets.QPushButton(DialogLogin)
        self.login_btn.setGeometry(QtCore.QRect(280, 330, 71, 25))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QtWidgets.QPushButton(DialogLogin)
        self.signup_btn.setGeometry(QtCore.QRect(378, 330, 81, 25))
        self.signup_btn.setObjectName("signup_btn")
        self.panel_label = QtWidgets.QLabel(DialogLogin)
        self.panel_label.setGeometry(QtCore.QRect(200, 69, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.panel_label.setFont(font)
        self.panel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_label.setObjectName("panel_label")

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)

    def retranslateUi(self, DialogLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogLogin.setWindowTitle(_translate("DialogLogin", "Login form"))
        self.username_label.setText(_translate("DialogLogin", "USERNAME :"))
        self.password_label.setText(_translate("DialogLogin", "PASSWORD :"))
        self.login_btn.setText(_translate("DialogLogin", "Login"))
        self.signup_btn.setText(_translate("DialogLogin", "Sign Up"))
        self.panel_label.setText(_translate("DialogLogin", "Login form"))






if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogLogin()
    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec_())

