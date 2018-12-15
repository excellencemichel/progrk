# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/michel/progrk/eric/TestQGraphics/test_scene.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 730)
        MainWindow.setStyleSheet("#dockWidget{\n"
" background-color:qlineargradient(spread:pad, x1:0.936, y1:0.188, x2:0.091, y2:1, stop:0 rgba(191, 249, 92, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vuePrincipale = QtWidgets.QGraphicsView(self.centralWidget)
        self.vuePrincipale.setObjectName("vuePrincipale")
        self.horizontalLayout.addWidget(self.vuePrincipale)
        MainWindow.setCentralWidget(self.centralWidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setStyleSheet("")
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonCreerDisque = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButtonCreerDisque.setObjectName("pushButtonCreerDisque")
        self.verticalLayout.addWidget(self.pushButtonCreerDisque)
        self.pushButtonChangerCouleur = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButtonChangerCouleur.setObjectName("pushButtonChangerCouleur")
        self.verticalLayout.addWidget(self.pushButtonChangerCouleur)
        self.lineEditTexte = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEditTexte.setObjectName("lineEditTexte")
        self.verticalLayout.addWidget(self.lineEditTexte)
        spacerItem = QtWidgets.QSpacerItem(20, 121, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.vueGlobale = QtWidgets.QGraphicsView(self.dockWidgetContents)
        self.vueGlobale.setObjectName("vueGlobale")
        self.verticalLayout.addWidget(self.vueGlobale)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.dialRotation = QtWidgets.QDial(self.dockWidgetContents)
        self.dialRotation.setMinimum(-180)
        self.dialRotation.setMaximum(180)
        self.dialRotation.setWrapping(True)
        self.dialRotation.setNotchTarget(30.0)
        self.dialRotation.setNotchesVisible(True)
        self.dialRotation.setObjectName("dialRotation")
        self.verticalLayout.addWidget(self.dialRotation)
        self.horizontalSliderZoom = QtWidgets.QSlider(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setKerning(True)
        self.horizontalSliderZoom.setFont(font)
        self.horizontalSliderZoom.setMinimum(10)
        self.horizontalSliderZoom.setMaximum(1000)
        self.horizontalSliderZoom.setTracking(True)
        self.horizontalSliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderZoom.setInvertedAppearance(False)
        self.horizontalSliderZoom.setInvertedControls(True)
        self.horizontalSliderZoom.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSliderZoom.setTickInterval(3)
        self.horizontalSliderZoom.setObjectName("horizontalSliderZoom")
        self.verticalLayout.addWidget(self.horizontalSliderZoom)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Boîte à outils"))
        self.pushButtonCreerDisque.setText(_translate("MainWindow", "Créer disque"))
        self.pushButtonChangerCouleur.setText(_translate("MainWindow", "Changer de couleur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

