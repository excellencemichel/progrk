#! /usr/python

#-*-conding:utf-8-*-


from PyQt5.QtWidgets import ( 
				 QApplication, QMainWindow,
				  QPushButton, QToolTip,
				  QStatusBar


				   )



class Window(QMainWindow):


	def __init__(self):

		super().__init__()


		self.title = "QStatus Bar"

		self.top = 200
		self.left = 200
		self.width = 600
		self.height = 500


		self.init_win()
		self.show()


	def init_win(self):
		self.statusBar().showMessage("This is simple message status")

		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)









if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())
