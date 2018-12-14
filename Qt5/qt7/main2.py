#! /usr/bin/python
#-*-coding:utf-8-*-

from PyQt5 import QtCore, QtGui, QtWidgets
from calculatrice import *



class calculatrice(QtWidgets.QWidget):
	"""docstring for calculatrice"""
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self)
		self.ui = Ui_Calculatrice()
		self.ui.setupUi(parent)
		self.ui.pushButtonEgal.setText("Egal")




def main(args):
	app = QtWidgets.QApplication(args)
	f = QtWidgets.QWidget()
	c = calculatrice(f)
	f.show()

	r = app.exec_()
	return r


if __name__ == '__main__':
	import sys
	main(sys.argv)