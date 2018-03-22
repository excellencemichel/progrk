#! /usr/bin/python
#-*-coding:utf-8 -*-

import sys, os

# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *




from calculatrice1 import *


def main(args):
	a= QApplication(args)

	f = QWidget()

	c = Ui_calculatrice()	

	c.setupUi(f)

	f.show()

	r = a.exec_()
	return r




if __name__ == "__main__":
	main(sys.argv) #<include <QApplication>

