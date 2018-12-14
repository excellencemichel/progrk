#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
		QApplication,
		QMainWindow, QDialog,
		 QWidget, QVBoxLayout,
		 QLineEdit, QSlider,

		 )



class Window(QWidget):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Window QSlider Part one"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 200


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		vboxLayout = QVBoxLayout()
		self.lineEdit = QLineEdit(self)
		vboxLayout.addWidget(self.lineEdit)
		self.lineEdit.move(100, 50)


		self.slider = QSlider(Qt.Horizontal, self) #Par defaut les slider sorte en verticale
		self.slider.move(100, 20)
		self.slider.setMinimum(1)
		self.slider.setMaximum(99)
		self.slider.setValue(20) #Si on donne une veleur minimum >= à setValue cela ne marche pas setValue donne pas alors la valeur par défaut au slider
		self.slider.setTickPosition(QSlider.TicksBelow) #Les pointiers en bas
		vboxLayout.addWidget(self.slider)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



