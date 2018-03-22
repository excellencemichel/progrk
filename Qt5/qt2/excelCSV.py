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
			with open(path[0], newline="") as csv_file:
				self.setRowCount(0)
				self.setColumnCount(10)

				my_file = csv.reader(csv_file, dialect="excel") 
				for row_data in my_file:
					row = self.rowCount()

					self.insertRow(row)

					if len(row_data)> 10:
						self.setColumnCount(len(row_data))


					for column , stuff in enumerate(row_data):
						item = QtWidgets.QTableWidgetItem(stuff)
						self.setItem(row, column, item)



		self.check_change = True


	def save_sheet(self):
		path = QtWidgets.QFileDialog.getSaveFileName(self, "Save file csv", os.getenv("home")) #"CSV(*.csv)")

		if path[0] !="":
			with open(path[0], "w") as csv_file:
				writer = csv.writer(csv_file, dialect="excel")
				for row in range(self.rowCount()):
					row_data = []
					for column in range(self.columnCount()):
						item = self.item(row, column)
						if item is not None:
							row_data.append(item.text())

						else:
							row_data.append("")

					writer.writerow(row_data)
																




class Sheet(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()




		self.form_widget = MyTable(10,10)
		self.setCentralWidget(self.form_widget)
		col_header = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

		self.form_widget.setHorizontalHeaderLabels(col_header)


		#Set Menu

		bar = self.menuBar()

		file = bar.addMenu("File")


		save_action = QtWidgets.QAction("&Save", self)
		save_action.setShortcut("Ctr+S")


		open_action = QtWidgets.QAction("&Open", self)
		open_action.setShortcut("Ctr+N")

		quit_action = QtWidgets.QAction("&Quit", self)


		file.addAction(save_action)
		file.addAction(open_action)
		file.addAction(quit_action)


		quit_action.triggered.connect(self.quit_app)
		save_action.triggered.connect(self.form_widget.save_sheet)
		open_action.triggered.connect(self.form_widget.open_sheet)

		self.show()



	def quit_app(self):
		QtWidgets.qApp.quit()








if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)

	sheet = Sheet()

	sys.exit(app.exec_())