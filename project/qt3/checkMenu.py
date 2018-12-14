#! /usr/python

#-*-conding:utf-8-*-

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
				 QApplication, QMainWindow,
                  QAction,
                  qApp,
                  QMenu,
                  

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


		self.statusbar = self.statusBar()

		self.statusbar.showMessage("Message is ready")


		menubar = self.menuBar()

		viewMenu = menubar.addMenu("View")

		viewAction = QAction("Veiw Status", self, checkable=True)
		viewAction.setStatusTip("View statusbar")
		viewAction.setChecked(True)
		viewAction.triggered.connect(self.toggleMenu)


		viewMenu.addAction(viewAction)



		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



	def toggleMenu(self, state):
		if state:
			self.statusbar.show()

		else:
			self.statusbar.hide()








if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())
