#! /usr/bin/pyhon
#-*-coding:utf-8-*-


import sys

from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QApplication, QMainWindow

from other1 import Ui_Other1
from other2 import Ui_otherwindow



class FirstWindow(QMainWindow, Ui_Other1):


	def __init__(self, parent=None):

		QMainWindow.__init__(self)

		self.setupUi(parent)


		self.btn_open.clicked.connect(self.openWindow)



	def openWindow(self):
		self.window = QMainWindow()
		self.ui = Ui_otherwindow()
		self.ui.setupUi(self.window)
		# self.hide()
		self.window.show()









def main(agrs):

	app = QApplication(agrs)

	f = QMainWindow()

	w = FirstWindow(f)

	f.show()
	r = app.exec_()

	return r 



if __name__ == '__main__':
	main(sys.argv)



