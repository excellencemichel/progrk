#!/usr/bin/python
#-*-coding:utf-8-*-


import sys

from PyQt5.QtWidgets import *


#Classe définissant un button avec le texte Hello World !

class HelloButton(QPushButton):
	def __init__(self, args):
		QPushButton.__init__(self, None)

		self.setText("Hello World ! C'est moi \n Excellence Michel qui vous salut")




class HelloApplication(QApplication):

	def __init__(self, args):

		QApplication.__init__(self, args)

		#Création et affichage d'un objet HelloButton
		self.button = HelloButton(self)
		self.button.show()


		#Traitement des divers evenements
		self.lastWindowClosed.connect(self.quit) #Mais ce evenement est gérer par défaut par le système exploitation
		self.button.clicked.connect(self.quit)


		#Boucle principale de traitement des evenements

		self.exec()


if __name__ == "__main__":
	app = HelloApplication(sys.argv)