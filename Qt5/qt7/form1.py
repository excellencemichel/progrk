# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(162, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(218, 258, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 3, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(348, 190, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 3)

        self.retranslateUi(Form)
        self.horizontalSlider.sliderMoved['int'].connect(self.label.setNum)
        self.horizontalSlider.sliderMoved['int'].connect(self.progressBar.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "0"))




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    f = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(f)
    f.show()

    sys.exit(app.exec_())

