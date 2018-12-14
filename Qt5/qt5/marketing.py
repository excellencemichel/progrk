#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
from PyQt5 import QtCore, QtGui, QtWidgets


##Création de la fenêtre principale.
class Frame(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.resize(600, 500)
		size_ecran = QtWidgets.QDesktopWidget().screenGeometry()
		size_fenetre = self.geometry()







if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	## Création d'un widget QPixmap qui permet d'accéder à l'image img.JPG
	pixmap = QtGui.QPixmap("michel.jpg")
	# import pdb; pdb.set_trace()

	##Création de la page d'acceuil.
	splash = QtWidgets.QSplashScreen(pixmap)
	# splash.setMask(pixmap.mask())
	splash.show()
	app.processEvents()
	##Ici, je fige volontairement le code pour que nous puissions bien voir la page d'acceuil.
	time.sleep(5)
	frame = Frame()
	frame.show()
	splash.finish(frame)
	sys.exit(app.exec_())


