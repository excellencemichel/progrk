#! /usr/bin/python

#-*-coding:utf-8-*-

import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  QApplication, QMainWindow, QTableWidgetItem

#Local
from dataliste import Ui_Dataliste
from create_data_liste import Create




class ListeData(QMainWindow, Ui_Dataliste ):


	def __init__(self, parent=None):
		QMainWindow.__init__(self)


		self.setupUi(parent)


		self.btn_load.clicked.connect(self.loadData)



	def loadData(self):

		table = Create("liste")

		resultat = table.query_all(table.table_name)

		self.tableWidget.setRowCount(0)
		for row_number, row_data in enumerate(resultat):
			self.tableWidget.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))





def main(args):

	app = QApplication(args)

	f = QMainWindow()

	w = ListeData(f)

	f.show()

	r = app.exec_()
	return r 



if __name__ == '__main__':
	main(sys.argv)