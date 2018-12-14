#-*- coding: utf-8-*-



from PyQt5.QtWidgets import  ( 
            QMainWindow,  QWidget,
            QLabel,  QLineEdit, 
            QPushButton,  QMessageBox, 
            QHBoxLayout,  QVBoxLayout
            )
from PyQt5.QtCore import QMetaObject,  pyqtSlot


#Locale import
from Ui_main_window_biblio import Ui_mainWindowBiblio

class MainWindowBiblio(QMainWindow,  Ui_mainWindowBiblio):
    def __init__(self,  parent=None):
        super(MainWindowBiblio,  self).__init__(parent)
        self.setupUi(self)
        self.resize(300, 150)
        self.setWindowTitle("Biblio App")
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.label = QLabel("Titre Alléluia",  self.centralWidget)
        self.lineEditTitre = QLineEdit(self.centralWidget)
        #self.lineEditTitre.move(97,0)
        self.pushButtonOK = QPushButton("OK",  self.centralWidget)
        #self.pushButtonOK.move(20, 40)
        #self.pushButtonOK.clicked.connect(self.onPushButtonOKClicked)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.label)
        self.hBoxLayout.addWidget(self.lineEditTitre)
        
        self.vBoxLayout = QVBoxLayout(self.centralWidget)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addStretch()
        
        self.hBoxLayout2 = QHBoxLayout()
        self.hBoxLayout2.addStretch()
        self.hBoxLayout2.addWidget(self.pushButtonOK)
        self.hBoxLayout2.addStretch()
        self.vBoxLayout.addLayout(self.hBoxLayout2)
        
#        self.vBoxLayou = t.addWidget(self.pushButtonOK)
        
        
        self.pushButtonOK.setObjectName("pushButtonOK")
        QMetaObject.connectSlotsByName(self)
    
    
    def onPushButtonOKClicked(self):
        QMessageBox.information(self,  "Info",  
        "Titre: " + self.lineEditTitre.text()
        )
        
        
        
    @pyqtSlot()
    def on_pushButtonOK_clicked(self):
        QMessageBox.information(self,  "Info", 
        "Titre entré : " + self.lineEditTitre.text())
