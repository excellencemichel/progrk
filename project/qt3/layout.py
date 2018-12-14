#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox



class Window(QDialog):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Layouts "
		self.top = 100
		self.left = 100
		self.width = 300
		self.height = 100


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)

		self.horizontalLayout()

		vbox = QVBoxLayout()
		vbox.addWidget(self.groupbox)
		self.setLayout(vbox)
		self.show()


	def horizontalLayout(self):
		self.groupbox = QGroupBox("What is your favorite sports ?")
		hboxlayout = QHBoxLayout()

		button = QPushButton("Football", self)
		hboxlayout.addWidget(button)

		button1 = QPushButton("Cricket")
		hboxlayout.addWidget(button1)

		button2 = QPushButton("Tennis", self)
		hboxlayout.addWidget(button2)


		self.groupbox.setLayout(hboxlayout)

		button.clicked.connect(self.buttonConclick)
		button1.clicked.connect(self.button1Conclick)
		button2.clicked.connect(self.button2Conclick)



	def buttonConclick(self):
		QMessageBox.information(self, "Football", "Yes I like Football")


	def button1Conclick(self):
		QMessageBox.information(self, "Cricket", "Yes I like Cricket")



	def button2Conclick(self):
		QMessageBox.information(self, "Tennis", "Yes I like Tennis")


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



