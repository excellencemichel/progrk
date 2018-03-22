#! /usr/bin/python3
#-*-coding:utf-8-*-


# import sys

import psycopg2


from PyQt5 import QtCore, QtGui, QtWidgets



#Local import 
from login import Ui_DialogLogin
from signup import Ui_DialogSignup

from wellcom import Ui_Wellcom
import mainSignup


class Login(QtWidgets.QDialog, Ui_DialogLogin):

	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self)

		self.setupUi(parent)



		################## "" Conexion des bouton """ ##################
		self.login_btn.clicked.connect(self.loginCkeck)

		self.signup_btn.clicked.connect(self.signupCheck)


	def hideWindow(self):
		SelfWindow = QtWidgets.QDialog()
		ui = Login(SelfWindow)
		SelfWindow.hide()

	def shwoMessageBox(self, title, message):
		msgBox = QtWidgets.QMessageBox()

		msgBox.setIcon(QtWidgets.QMessageBox.Warning)
		msgBox.setWindowTitle(title)
		msgBox.setText(message)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes)
		msgBox.exec_()


	def wellcomWindowShow(self):
		self.wellcomWindow = QtWidgets.QMainWindow()
		self.ui = Ui_Wellcom()
		self.ui.setupUi(self.wellcomWindow)

		self.wellcomWindow.show()



	def signupShow(self):
		self.signupWindow = QtWidgets.QDialog()
		self.ui = Ui_DialogSignup()

		self.ui.setupUi(self.signupWindow)

		self.hideWindow()

		self.signupWindow.show()




	def loginCkeck(self):
		print("Login Buton clicked !")

		username = self.username_lineEdit.text()

		password = self.password_lineEdit.text()


		try:
			connection_dbase = psycopg2.connect(
										"dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' "
									)

			cursor_dbase = connection_dbase.cursor()


		except:
			print("Cant connect on database")

		print(cursor_dbase)


		commend_select = (" SELECT * FROM users  WHERE username = '{}' AND password = '{}' ".format(username, password)) # A cause des griffe autour des clause données à WHERE on peut perdre du temps à recolter des erreurs
		# commend_select = "SELECT * FROM users WHERE username = " + username + " AND password = " + password + ""

		cursor_dbase.execute(commend_select)

		result = cursor_dbase.fetchall()

		if len(result)>0:
			print("User found !")

			self.wellcomWindowShow()

		else:
			print("User not found !")

			self.shwoMessageBox("Warning", "Invalid Username and Password")







	def signupCheck(self):
		print("Sign Up Buton clicked !")
		self.signupShow()




def main(args):

	app = QtWidgets.QApplication(args)

	Dialog = QtWidgets.QDialog()

	ui = Login(Dialog)

	Dialog.show()

	r = app.exec_()

	return r 




if __name__ == '__main__':
	import sys
	main(sys.argv)


