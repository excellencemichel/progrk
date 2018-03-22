import sys
import re
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  PyQt5.QtWidgets import *



#Données à représenter

my_array = [["00", "01", "02"],
            ["10", "11", "12"],
            ["20", "21", "22"]]




def main():

    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    sys.exit(app.exec_())



#Création de la vue et du conteneur

class MyWindow(QWidget):

    def __init__(self, *args):
        QWidget.__init__(self, *args)


        #Création du tableau
        self.get_table_data()
        table = self.createTable()



        # tablemodel = MyTableModel(my_array, self)
        # tableview = QTableView()
        # tableview.setModel(tablemodel)



        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)


    def get_table_data(self):
        # stdouterr = os.popen("dir /", "ab")[1].read()

        stdouterr = "jkzerifgieuifviguigerbuyreidguiberf hgei hgugf hgzerr"

        lines = stdouterr.splitlines()
        lines = lines[5:]
        lines = lines[:-2]
        self.tabledata = [repr().split(r"\s+", line, 4) for line in lines]



    def createTable(self):
        #Création de vue

        tv = QTableView()


        #Création du modèle
        header = ["date", "time", "", "size", "filename"]
        tm = MyTableModel(self.tabledata, header, self)

        tv.setModel(tm)

        #Rajout d'une taille minimale
        self.setMinimumSize(400,300)


        #Et suppression du quadrillage
        tv.setShowGrid(False)


        #Mise en place de la police
        font = QFont("courier New", 8)
        tv.setFont(font)



        #Suppression de l'en-tête vertivale
        vh = tv.verticalHeader()
        vh.setVisible(False)


        #Mise en place de l'en-tête horizontale
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)



        #redimentionnement de la largeur des colonnes
        tv.resizeColumnsToContents()

        #définition de la largeur des cellules
        nrows = len(self.tabledata)
        for row in range(nrows):
            tv.setRowHeight(row, 18)


        return tv









    #Création de modèle
class MyTableModel(QAbstractTableModel):
    def __init__(self, datain,headerdata, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata




    def rowCount(self, parent):
        return len(self.arraydata)


    def culumnCount(self, parent):
        return len(self.arraydata[2])




    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()

        return QVariant(self.arraydata[index.row()][index.column()])



    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata([col]))


        return QVariant()




if __name__ == "__main__":
    main()