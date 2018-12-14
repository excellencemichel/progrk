#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QLabel,
		QSlider,
		QWidget,

		)



class Window(QWidget):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Slider parti two "
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):

		self.slider = QSlider(Qt.Horizontal, self)
		self.slider.setGeometry(60,60,100,20) #Le premier point de coordonnées (24,120) donnent les coordonnées du placement du slider, Tant disque les dernier nombres donnes les dimensions du slider

		self.label = QLabel(self)
		self.label.setPixmap(QPixmap("icons/png/icon_python_001.png"))

		self.label.setGeometry(60,100, 150, 120)

		self.slider.valueChanged.connect(self.changedValue)
		# self.slider.valueChanged[int].connect(self.changedValue) #les deux font la même chose




		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)

		self.show()



	def changedValue(self, value):
		if value ==0:
			self.label.setPixmap(QPixmap("icons/png/icon_python_001.png"))


		elif value <50:
			self.label.setPixmap(QPixmap("icons/png/icon_java_004.png"))

		else:
			self.label.setPixmap(QPixmap("icons/png/icon_html_004.png"))




if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



