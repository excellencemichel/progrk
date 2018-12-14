#-*- coding:utf-8 -*-

#Standard import
import sys



#Library import
from PyQt5.QtWidgets import QApplication


#Locale import
from test_scene import MainWindow

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	mainwindow.show()
	sys.exit(app.exec_())