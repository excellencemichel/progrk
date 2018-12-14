#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QMessageBox, QPushButton, QLineEdit



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Window Nice"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png"))

		self.init_window()



	def init_window(self):



		self.linedit = QLineEdit(self)
		self.linedit.move(200,200) #Placement
		self.linedit.resize(280,80)
		self.buton = QPushButton("Show text", self)
		self.buton.move(290, 290)

		self.buton.clicked.connect(self.onClick)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def onClick(self):
		textValue = self.linedit.text()
		QMessageBox.question(self, "Line Edit", "You have typed : {} ".format(textValue), QMessageBox.Ok, QMessageBox.Ok )



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



