#! /usr/python

#-*-conding:utf-8-*-


from PyQt5.QtWidgets import ( 
				 QApplication, QMainWindow,
				  QPushButton, QToolTip,
				   QLabel, QAction,


				   )

from PyQt5 import QtGui


class Window(QMainWindow):

	def __init__(self):
		super().__init__()


		self.title= "PyQt5 PusButton"

		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 540

		self.setWindowIcon(QtGui.QIcon("icons/line.png"))

		button1 = QPushButton("Click Me", self)
		# button1.move(200,200) #Si on ne précise pas d'enplacement l'élément se place à suite des éléments déjà existant comme les dive

		button2 = QPushButton("And Me", self)
		# button2.move(250, 250)

		button2.setToolTip("<h1>This is clic Button</h1>")

		label = QLabel("C'est un label", self)
		label.move(200, 300) #Si on fait pas le placelement tous les élément irrons se placer au coins superieurs gauche

		self.init_window()


	def init_window(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		


		self.show()




if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())