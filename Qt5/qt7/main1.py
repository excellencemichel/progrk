#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


from calculatrice import *

def main(args):
	app = QtWidgets.QApplication(args)
	f = QtWidgets.QWidget()
	c = Ui_Calculatrice()
	c.setupUi(f)
	f.show()

	r = app.exec_()
	return r

if __name__ == '__main__':
	import sys
	main(sys.argv)
