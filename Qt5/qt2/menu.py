#! /usr/bin/python3
#-*-condig:utf-8-*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore



class MenuDemo(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		super().__init__()

		#Create Menu Bar
		bar = self.menuBar()

		#Create Root Menus : La création des menus chaque variable crée ici une rentrée de menu
		file = bar.addMenu("File")
		edit = bar.addMenu("Edit")
		create = bar.addMenu("Create")
		quit = bar.addMenu("Quit")

		#Create Actions for Menus : Création des actions qui divent être liées aux menus

		save_action = QtWidgets.QAction("Save", self) #L'argument self permet d'afficher ce menu dans ce widget sinon ça ne va pas s'afficher
		save_action.setShortcut("Ctr+S")


		new_action = QtWidgets.QAction("New", self)
		new_action.setShortcut("Ctr+N")


		open_file = QtWidgets.QAction("Fichier", self)
		open_file.setShortcut("Ctr+O")

		open_folder = QtWidgets.QAction("Dossier", self)
		open_folder.setShortcut("Ctr+Mjc+N")



		quit_action = QtWidgets.QAction("Quit", self)
		quit_action.setShortcut("Ctr+Q")

		find_action = QtWidgets.QAction("Find..", self)

		replace_action = QtWidgets.QAction("Replace...", self)

		#Add Actions to Menus : Liaison des actions à la barre de menu
		#Ici on lie à l'entrée menu 'File' deux action, quand clique dessus il affiche les actions
		file.addAction(new_action) #Laison de l'action new_action au menu file
		file.addAction(save_action)

		#Alborescence du menu : Permet de donner au menu des sous menu
		find_file = file.addMenu("Moi") #Liason d'un sous menu find_file au menu principale file
		find_file.addAction(new_action) #Liaison de l'action new_action au sous menu find_file
		find_file.addAction(quit_action)
		
		# file.addAction(quit_action)


		find_menu = edit.addMenu("Open") #Sous menu à edit
		find_menu.addAction(open_file) #Liaison des action
		find_menu.addAction(open_folder)


		# quit.addAction(quit_action)

		#Events

		#Liaison des evenements que peuvent avoir les actions
		quit_action.triggered.connect(self.quit_trigger)
		file.triggered.connect(self.selected)
		quit.triggered.connect(self.quit_trigger) #Liaison directe du menu à l'action de la fonction






		self.setWindowTitle("My Menus")
		self.resize(600,400)

		self.show()


	def quit_trigger(self):
		"""
		Fonction permettant de fermer l'application
		"""
		QtWidgets.qApp.quit() #qApp permet d'avoir accès à QApplication qui gère la liaison de l'application au système d'exploitation dans le programme


	def selected(self, q):
		print(q.text() + " selected")




if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MenuDemo()

	sys.exit(app.exec_())