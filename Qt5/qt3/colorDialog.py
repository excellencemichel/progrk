#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QFontDialog,
		QPushButton,
		QTextEdit,
		QColorDialog,

		)



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Font Dialog"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		self.button = QPushButton("Open Font Dialog", self)
		self.button.setGeometry(100,100,130,30)

		self.button.clicked.connect(self.createFontDialog)

		self.button1 = QPushButton("Open color Dialog", self)
		self.button1.setGeometry(233,100, 130, 30)

		self.button1.clicked.connect(self.createColorDialog)


		self.textEdit = QTextEdit(self)
		self.textEdit.setGeometry(100, 150, 200, 200)



		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()


	def createFontDialog(self):
		font, ok = QFontDialog.getFont()

		if ok:
			self.textEdit.setFont(font)



	def createColorDialog(self):
		color = QColorDialog.getColor()

		self.textEdit.setTextColor(color)



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



