#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtCore import QFileInfo
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QPushButton,
		QTextEdit,
		QFileDialog,

		)



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 PDF Exporter"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 530


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):

		self.button = QPushButton("Export PDF", self)
		self.button.setGeometry(100, 100, 100, 50)

		self.button.clicked.connect(self.printPDF)


		self.textEdit = QTextEdit(self)
		self.textEdit.setGeometry(100, 150, 400, 370)

		
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def printPDF(self):
		fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf) All Files ();")

		if fn !=" ":
			if QFileInfo(fn).suffix() == "" : fn += ".pdf"
			printer = QPrinter(QPrinter.HighResolution)
			printer.setOutputFormat(QPrinter.PdfFormat)
			printer.setOutputFileName(fn)
			self.textEdit.document().print_(printer)




if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



