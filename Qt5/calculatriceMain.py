#! /usr/bin/python
#-*-coding:utf-8 -*-

import sys, os


from PyQt5.QtWidgets import *


from calculatrice1 import *


class calculatrice(QWidget, Ui_calculatrice):
	def __init__(self, parent=None):
		QWidget.__init__(self)
		# self.ui = Ui_calculatrice() #Parce que nous avons hérité maintenant de Ui_calculatrice
		self.setupUi(parent)


		#On peut maintenant personnaliser nos widgets si on veut
		#Réaliser les connexions supplémentaires entre signaux et slots

		# self.connect(self.pushButtonEgal,
		# 				SIGNAL("clicked()"),
		# 				self.calcul
		# 	)

		self.pushButtonEgal.clicked.connect(self.calcul)


	def calcul(self):
		nb1 = self.spinBoxNombre1.value()
		nb2 = self.spinBoxNombre2.value()
		opt = self.comboBoxOperation.currentText()

		if opt =="+":
			self.labelResultat.setText(str(nb1 + nb2))

		elif opt == "-":
			self.labelResultat.setText(str(nb1 - nb2))

		elif opt == "*":
			self.labelResultat.setText(str(nb1 * nb2))

		elif opt == "/":
			self.labelResultat.setText(str(nb1 / nb2))


		else:
			self.labelResultat.setText(self.trUtf8("Cette opération n'est pas implementée ! Merci de revoir"))




def main(args):
	a= QApplication(args)
	f=QWidget()
	c=calculatrice(f)

	f.show()

	r = a.exec_()
	return r



if __name__=="__main__":
	main(sys.argv)