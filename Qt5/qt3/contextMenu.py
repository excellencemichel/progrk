#! /usr/bin/python
#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu



class Window(QMainWindow):

	def __init__(self):
		super().__init__()


		self.title = "Context Menu"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 500

		self.setWindowIcon(QtGui.QIcon("icons/icon_002.png"))

		self.init_win()



	def init_win(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.top,self.left, self.width, self.height)

		self.show()



	def contextMenuEvent(self, event):
		un_autre = QMenu(self) #Si on donne ça à la valeur de action, au clique du bouton droit rien ne va tout simplement se passer
		contextMenu = QMenu(self)
		newAct = contextMenu.addAction("New")
		openAct = contextMenu.addAction("Open")
		quitAct = contextMenu.addAction("Quit")

		action = contextMenu.exec_(self.mapToGlobal(event.pos())) #Capture le clique tu bouton droit

		if action == quitAct:
			self.close()




if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())