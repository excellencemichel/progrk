#! /usr/bin/python3
#-*-coding:utf-8-*-


# import sys
import psycopg2


from PyQt5 import QtCore, QtGui, QtWidgets


#Local import 
from signup import Ui_DialogSignup



class Signup(QtWidgets.QDialog, Ui_DialogSignup):

	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(parent)



		self.signup_btn.clicked.connect(self.insert_data)



	def insert_data(self):
	    username = self.username_lineEdit.text()
	    email    = self.email_lineEdit.text()
	    password = self.password_lineEdit.text()

	    try:
	        connection_dbase = psycopg2.connect(
	                        "dbname = 'formation' user = 'michel' host = 'localhost' password = 'SaintMichel' port ='5432' "
	                         )
	        connection_dbase.autocommit = True
	        cursor_dbase = connection_dbase.cursor()


	    except:
	        print("Can connect to data base")


	    insert_command = ("INSERT INTO users(username, email, password) VALUES('{}', '{}', '{}')".format(username, email, password))

	    cursor_dbase.execute(insert_command)




def main(arg):
	app = QtWidgets.QApplication(arg)

	Dialog = QtWidgets.QDialog()

	ui = Signup(Dialog)

	Dialog.show()

	r = app.exec_()
	return r



if __name__ == '__main__':
	import sys
	main(sys.argv)