#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtWidgets, QtGui



class Window(QtWidgets.QMainWindow):
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


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		button = QtWidgets.QPushButton("Click Me", self)
		button.move(200,200)

		#Appel de la fonction pour qu'à l'instanciation de la classe
		#lorsque le contrusteur init l'objet la fonction soit appelée

		self.init_window()



	def init_window(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



