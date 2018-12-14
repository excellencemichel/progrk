#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow, QCheckBox, QLabel



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Window CheckBox"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		checkBox = QCheckBox("Do you like football ?", self)
		checkBox.move(100,100)
		checkBox.toggle() #Permet de croché la case par defaut

		self.label = QLabel("Result:", self)
		self.label.move(120, 150)

		checkBox.stateChanged.connect(self.checkBoxChange)



		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()


	def checkBoxChange(self, state):
		if state == Qt.Checked:
			self.label.setText("Yes I like football")

		else:
			self.label.setText("No I didn't like football")




if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



