#!/usr/bin/python
#-*-coding:utf-8-*-


import sys

from PyQt5.QtWidgets import *




def main(args):
	"""
	Chaque programme doit disposser d'une instance de QApplication gérant l'ensemble des widgets


	"""
	app = QApplication(args)

	#Un nouveau en instanciant la classe QPushButton
	button = QPushButton("Hello World", None)


	#On l'affiche car les widgets ne sont pas visibles par défaut lors de leur création
	button.show()


	#fin de l'application lorsque toutes les fenêtres sont fermées
	app.lastWindowClosed.connect(quit)


	#fin de l'application lorsque l'utilisateur clique sur le bouton
	button.clicked.connect(quit)


	app.exec_()



if __name__=="__main__":
	main(sys.argv)


