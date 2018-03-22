#! /usr/bin/python3
#-*-condig:utf-8-*-


import sys
from PyQt5 import QtWidgets, QtGui, QtCore



class NotePad(QtWidgets.QWidget):


	def __init__(self):
		super(NotePad, self).__init__()

		self.text = QtWidgets.QTextEdit(self)
		self.clr_btn = QtWidgets.QPushButton("Clear")


		self.init_ui()



	def init_ui(self):
		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.text)
		layout.addWidget(self.clr_btn)

		self.clr_btn.clicked.connect(self.clear_text)

		self.setLayout(layout)
		self.setWindowTitle("Text edit model")


		self.show()


	def clear_text(self):
		self.text.clear()



app = QtWidgets.QApplication(sys.argv)

writter = NotePad()
sys.exit(app.exec_())
