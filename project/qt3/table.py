#! /usr/bin/python

#-*-coding:utf-8-*-


from PyQt5 import QtGui
from PyQt5.QtWidgets import ( 
		QApplication,
		QMainWindow,
		QWidget,
		QTableWidget,
		QTableWidgetItem,
		QVBoxLayout,
		)



class Window(QWidget):
	"""
	Cette classe nous montre qu'on peut soi-même faire les
	dimensions de la fenêtre à la main
	"""
	def __init__(self):
		super().__init__() # Appel du constructeur de la classe QMainWindow

		self.title = "PyQt5 Table"
		self.top = 100
		self.left = 100
		self.width = 500
		self.height = 400


		self.setWindowIcon(QtGui.QIcon("icons/line.png")) #ça na pas marché


		self.init_window()



	def init_window(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)

		self.creatingTables()

		self.vBoxLayout = QVBoxLayout() #Cet appel de la fonction rend disponible la qui la contient c'est pourquoi on peut acceder à la variable tableWidget
		self.vBoxLayout.addWidget(self.tableWidget) #Ici on donne la variable à la disposition verticale

		self.setLayout(self.vBoxLayout) #Il faut noter que si on ne donne pas cette disposition à l'objet rien ne se passe


		self.show()



	def creatingTables(self):
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(7)
		self.tableWidget.setColumnCount(3)


		self.tableWidget.setItem(0,0, QTableWidgetItem("Name")) #le point de (0,0) donne les coordonnées dans le tableau
		self.tableWidget.setItem(0,1, QTableWidgetItem("Email"))
		self.tableWidget.setItem(0,2, QTableWidgetItem("Phone No"))


		self.tableWidget.setItem(1,0, QTableWidgetItem("Michel"))
		self.tableWidget.setItem(1,1, QTableWidgetItem("bnvnmmnl@gmail.com"))
		self.tableWidget.setItem(1,2, QTableWidgetItem("669443344"))
		self.tableWidget.setColumnWidth(1, 200) #Permet d'agrandir la largeur de la colone

		self.tableWidget.setItem(2,0, QTableWidgetItem("Excellence"))
		self.tableWidget.setItem(2,1, QTableWidgetItem("nyambalamou@gmail.com"))
		self.tableWidget.setItem(2,2, QTableWidgetItem("0681282885"))


		self.tableWidget.setItem(3,0, QTableWidgetItem("Saint Michel"))
		self.tableWidget.setItem(3,1, QTableWidgetItem("michel3124077@gmail.com"))
		self.tableWidget.setItem(3,2, QTableWidgetItem("664254887"))


		self.tableWidget.setItem(4,0, QTableWidgetItem("Saint Jean"))
		self.tableWidget.setItem(4,1, QTableWidgetItem("jean@gmail.com"))
		self.tableWidget.setItem(4,2, QTableWidgetItem("664254887"))


		self.tableWidget.setItem(5,0, QTableWidgetItem("Saint Pierre"))
		self.tableWidget.setItem(5,1, QTableWidgetItem("pierre@gmail.com"))
		self.tableWidget.setItem(5,2, QTableWidgetItem("664254887"))





if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	window = Window()

	sys.exit(app.exec_())



