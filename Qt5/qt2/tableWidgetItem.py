#! /usr/bin/python3
#-*-condig:utf-8-*-

from PyQt5 import QtWidgets, QtGui, QtCore



class MyTable(QtWidgets.QTableWidget):

	def __init__(self, r, c):
		"""
		Les paramètres f et e seront les ligne et les colones que la table aura
			-f (row) est le nombre de ligne
			-e (column) est le nombre de colonne
		"""
		super().__init__(r, c)

		self.init_ui()


	def init_ui(self):

		self.cellChanged.connect(self.c_cureent)
		# self.cellChanged.connect(self.c_cureent)


		self.show()



	def c_cureent(self):
		row = self.currentRow()
		col = self.currentColumn()
		value = self.item(row, col)
		value = value.text()

		print("The current call is {} {}".format(row, col))
		print("In this cell we have {}".format(value))


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


		self.show()








if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)

	sheet = Sheet()

	sys.exit(app.exec_())