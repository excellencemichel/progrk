#! /usr/bin/python
# -*- coding: utf-8 -*-



from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QWidget,
		QPushButton,
		QFrame,
		QLabel,
		QHBoxLayout,
		QSizePolicy


		)



class Exemple(QWidget):
	def __init__(self):
		super().__init__()
		# self.resize(600, 500)

		self.initUi()


		# self.button = QPushButton("Hello", self)
		# ##Création d'un objet self.animate isu de QPropertyAnimation.
		# ##Nous passons en argument le widget qui sera à animer et la propriété que nous allons animer
		# self.animate = QtCore.QPropertyAnimation(self.button, "geometry")
		# ##Nous rentrons le délai de l'animation en ms
		# self.animate.setDuration(800)
		# ##Nous indiquons les propriétés de départ
		# self.animate.setStartValue(QtCore.QRect(0,0,100,30))
		# ##Puis les propriétés de fin
		# self.animate.setEndValue(QtCore.QRect(250,250,300,30))
		# ##Et enfin nous demarons l'animation
		# self.animate.start()


	def initUi(self):
		self.button = QPushButton("Start", self)
		self.button.clicked.connect(self.doAmin)
		self.button.move(30,30)


		self.frame = QFrame(self)
		self.frame.setFrameStyle(QFrame.Panel|QFrame.Raised)
		self.frame.setGeometry(150,30,100,100)


		self.setGeometry(300,300,380,300)
		self.setWindowTitle("Animation")
		self.show()



	def doAmin(self):
		self.anim = QPropertyAnimation(self.frame, b"geometry")
		self.anim.setDuration(1000)
		self.anim.setStartValue(QRect(150,30,100,100))
		self.anim.setEndValue(QRect(150,30,200,200))
		self.anim.start()










if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Exemple()


	sys.exit(app.exec_())