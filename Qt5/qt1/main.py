import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
#                              QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider)
from groupbox import Ui_GroupBox





class ShipHolderApplication(QGroupBox):
    def __init__(self, parent=None):
        super(ShipHolderApplication, self).__init__(parent)
        self.createWidgets()



    def createWidgets(self):
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = ShipHolderApplication()
    myapp.show()

    sys.exit(app.exec_())