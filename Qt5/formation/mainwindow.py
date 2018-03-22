#! /usr/bin/python

#-*-coding:utf-8 -*-




"""
Fichier pour la démonstration de la classe QMainWindow

"""

import sys


from PyQt5.QtWidgets import *






class Demo(QApplication):

    def __init__(self,args):
        QApplication.__init__(self, args)


        #widget principal, il s'agit d'une fenêtre de dialogue

        self.main = QMainWindow()
        self.main.setWindowTitle("Demo QMainWindow")
        self.main.resize(640, 480)


        #widget central : QTextEdit
        self.edit = QTextEdit("Editeur", self.main)
        self.edit.setFocus()
        self.main.setCentralWidget(self.edit)


        #Ajout facile d'éléments dans la barre de menu
        #Note: crée la barre s'il n'existe pas
        self.main.menuBar().addAction("New")
        self.main.menuBar().addAction("Quit")


        #Changement du message de status
        #NOTE: crée la zone de status si inexistante
        self.main.statusBar().showMessage("Demo en cours", 10000)
        self.main.show()

        self.lastWindowClosed.connect(self.quit)
        self.exec_()



if __name__=="__main__":
    # app = QApplication(sys.argv)

    mainwindow = Demo(sys.argv)

