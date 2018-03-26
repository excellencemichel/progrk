#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, qApp



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Tooars"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QIcon("icons/line.png")) #ça na pas marché

		self.init_window()



	def init_window(self):

		exitAct = QAction(QIcon("icons/png/icon_003.png"), "Exit", self)
		exitAct.setShortcut("Ctrl+Q")


		openAct = QAction(QIcon("icons/png/icon_007.png"), "Open", self)
		openAct.setShortcut("Ctrl+O")

		copyAct = QAction(QIcon("icons/png/icon_008.png"), "Copy", self)
		copyAct.setShortcut("Ctrl+C")

		pasteAct = QAction(QIcon("icons/png/icon_004.png"), "Paste", self)
		pasteAct.setShortcut("Ctrl+V")

		deteleAct = QAction(QIcon("icons/png/icon_005.png"), "Delete", self)
		deteleAct.setShortcut("Ctrl+D")

		saveAct = QAction(QIcon("icons/png/icon_002.png"), "Save", self)
		saveAct.setShortcut("Ctrl+S")

		self.toobar = self.addToolBar("Toobar")

		self.toobar.addAction(exitAct)
		self.toobar.addAction(openAct)
		self.toobar.addAction(copyAct)
		self.toobar.addAction(pasteAct)
		self.toobar.addAction(deteleAct)
		self.toobar.addAction(saveAct)



		# exitAct.triggered.connect(qApp.exit) #Si tu as trop de la flemme ça peut aussi fermer la fennêtre
		# exitAct.triggered.connect(self.close) #Idem que ça aussi
		# exitAct.triggered.connect(self.closeApp)






		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def closeApp(self):
		qApp.exit()



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



