#! /usr/bin/python
#-*-coding: utf-8 -*-


from PyQt5 import QtWidgets
from fonctions import Calculatrice



def main(args):
	app = QtWidgets.QApplication(args)
	fenetre = QtWidgets.QWidget()
	calculatrice = Calculatrice(fenetre)
	fenetre.show()

	r = app.exec_()
	return r



if __name__ == '__main__':
	import sys
	main(sys.argv)