#! /usr/python

#-*-conding:utf-8-*-


from PyQt5.QtWidgets import ( 
				 QApplication, QMainWindow,
				  QPushButton, QToolTip,
				   QLabel, QAction,


				   )


from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication


class Window(QMainWindow):

	def __init__(self):
		super().__init__()


		self.title= "PyQt5 PusButton"

		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 540

		self.setWindowIcon(QtGui.QIcon("icons/line.png"))

		button = QPushButton("Click for close", self)
		button.move(200,200)

		button.clicked.connect(self.close)


		label = QLabel("C'est un label", self)
		label.move(200, 230) #Si on fait pas le placelement tous les élément irrons se placer au coins superieurs gauche

		self.init_window()


	def init_window(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		


		self.show()



	def close(self):
		QCoreApplication.instance().quit()


if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())