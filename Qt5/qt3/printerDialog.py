#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtPrintSupport import (
	QPrintDialog,
	 QPrinter,
	 QPrintPreviewDialog,
	 )
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QPushButton,
		QTextEdit,

		)



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Window "
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):

		self.button = QPushButton("Print", self)

		self.button.setGeometry(100,100,100, 50)

		self.button.clicked.connect(self.createPrintDialog)

		self.button1 = QPushButton("Preview", self)
		self.button1.setGeometry(203, 100,100, 50)

		self.button1.clicked.connect(self.printPreviewDialog)



		self.textEdit = QTextEdit(self)
		self.textEdit.setGeometry(100, 150, 200, 200 )


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def createPrintDialog(self):
		printer = QPrinter(QPrinter.HighResolution)
		dialog = QPrintDialog(printer, self)

		if dialog.exec_() == QPrintDialog.Accepted:
			self.textEdit.print_(printer)



	def printPreviewDialog(self):
		printer = QPrinter(QPrinter.HighResolution)
		previewDialog = QPrintPreviewDialog(printer, self)
		previewDialog.paintRequested.connect(self.printPreview)
		previewDialog.exec_()



	def printPreview(self, printer):
		self.textEdit.print_(printer)




if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



