"""
Dans les classe avec PyQt5 
Une clase cette façon :

		class Window(QMainWindow, Ui_MainWindow):
			"""

			"""
			def __init__(self, parent=None):
				QMainWindow.__init__(self)
				# super().__init__() # Appel du constructeur de la classe QMainWindow

				self.setupUi(parent)
				parent.setWindowIcon(QtGui.QIcon("icons/line.png"))

	les attributions passe par parents parce que c'est elle qui represente la classe qui détient le graphique

Dans la classe mère comme :

		class Ui_MainWindow(object):
  		  def setupUi(self, MainWindow):
  	les attributions passent par MainWindow qui est encore ici le parametre de setupUi qui est en quelque sorte l'initiateur le contructeur





"""