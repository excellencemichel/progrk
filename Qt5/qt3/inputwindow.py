#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QWidget,
		QInputDialog,
		QLabel,
		QPushButton,
		QVBoxLayout,
		)



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Input Dialogs"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		self.button = QPushButton("Open Dialog", self)
		self.button.move(100,100)
		self.button.clicked.connect(self.createInpuntDialog)


		self.label = QLabel("Hello", self)

		# self.label.move(100,130) #A même effet que setGeometry
		self.label.setGeometry(100, 150, 300, 50)
	
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def createInpuntDialog(self):
		text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your Name")

		if ok:
			if " " in text:
				self.label.setText(str(text + " il y a espace"))

			else:
				self.label.setText(str(text)) 






if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



