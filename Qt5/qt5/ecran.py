from PyQt5 import QtCore, QtGui, QtWidgets

class Frame(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.resize(600,500)
		size_ecran = QtWidgets.QDesktopWidget().screenGeometry()
		#Renvoie la tille de l'écran. Cette ligne nous permettra par la suite de connaître la hauteur et la largeur de l'écran.
		size_fenetre = self.geometry()
		#Même chose que ci-dessus mais avec la fenêtre de l'application.


		self.move((size_ecran.width() - size_fenetre.width())/2, (size_ecran.height()-size_fenetre.height())/2)
"""La fonction move() permet de déplacer la fenêtre aux coordonnées passées en arguments.
Dans le premier cas on centre horizontalement la fenêtre, puis verticalement.
Exemple : si l'écran fait 900 pixels de large, la fenêtre, 400, le calcul pour centrer la fenêtre est bien (900-400) / 2 soit 250.
Nous aurons donc 250 pixels d'espace, une fenêtre de 400 pixels, 250 pixels d'espace soit bien 900 pixels au total."""
 


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	frame = Frame()
	frame.show()
	sys.exit(app.exec_())