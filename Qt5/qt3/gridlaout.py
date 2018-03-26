#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QGroupBox, QGridLayout, QPushButton, QVBoxLayout



class Window(QDialog):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Window Grid Layout"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)


		self.gridLayoutCreation()

		vBoxLayout = QVBoxLayout()

		vBoxLayout.addWidget(self.groupBox)

		self.setLayout(vBoxLayout)

		self.show()



	def gridLayoutCreation(self):
		self.groupBox = QGroupBox("Grid Layout Example")

		gridLayout = QGridLayout()

		# gridLayout.addWidget(QPushButton("0"), 0,0)
		gridLayout.addWidget(QPushButton("1"), 0,0)
		gridLayout.addWidget(QPushButton("2"), 0,1)
		gridLayout.addWidget(QPushButton("3"), 0,2)

		gridLayout.addWidget(QPushButton("4"), 1,0)
		gridLayout.addWidget(QPushButton("5"), 1,1)
		gridLayout.addWidget(QPushButton("6"), 1,2)

		gridLayout.addWidget(QPushButton("7"), 2,0)
		gridLayout.addWidget(QPushButton("8"), 2,1)
		gridLayout.addWidget(QPushButton("9"), 2,2)


		self.groupBox.setLayout(gridLayout)


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



