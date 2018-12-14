#! /usr/bin/python

#-*-coding:utf-8-*-



from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow, QSpinBox, QLabel, QVBoxLayout, QDoubleSpinBox



class Window(QMainWindow):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Window SpinBox"
		self.top = 100
		self.left = 100
		self.width = 300
		self.height = 200


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		vBoxLayout = QVBoxLayout()
		self.label = QLabel("Current value", self)

		self.label.move(60,60)
		vBoxLayout.addWidget(self.label)



		self.spinBox = QSpinBox(self)
		self.doubleSpinBox = QDoubleSpinBox(self)
		self.doubleSpinBox.move(60, 100)
		self.spinBox.move(60,30)

		self.spinBox.setMinimum(40)
		self.spinBox.setMaximum(77)
		self.doubleSpinBox.valueChanged.connect(self.valueChang)


		vBoxLayout.addWidget(self.spinBox)







		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()


	def valueChang(self):
		self.label.setText("Current value is " + str(self.doubleSpinBox.value())) #ça ne marche



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



