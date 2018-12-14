#! /usr/bin/python

#-*-coding:utf-8-*-


import sys
from pprint import  pprint


from PyQt5 import QtGui
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QPushButton,
		QMessageBox,


		)

import psycopg2 as mdb



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Connecting Database"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):

		self.button = QPushButton("DB Connection Status", self)
		self.button.setGeometry(100, 100, 200, 50)

		self.button.clicked.connect(self.connectDB)



		
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()




	def connectDB(self):
		try:
			#Connection à la base de données avec les paramètres nécésaaires
			self.connection = mdb.connect("dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' ")
			
			#C'est ça qui autorise la cr&tion des tbale sinon les fonction vont 100 fois s'exécuter rien ne va se passer
			self.connection.autocommit = True
			QMessageBox.about(self, "Connection", "Successfully connected to DB")


			# le curseur pour la communication avec la base de données
			self.cursor = self.connection.cursor()

		except mdb.OperationalError as e:

			pprint("Cant connect dadabase {}".format(e.code))
			QMessageBox.about(self, "Connection", "Not connected Successfully {}".format(e))
			sys.exit(1)






if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



