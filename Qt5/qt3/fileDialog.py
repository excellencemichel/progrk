#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QFileDialog,
		QPushButton,
		QTextEdit




		)



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 File Dialog"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		self.button = QPushButton("Open file", self)
		self.button.setGeometry(100,100,100,50)

		self.button.clicked.connect(self.openFileDialog)


		self.textEdit = QTextEdit(self)
		self.textEdit.setGeometry(100, 150, 400, 300)





		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()




	def openFileDialog(self):
		filename = QFileDialog.getOpenFileName(self, "Open File", "/home/michel")

		if filename[0]:
			f = open(filename[0], "r") #Les fichier à extension .txt sont lu sans problème
			with f:
				data = f.read()
				self.textEdit.setText(data)


if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



