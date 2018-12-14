#-*- coding: utf-8-*-

from PyQt5.QtWidgets import  ( 
            QMainWindow,  QFileDialog,  
            QMessageBox
            )
from PyQt5.QtCore import pyqtSlot, QDate, QItemSelectionModel
#Locale import
from Ui_main_window_biblioApp import Ui_main_window_biblioApp

from modele_biblio import Livre,  ModeleTableBiblio

class MainWindowBiblio(QMainWindow,  Ui_main_window_biblioApp):
    def __init__(self,  parent=None):
        super(MainWindowBiblio,  self).__init__(parent)
        self.setupUi(self)

        self.modeleTableBiblio = ModeleTableBiblio()
        self.comboBoxGenre.addItems(self.modeleTableBiblio.genres())
        self.treeViewLivres.setModel(self.modeleTableBiblio)
        self.treeViewLivres.selectionModel().selectionChanged.connect(
                self.on_treeViewLivres_selectionChanged)


        self.dateEditAnnee.setMinimumDate(QDate(101,1,1)) 
        self.dateEditAnnee.setSpecialValueText(" ")

        self.doubleSpinBoxPrix.setMinimum(-0.01)
        self.doubleSpinBoxPrix.setSpecialValueText(" ")

        self.effaceLivre()

        self.pushButtonSupprimer.setEnabled(False)

        self.pushButtonSauvegarder.setEnabled(False)


        for lineEdit in (self.lineEditTitre,
                        self.lineEditAuteur,
                        self.lineEditEditeur):
            lineEdit.textEdited.connect(self.declareSaisieEncours)
        self.comboBoxGenre.currentIndexChanged.connect(
                                self.declareSaisieEncours)

        self.dateEditAnnee.dateChanged.connect(
            self.declareSaisieEncours)

        self.plainTextEditResume.textChanged.connect(
            self.declareSaisieEncours)
        self.doubleSpinBoxPrix.valueChanged.connect(
            self.declareSaisieEncours)


    def declareSaisieEncours(self):
        self.pushButtonNouveau.setEnabled(False)
        saisieValide = len(self.lineEditTitre.text().strip())>0
        self.pushButtonSauvegarder.setEnabled(saisieValide)

    
    def on_treeViewLivres_selectionChanged(self,  selected,  deselected):
        indexesSelection = selected.indexes()
        if self.pushButtonSauvegarder.isEnabled():
            response = QMessageBox.question(self, self.tr("Confirmation"),
                     self.tr("Abandonner la saisie en cours ?"),
                      QMessageBox.Yes, QMessageBox.No)

            if response == QMessageBox.No:
                selectionModel = self.treeViewLivres.selectionModel()
                selectionModel.selectionChanged.disconnect(
                    self.on_treeViewLivres_selectionChanged)
                selectionModel.select(selected, QItemSelectionModel.Deselect)
                selectionModel.select(deselected, QItemSelectionModel.Select)
                selectionModel.selectionChanged.connect(
                    self.on_treeViewLivres_selectionChanged)
                return
        if len(indexesSelection)==0:
            self.effaceLivre()
            self.pushButtonSupprimer.setEnabled(False)

        else:
            self.indexSelection = indexesSelection[0]
            self.indiceLivreSelectionne = self.indexSelection.row()
            self.afficherLivre(self.modeleTableBiblio.livres[
                                self.indiceLivreSelectionne])
            self.pushButtonSupprimer.setEnabled(True)
            self.pushButtonNouveau.setEnabled(True)
            self.pushButtonSauvegarder.setEnabled(False)


    def effaceLivre(self):
        for lineEdit in (self.lineEditTitre,
                         self.lineEditAuteur,
                        self.lineEditEditeur):
            lineEdit.setText("")

        self.comboBoxGenre.setCurrentIndex(0)
        self.dateEditAnnee.setDate(self.dateEditAnnee.minimumDate())
        self.plainTextEditResume.setPlainText("")
        self.doubleSpinBoxPrix.setValue(self.doubleSpinBoxPrix.minimum())
    
    
    def afficherLivre(self, livre):
        self.lineEditTitre.setText(livre.titre)
        self.lineEditAuteur.setText(livre.auteur)
        self.comboBoxGenre.setCurrentText(livre.genre)
        self.lineEditEditeur.setText(livre.editeur)
        self.dateEditAnnee.setDate(QDate(livre.annee,1,1))
        self.plainTextEditResume.setPlainText(livre.resume)
        self.doubleSpinBoxPrix.setValue(livre.prix)
    



    @pyqtSlot()
    def on_pushButtonNouveau_clicked(self):
        self.treeViewLivres.selectionModel().clearSelection()
        self.effaceLivre()
        self.pushButtonSauvegarder.setEnabled(False)


    @pyqtSlot()
    def on_pushButtonSauvegarder_clicked(self):
        livre = Livre(idLivre = None,
                titre=self.lineEditTitre.text(),
                auteur = self.lineEditAuteur.text(),
                editeur = self.lineEditEditeur.text(),
                genre = self.comboBoxGenre.currentText(),
                annee = self.dateEditAnnee.date().year(),
                resume = self.plainTextEditResume.toPlainText(),
                prix = self.doubleSpinBoxPrix.value()
                 )

        selectionModel = self.treeViewLivres.selectionModel()
        indexesSelectionnes = selectionModel.selectedRows()
        if len(indexesSelectionnes) == 0:
            self.modeleTableBiblio.ajouterLivre(livre)
            self.on_pushButtonNouveau_clicked()

        else:
            indiceLivreSelectionne = indexesSelectionnes[0].row()
            self.modeleTableBiblio.remplaceLivre(indiceLivreSelectionne, livre)



    @pyqtSlot()
    def on_pushButtonSupprimer_clicked(self):
        selectionModel = self.treeViewLivres.selectionModel()
        indexesSelectionnes = selectionModel.selectedRows()
        if len(indexesSelectionnes)>0:
            indiceLivreSelectionne = indexesSelectionnes[0].row()
            self.modeleTableBiblio.supprimerLivre(indiceLivreSelectionne)


    
    @pyqtSlot()
    def on_actionQuitter_triggered(self):
        self.close()


