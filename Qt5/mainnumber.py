#! /usr/bin/python

#-*-coding:utf-8-*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from number import Ui_Number


class Number(QtWidgets.QMainWindow, Ui_Number):

	def __init__(self, parent=None):

		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(parent)




def main(args):
	app = QtWidgets.QApplication(args)

	f = QtWidgets.QMainWindow()

	w = Number(f)
	f.show() #Affiche la fenêtre qu'on a éditée
	w.show() #Afficher cette variable qui a l'instance de notre classe revient à afficher un QtWidgets.QMainWindow sans rien dedans

	r= app.exec_()
	return r




if __name__ == '__main__':
	main(sys.argv)