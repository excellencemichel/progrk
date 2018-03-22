
#! /usr/bin/python3
#-*-condig:utf-8-*-


import sys
from PyQt5 import QtWidgets, QtGui, QtCore



class Window(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()



	def init_ui(self):
		self.le = QtWidgets.QLineEdit()
		self.b1 = QtWidgets.QPushButton("Clear")
		self.b2 = QtWidgets.QPushButton("Print")

		self.sl = QtWidgets.QSlider(QtCore.Qt.Horizontal)

		self.sl.setMinimum(1)
		self.sl.setMaximum(99)
		self.sl.setValue(25)
		self.sl.setTickInterval(10)
		self.sl.setTickPosition(QtWidgets.QSlider.TicksBelow)


		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.le)
		v_box.addWidget(self.sl)
		v_box.addWidget(self.b1)
		v_box.addWidget(self.b2)


		self.setLayout(v_box)
		self.setWindowTitle("Slider")

		self.b1.clicked.connect(lambda: self.btn_click(self.b1, "Hello from Clear"))
		self.b2.clicked.connect(lambda: self.btn_click(self.b2, "Hello from Print"))
		self.sl.valueChanged.connect(self.v_change)



		self.show()


	def btn_click(self, b, string):
		if b.text() == "Print":
			print(self.le.text())

		else:
			self.le.clear()
		print(string)



	def v_change(self):
		my_value = str(self.sl.value())
		self.le.setText(my_value)



app = QtWidgets.QApplication(sys.argv)

a_window = Window()

sys.exit(app.exec_())



