#! /usr/python

#-*-conding:utf-8-*-


from PyQt5.QtWidgets import ( 
				 QApplication, QMainWindow,
				  QPushButton, QToolTip,
				   QLabel, QAction,
				   QMessageBox,


				   )


from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication


class Window(QMainWindow):

	def __init__(self):
		super().__init__()


		self.title= "PyQt5 PusButton"

		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 540

		self.setWindowIcon(QtGui.QIcon("icons/line.png"))

		button = QPushButton("Click for close", self)
		button.move(200,200)

		button.clicked.connect(self.closeApp)


		

		self.init_window()


	def init_window(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		


		self.show()



	def closeApp(self):
		reply = QMessageBox.question(self, "What do you want ? Close or what ?", "Are you sure to close window?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			self.close()



if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())