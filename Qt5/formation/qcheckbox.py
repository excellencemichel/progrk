#! /usr/bin/python
#-*-coding:utf-8 -*-




"""
Programme exemple pour les boutons de selection
"""


import  sys


from PyQt5.QtWidgets import *


class Demo(QApplication):
    def __init__(self, args):
        """
        Le contructeur qu'on donne la possibilité d'appeler le constructeur de QApplication
        :param args:
        """

        QApplication.__init__(self, args)

        #Widget principale, il s'agit d'une fenêtre de dialogue
        self.dialogue = QDialog() #Qu'on le rend disponible dans l'interface
        self.dialogue.setWindowTitle(("Fenêtre de dialogue"))
        #Astuce: On peut regrouper les boutons grâce à la classe
        # QButtonGroup;; positionnement horizontal des boutons
        self.groupe1 = QGroupBox("Essai QCheckBox", self.dialogue)
        self.groupe1.setObjectName("Groupe1")
        #Définition de 3 checkboxes
        self.check1 = QCheckBox("checkbox 1")
        self.check2 = QCheckBox("checkbox 2")
        self.check3 = QCheckBox("checkbox 3")

        #on met le bouton check1 en état de tristate
        self.check1.setTristate()

        #Le bouton ckeck2 est par défaut coché
        self.check2.setChecked(True)

        #Le bouton chec 3 n'est pas modifiable
        self.check3.setDisabled(True)


        #Layout vertical pour les checkboxes
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.check1)
        self.vbox.addWidget(self.check2)
        self.vbox.addWidget(self.check3)
        self.vbox.addStretch(1)
        self.groupe1.setLayout(self.vbox)
        #Layout pour le groupe
        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.groupe1)
        self.dialogue.setLayout(self.vbox2)

        #Affichage
        self.dialogue.show()
        self.lastWindowClosed.connect(quit)
        self.exec_()



if __name__ == '__main__':
    app = Demo(sys.argv)

