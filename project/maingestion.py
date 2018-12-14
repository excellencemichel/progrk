#! /usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5 import QtGui, QtWidgets, QtCore

# from PyQt5.QtWidgets import ( 
# 		QApplication,
# 		QMainWindow,

# 		)

from PyQt5.uic import loadUi

from gestion import Ui_MainWindow

from qt3.gridlayout import Window as gridlayout_widows




class Window(QtWidgets.QMainWindow, Ui_MainWindow):
	"""

	"""
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self)
		# super().__init__() # Appel du constructeur de la classe QMainWindow

		self.setupUi(parent)
		parent.setWindowIcon(QtGui.QIcon("icons/line.png"))
		my_wid = gridlayout_widows()
		# parent.setWidget(my_wid)
		# loadUi("gestion.ui", self)

		# QMainWindow.setWindowIcon(self,QtGui.QIcon("icons/line.png"))

		# self.setWindowTitle("La gestion des inscription")
		# self.database_connexion()
		# self.menu_barre_connexion.triggered.connect(self.widget_connexion.show)




	# def database_connexion(self):


	# 	self.widget_connexion = QtWidgets.QWidget(self)
	# 	self.widget_connexion.setGeometry(QtCore.QRect(12, 112, 521, 321))


	# 	hboxlayout = QtWidgets.QHBoxLayout()

	# 	dbname_lineEdit = QtWidgets.QLineEdit()
	# 	dbname_lineEdit.setPlaceholderText("Nom de la base de données")

	# 	dbuser_lineEdit = QtWidgets.QLineEdit()
	# 	dbuser_lineEdit.setPlaceholderText("L'utilisateur de la base de bonnées")

	# 	dbhost_lineEdit = QtWidgets.QLineEdit()
	# 	dbhost_lineEdit.setPlaceholderText("Serveur location")

	# 	dbpassword_lineEdit = QtWidgets.QLineEdit()
	# 	dbpassword_lineEdit.setPlaceholderText("Mot de passe")

	# 	dbport_lineEdit = QtWidgets.QLineEdit()
	# 	dbport_lineEdit.setPlaceholderText("Port d'accès")

	# 	hboxlayout.addWidget(dbname_lineEdit)
	# 	hboxlayout.addWidget(dbuser_lineEdit)
	# 	hboxlayout.addWidget(dbhost_lineEdit)
	# 	hboxlayout.addWidget(dbpassword_lineEdit)
	# 	hboxlayout.addWidget(dbport_lineEdit)



	# 	button_connexion = QtWidgets.QPushButton("Login")
	# 	hboxlayout.addWidget(button_connexion)

	# 	vbwidget = QtWidgets.QVBoxLayout()

	# 	# vbwidget.addWidget(hboxlayout)


	# 	self.widget_connexion.setLayout(hboxlayout)
		
	# 	self.widget_connexion.show()

	# 	dbname_lineEdit_value = dbname_lineEdit.text()
	# 	dbuser_lineEdit_value = dbname_lineEdit.text()
	# 	dbhost_lineEdit_value = dbname_lineEdit.text()
	# 	dbpassword_lineEdit_value = dbname_lineEdit.text()
	# 	dbport_lineEdit_value = dbname_lineEdit.text()

	# 	# button_connexion.clicked.connect(self.login_db_button_clicked(dbname_lineEdit_value, dbuser_lineEdit_value, dbhost_lineEdit_value, dbpassword_lineEdit_value,dbport_lineEdit_value))
	# 	# button_connexion.clicked.connect(self.widget_connexion.hide)






	# def login_db_button_clicked(self, dbname_lineEdit_value, dbuser_lineEdit_value, dbhost_lineEdit_value, dbpassword_lineEdit_value,dbport_lineEdit_value):
	# 	try:
	# 		mydb.connexion_database(dbname_lineEdit_value, dbuser_lineEdit_value, dbhost_lineEdit_value, dbpassword_lineEdit_value,dbport_lineEdit_value)
	# 		QtWidgets.QMessageBox.information(self, "Information sur la connexion", "La connexion s'est bien déroulée")


	# 	except:
	# 		print("La connexion n'a pas marché")
	# 		QtWidgets.QMessageBox.information(self,  "Information sur la connexion", "La connexion s'est pas bien déroulée")
		




if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	f = QtWidgets.QMainWindow()
	window = Window(f)
	f.show()

	sys.exit(app.exec_())



