#! /usr/bin/python
#-*-coding: utf-8 -*-


from PyQt5 import QtWidgets, QtGui
from calculatrice import Ui_Calculatrice


class Calculatrice(QtWidgets.QWidget, Ui_Calculatrice):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(parent)
		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché

		self.pushButtonEgal.clicked.connect(self.on_pushButtonEgal_clicked)



	def on_pushButtonEgal_clicked(self):
		nb1 = self.spinBoxNombre1.value()
		nb2 = self.spinBoxNombre2.value()

		op = self.comboBoxOperation.currentText()

		if op == "+":
			self.labelResultat.setText(str(nb1+nb2))
		elif op == "-":
			self.labelResultat.setText(str(nb1-nb2))
		elif op == "*":
			self.labelResultat.setText(str(nb1*nb2))

		elif op == "/":
			self.labelResultat.setText(str(nb1/nb2))

		else:
			self.labelResultat.setText(self.trUtf8("Cette opération n'a pas été implementée dans la législation"))
			print("Cette opération n'a pas été prévu dans la législation")








if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	f = QtWidgets.QWidget()
	wind = Calculatrice(f)
	f.show()

	sys.exit(app.exec_())