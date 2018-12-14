# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestion.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{ \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.069, x2:1, y2:0, stop:0 rgba(127, 0, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0.069, x2:1, y2:0, stop:0 rgba(232, 232, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 241, 291))
        self.frame.setStyleSheet("#frame{background-color: qlineargradient(spread:pad, x1:0, y1:0.069, x2:1, y2:0, stop:0 rgba(197, 15, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(290, 40, 451, 291))
        self.frame_2.setStyleSheet("#frame_2{ \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.069, x2:1, y2:0, stop:0 rgba(232, 15, 15, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 9, 700, 411))
        self.widget.setStyleSheet("QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(132, 214, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_1.setGeometry(QtCore.QRect(0, 9, 400, 100))
        self.widget_1.setStyleSheet("QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(132, 214, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.widget_1.setObjectName("widget_1")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setGeometry(QtCore.QRect(240, 290, 80, 25))
        self.login_btn.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"/*\n"
"border:none;\n"
"C\'est pas idéal d\'enlever la bordure\n"
"*/")
        self.login_btn.setObjectName("login_btn")
        self.username_label = QtWidgets.QLabel(self.widget)
        self.username_label.setGeometry(QtCore.QRect(98, 160, 92, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.password_lineEdit.setGeometry(QtCore.QRect(240, 225, 142, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy)
        self.password_lineEdit.setStyleSheet("")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.signup_btn = QtWidgets.QPushButton(self.widget)
        self.signup_btn.setGeometry(QtCore.QRect(388, 290, 80, 25))
        self.signup_btn.setStyleSheet("color:#fff;")
        self.signup_btn.setObjectName("signup_btn")
        self.panel_label = QtWidgets.QLabel(self.widget)
        self.panel_label.setGeometry(QtCore.QRect(98, 83, 166, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel_label.sizePolicy().hasHeightForWidth())
        self.panel_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.panel_label.setFont(font)
        self.panel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_label.setObjectName("panel_label")
        self.username_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.username_lineEdit.setGeometry(QtCore.QRect(240, 160, 142, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_lineEdit.sizePolicy().hasHeightForWidth())
        self.username_lineEdit.setSizePolicy(sizePolicy)
        self.username_lineEdit.setStyleSheet("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_label = QtWidgets.QLabel(self.widget)
        self.password_label.setGeometry(QtCore.QRect(98, 225, 93, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.username_label.setBuddy(self.username_lineEdit)
        self.password_label.setBuddy(self.password_lineEdit)

        self.retranslateUi(MainWindow)
        self.login_btn.clicked.connect(self.widget.hide)
        if self.signup_btn.text() =="Sign p":
            self.signup_btn.clicked.connect(self.widget_1.hide)
        else:
            self.signup_btn.clicked.connect(self.widget.hide)
            self.signup_btn.clicked.connect(self.widget_1.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.username_label.setText(_translate("MainWindow", "USERNAME :"))
        self.signup_btn.setText(_translate("MainWindow", "Sign Up"))
        self.panel_label.setText(_translate("MainWindow", "Login form"))
        self.password_label.setText(_translate("MainWindow", "PASSWORD :"))



def main(args):
    app = QtWidgets.QApplication(args)
    f = QtWidgets.QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(f)
    f.show()

    r = app.exec_()
    return r


if __name__ == '__main__':
    import sys
    main(sys.argv)

