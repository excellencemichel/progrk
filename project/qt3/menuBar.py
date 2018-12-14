#! /usr/python

#-*-conding:utf-8-*-

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
				 QApplication, QMainWindow,
                  QAction,
                  qApp,
                  

				   )



class Window(QMainWindow):


	def __init__(self):

		super().__init__()


		self.title = "Q menu bar"

		self.top = 200
		self.left = 200
		self.width = 600
		self.height = 500


		self.init_win()


	def init_win(self):

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		viewMenu = mainMenu.addMenu("Viw")
		editMenu = mainMenu.addMenu("Edit")
		searchMenu = mainMenu.addMenu("Search")
		toolMenu = mainMenu.addMenu("Tool")
		helpMenu = mainMenu.addMenu("Help")

		#Mettre ça ajoute les rentrées de menu sur la même ligne
		geekMenu = self.menuBar()

		runMenu = geekMenu.addMenu("Run")
		findMenu  = geekMenu.addMenu("Find")


		exitButton = QAction(QIcon("icons/icon_002.png"), "Exit", self)
		exitButton.setShortcut("Ctrl+Q")
		exitButton.setStatusTip("Exit application")

		exitButton.triggered.connect(self.close)
		fileMenu.addAction(exitButton)



		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)


		self.show()


	def close(self):
		qApp.quit()






if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())
