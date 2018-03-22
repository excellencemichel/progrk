#! /usr/bin/python3
#-*-condig:utf-8-*-

from PyQt5 import QtWidgets, QtGui, QtCore



class MyTable(QtWidgets.QTableWidget):

	def __init__(self, r, c):
		"""
		Les paramètres f et e seront les ligne et les colones que la table aura
			-r (row) est le nombre de ligne
			-e est le nombre de colonne
		"""
		super().__init__(r, c)

		self.show()


class Sheet(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()



		self.form_widget = MyTable(7,10)
		self.setCentralWidget(self.form_widget)

		self.show()







if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)

	sheet = Sheet()

	sys.exit(app.exec_())