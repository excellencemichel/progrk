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

		button = QPushButton("About Box", self)
		button.move(200,200)

		button1 = QPushButton("Message de Question",self)
		button1.move(100, 150)

		button.clicked.connect(self.aboutApp)
		button1.clicked.connect(self.quitionmessage)


		

		self.init_window()


	def init_window(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		


		self.show()



	def aboutApp(self):
		QMessageBox.about(self, "About Message", "This is about Message Box")




	def quitionmessage(self):

		message = QMessageBox.question(self, "Question Message", "Cest le contenu comme ça", QMessageBox.Yes| QMessageBox.No, QMessageBox.No)

		if message == QMessageBox.Yes:
			print("Yes you are into my clomb")

		else:
			print("You aren't ")















if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())