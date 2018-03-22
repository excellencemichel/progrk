#! /user/bin/python3
#! coding : utf-8



"""

	Si newline='' n’est pas spécifié, les caractères de fin de ligne embarqués
	 dans des champs délimités par des guillemets ne seront pas interprétés correctement, 
	 et sur les plateformes qui utilisent \r\n comme marqueur de fin de ligne, un \r sera ajouté.
	  Vous devriez toujours spécifier sans crainte newline='', puisque le module csv gère lui-même 
	  les fins de lignes (universelles).


"""

import csv, os

from PyQt5 import QtWidgets, QtGui, QtCore



class MyTable(QtWidgets.QTableWidget):

	def __init__(self, r, c):
		"""
		Les paramètres f et e seront les ligne et les colones que la table aura
			-f (row) est le nombre de ligne
			-e (column) est le nombre de colonne
		"""
		super().__init__(r, c)

		self.check_change = True

		self.init_ui()


	def init_ui(self):

		self.cellChanged.connect(self.c_cureent)
		# self.cellChanged.connect(self.c_cureent)


		self.show()



	def c_cureent(self):
		if self.check_change:
			row = self.currentRow()
			col = self.currentColumn()
			value = self.item(row, col)
			value = value.text()

			print("The current call is {} {}".format(row, col))
			print("In this cell we have {}".format(value))


	def open_sheet(self):
		self.check_change = False
		path = QtWidgets.QFileDialog.getOpenFileName(self, "Open csv", os.getenv("home"), "CSV(*.csv)")

		if path[0] != "":
			with open(path[0], "r", newline="") as csv_file: #L'argument newline n'est pas obligatoir pour la lecture de fichier d'extention csv et donc ici les données sont séparés par des virgules
				self.setRowCount(0)
				self.setColumnCount(10)

				my_file = csv.reader(csv_file, delimiter=',',quotechar='|') #Les deux arguments delimiter et quotechar
				# ne sont pas nécéssaire pour la lecture du fichier d'extention .csv
				#parce delimiter a une valeur par défaut qui est ',' et vu que les données ici sont séparées par des
				#virgules donc ça marche sans soucis et delimiter doit être d'un caractère seulement
				for row_data in my_file:
					row = self.rowCount()

					self.insertRow(row)

					if len(row_data)> 10:
						self.setColumnCount(len(row_data))


					for column , stuff in enumerate(row_data):
						item = QtWidgets.QTableWidgetItem(stuff)
						self.setItem(row, column, item)



		self.check_change = True




class Sheet(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()


		self.form_widget = MyTable(7,10)
		self.setCentralWidget(self.form_widget)

		col_insert = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
		self.form_widget.setHorizontalHeaderLabels(col_insert)

		number = QtWidgets.QTableWidgetItem("10") #L'argument doit être en str pour que ça s'affiche dans le cellule
		self.form_widget.setCurrentCell(1,1) #Permet de donner initialement le focus à la cellule 1,1
		self.form_widget.setItem(1, 1, number) #On donne la valeur stocker dans la variable number à la cellule

		self.form_widget.open_sheet()


		self.show()








if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)

	sheet = Sheet()

	sys.exit(app.exec_())