# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wellcom.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wellcom(object):
    def setupUi(self, Wellcom):
        Wellcom.setObjectName("Wellcom")
        Wellcom.resize(735, 363)
        Wellcom.setStyleSheet("QMainWindow{\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 232, 15, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(56, 232, 15, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(Wellcom)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        Wellcom.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Wellcom)
        self.statusbar.setObjectName("statusbar")
        Wellcom.setStatusBar(self.statusbar)

        self.retranslateUi(Wellcom)
        QtCore.QMetaObject.connectSlotsByName(Wellcom)

    def retranslateUi(self, Wellcom):
        _translate = QtCore.QCoreApplication.translate
        Wellcom.setWindowTitle(_translate("Wellcom", "Wellcom in here"))
        self.label.setText(_translate("Wellcom", "Wellcom to your handler"))
        self.label_2.setText(_translate("Wellcom", "Good morning friend !"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_Wellcom()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())