#! /usr/bin/python

#-*-coding:utf-8 -*-

"""
Apprentissage de la bibliateque PyQt
version 5
A la version la classe QMainWindow n'est pas de QtGui mais de QtWidgets


"""

import sys
from PyQt5 import QtGui, QtCore

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog


from mainwindow import Ui_MainWindow




class TextEditor(QMainWindow):
    def __init__(self, title="Default", parent=None):
        """
        On redéfinit ici le constructeur de la QMainWindow
        Pour lui assigner ce qu'on veut faire de cette classe
        en plus de cd qu'il fait

        """
        super(TextEditor, self).__init__(parent)
        self.title = title
        self.ui = Ui_MainWindow() #Instanciation de la classe qui nous avons créé dans le fichier mainwindow.py
        self.ui.setupUi(self)#lancement de sa fonction d'exécusion sur un objet de cette classe
        self.setWindowTitle(self.title)

        self._initSlotButtons()#Cela permet de lancer la fonction à partir de l'initiation des objets de la classe
        self.isFileOpne = False #Pour la verification de l'ouverture des fichiers
        self.isFileCreate = False


    def _initSlotButtons(self):
        self.ui.text.hide()
        self.ui.actiondossier.triggered.connect(self.openFile) #Selection de la variable liée au bouton, triggered fait le déclenchement
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionNewFile.triggered.connect(self.newFile)
        self.ui.actioncancel.triggered.connect(self.closeFile)


    def openFile(self):
        """
        Fonction pour ouvrir les fichier
        On utilise la la classe QFileDialog avec sa methode getOpenFileName
        Pour ouvrir le fichier, voici la définition de ses arguments
        parent: C'est la classe qui utilise la methode, ici notre classe elle même c'est pourquoi nous mettons self
        caption : La phrase qui s'affichera dans l'ouverture du fichier, Ici on se contente de dire Ouvrier un fichier
        directory: Le dossier dans lequel on se situera quand on veux ouvrir le fichier dans l'alborescence, Ici on va se situer directement dans le dossier home de l'alborescence(Spécialement pour linux)
        filter : Nous permet d'exclure ou d'inclure des types de fichiers en fonction de leur extentions, Ici on veut seulement que des fichier en extention .jpeg .png .pdf. Il faut noter que le * devant l'extention est nécéssaire
        option: pas trop d'inportance mais it's comming
        :return:
        """
        print("Ouverture d'un dossier pour choisir un fichier")
        # self.filename = QtWidgets.QFileDialog.getOpenFileName(parent=None, caption="", directory="", filter="", options=0)

        # options = QFileDialog.options()
        self.filename, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier") #La variable contient un tuple mais c'est la première valeur seulement qui est le fichier
        print(type(self.filename[0]))
        print(self.filename)
        # QtWidgets.QFileDialog
        #Il faut maintenant vérifier qu'un fichier a bien été choisi parce qu'il peut arriver que l'utilisateur ne choisi pas de fichier oubien il ferme la fenêtre de dialogue sans rien choisir
        if self.filename != "":#Le le fichier n'est pas vide
            self.isFileOpne = True #On crée une variable la donne la valeur True si un fichier a été choisi
            # self.file = open(self.filename[0], "rb") #On ouvre seulement le fichier en mode lecture
            # self.setWindowTitle(self.title + " - " + str( self.filename[0]))
            # self.ui.text.show()
            # file_text = self.file.read()
            # self.ui.text.setText(file_text)
            # self.file.close()

            with open(self.filename, 'rb') as f:
                self.setWindowTitle(self.title + " - " + str(f))
                self.ui.text.show()
                self.ui.text.setHtml(str(f.read()))



    def saveFile(self):
        import time

        if self.isFileCreate ==False or self.isFileOpne ==False:
            print("Aucun fichier n'a encore été ouvert")
            pass

        if self.isFileOpne == True:
            # self.isFileCreate = True
            with open(self.filename, "w") as f:
                f.write(self.ui.text.toHtml())

            self.ui.statusBar.showMessage(
                self.parseFileName() + " a bien été enregistré à la date du " + time.strftime("%d/%m/%y %H; %M",
                                                                                          time.localtime()), 3600)




        elif self.isFileCreate == True:
            # self.isFileOpne ==True

            # options = QFileDialog.options()
            self.filename = QFileDialog.getSaveFileName(self, "Sauvegarder le fichier", "nouvea fichier" )
            print(type(self.filename))
            print(self.filename)
            vide =('', '')

            if self.filename !="" and self.filename !=vide:
                with open(self.filename[0], "w") as f:
                    f.write(self.ui.text.toHtml())

                self.ui.statusBar.showMessage(
            self.parseFileName() + " a bien été enregistré à la date du " + time.strftime("%d/%m/%y %H; %M",
                                                                                      time.localtime()), 3600)


        else:
            pass





    def newFile(self):
        self.isFileCreate = True
        self.closeFile()

        self.ui.text.show()


    def closeFile(self):
        if self.ui.text.toHtml() == "" or self.ui.text.toPlainText() == "":
            pass

        else:
            reply = QMessageBox.question(self, "Attention !", "Êtes-vous sûr de vouloir fermer le fichier ouvert ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.ui.text.clear()
                self.ui.text.hide()
                self.setWindowTitle(self.title)
                self.isFileCreate = False
                self.isFileOpne = False

            else:
                pass




    def parseFileName(self):
        filename = str(self.filename)
        filename = filename.split("/")
        self.fName = filename[-1]

        return self.fName

if __name__ =="__main__":
    app = QApplication(sys.argv)

    w  = TextEditor("TextEditor  V1") #Intentiation de la classe qui a lancé le setup de GUI
    w.show()
    sys.exit(app.exec_())
