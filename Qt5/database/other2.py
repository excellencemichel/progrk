# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otherwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_otherwindow(object):
    def setupUi(self, otherwindow):
        otherwindow.setObjectName("otherwindow")
        otherwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(otherwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(136, 70, 271, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        otherwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(otherwindow)
        self.statusbar.setObjectName("statusbar")
        otherwindow.setStatusBar(self.statusbar)

        self.retranslateUi(otherwindow)
        QtCore.QMetaObject.connectSlotsByName(otherwindow)

    def retranslateUi(self, otherwindow):
        _translate = QtCore.QCoreApplication.translate
        otherwindow.setWindowTitle(_translate("otherwindow", "MainWindow"))
        self.label.setText(_translate("otherwindow", "Welcom to this window"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.agrv)

    OtherWindow = QtWidgets.MainWindow()

    ui = Ui_otherwindow()

    ui.setupUi(OtherWindow)

    OtherWindow.show()

    app.exec_()