import sys
from PyQt5.QtWidgets import  *

app = QApplication(sys.argv)
mainWindow = QMainWindow()
QLabel("Boonjour le monde!",  mainWindow)

mainWindow.show()
app.exec_()
