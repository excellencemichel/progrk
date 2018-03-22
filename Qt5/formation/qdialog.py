#! /usr/bin/python

#-*-coding:utf-8 -*-


"""
Fichoer pour la demontration de la classe QDialog

Il faut noter toute application utilisant le module de l'interface graphique doit forcement
instancier la classe QApplication c'est elle qui fait la liaison ebtre
le système d'exploitation et l'application donc son instanciation
est avant tout primordiale pour tout ouverture d'interface
graphique
"""


from sys import argv, exit
import pickler

from  PyQt5.QtWidgets import *
from PyQt5 import QtCore



class Demo(QDialog):

    def __init__(self):
        QApplication.__init__(self)#Appel du contructeur de la QApplication


        #Dialogue de selection de fichier

        s = QFileDialog.getOpenFileName(self, "Overture de fichier ", "/home/michel", "Boite d'ouverture de fichier" , "Choisissez")

        #Conversions nécéssaires entre QString et le type str de python
        h ="<h1> Vous avez choisi le fichier </h1><i>", s , "</i>"


        #Message d'information sur le fichier selectionné
        QMessageBox.information(self, "Fichier choisi", str(h))





if __name__=="__main__":
    app = QApplication(argv)

    dialogue = Demo()

    dialogue.show()


    exit(app.exec_())


