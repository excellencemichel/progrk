#! /usr/bin/python3
#-*-condig:utf-8-*-

import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore



class NotePad(QtWidgets.QWidget):


	def __init__(self):
		super(NotePad, self).__init__()

		self.isOpen = False
		self.isCreate = False

		self.text = QtWidgets.QTextEdit(self)
		self.clr_btn = QtWidgets.QPushButton("Clear")
		self.save_btn = QtWidgets.QPushButton("Save")
		self.open_btn = QtWidgets.QPushButton("Open")


		self.init_ui()



	def init_ui(self):
		v_layout = QtWidgets.QVBoxLayout()
		h_layout = QtWidgets.QHBoxLayout()


		h_layout.addWidget(self.clr_btn)
		h_layout.addWidget(self.save_btn)
		h_layout.addWidget(self.open_btn)


		v_layout.addWidget(self.text)
		v_layout.addLayout(h_layout)
		


		self.save_btn.clicked.connect(self.save_text)
		self.clr_btn.clicked.connect(self.clear_text)
		self.open_btn.clicked.connect(self.open_text)


		self.setLayout(v_layout)
		self.setWindowTitle("Text edit model")


		self.show()


	def save_text(self):
		filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", os.getenv("home"))
		with open(filename[0], "w") as f:
			my_text = self.text.toPlainText()
			f.write(my_text)


	def clear_text(self):
		self.text.clear()

	def open_text(self):
		filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", os.getenv("Home"))
		with open(filename[0], "r") as f:
			file_text = f.read()
			self.text.setText(file_text)


app = QtWidgets.QApplication(sys.argv)

writter = NotePad()
sys.exit(app.exec_())
