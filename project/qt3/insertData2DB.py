#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QLineEdit,
		QPushButton,
		QMessageBox

		)

import psycopg2 as mdb



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Data"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):

		self.lineedit1 = QLineEdit(self)

		self.lineedit1.setPlaceholderText("Please enter Your Name")
		self.lineedit1.setGeometry(200,100,200,30)


		self.lineedit2 = QLineEdit(self)

		self.lineedit2.setPlaceholderText("Please enter Your Email")
		self.lineedit2.setGeometry(200,150,200,30)


		self.lineedit3 = QLineEdit(self)

		self.lineedit3.setPlaceholderText("Please enter Your Phone")
		self.lineedit3.setGeometry(200,200,200,30)

		self.button = QPushButton("Insert data", self)
		self.button.setGeometry(250, 250, 100, 30)
		self.button.clicked.connect(self.inserData)




		
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def inserData(self):
		try:
			#Connection à la base de données avec les paramètres nécésaaires
			connection = mdb.connect("dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' ")
			
			#C'est ça qui autorise la cr&tion des tbale sinon les fonction vont 100 fois s'exécuter rien ne va se passer
			connection.autocommit = True
			with connection:
				cusor = connection.cursor()
				cusor.execute("INSERT INTO mydb(name, email, phone) "
					            "VALUES('{}', '{}', '{}')".format(self.lineedit1.text(), self.lineedit2.text(), self.lineedit3.text()))
				QMessageBox.about(self, "Connection", "Successfully connected to DB")
				self.close()





		except mdb.Error as e:
			pprint("Cant connect dadabase")
			QMessageBox.about(self, "Connection", "Not connected Successfully {}".format(e))



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



