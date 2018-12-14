#-*- coding: utf-8-*-

from PyQt5.QtWidgets import  ( 
            QMainWindow,  QFileDialog,  
            QMessageBox
            )
from PyQt5.QtCore import pyqtSlot, QDate, QItemSelectionModel
#Locale import
from Ui_main_window_biblio import Ui_mainWindowBiblio

from modele_biblio import Livre,  ModeleTableBiblio

class MainWindowBiblio(QMainWindow,  Ui_mainWindowBiblio):
    def __init__(self,  parent=None):
        super(MainWindowBiblio,  self).__init__(parent)
        self.setupUi(self)
        
        livresTest = [      Livre("Une étude en rouge",  "Conan Doyle", "Hachette",  "Policier",
                            1887,  "Cela date de trop et moi je suis hostile à ce genre de situation", 11.
                            ), 
                            Livre("Le Horla",  "Guy de Maupassant",  "Gallimard", "Fantastique", 
                                    1887, "La même situation de date de merde",  11.), 
                            Livre("Napoléon",  "André Castelot",  "Perrin", "Biographie",  
                            2008,  "Un peut recent donc cela passe ce moi",  24.)
                    ]

    
        self.nomFichierBiblio = None

        self.modeleTableBiblio = ModeleTableBiblio([])
        self.treeViewLivres.setModel(self.modeleTableBiblio)
        self.treeViewLivres.selectionModel().selectionChanged.connect(
                self.on_treeViewLivres_selectionChanged)


        self.modificationAEnregistrer(False)
        self.dateEditParution.setMinimumDate(QDate(101,1,1)) 
        self.dateEditParution.setSpecialValueText(" ")

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

        self.dateEditParution.dateChanged.connect(
            self.declareSaisieEncours)

        self.textEditResume.textChanged.connect(
            self.declareSaisieEncours)

        self.doubleSpinBoxPrix.valueChanged.connect(
            self.declareSaisieEncours)


    def declareSaisieEncours(self):
        self.pushButtonNouveau.setEnabled(False)
        saisieValide = len(self.lineEditTitre.text().strip())>0
        self.pushButtonSauvegarder.setEnabled(saisieValide)

    def modificationAEnregistrer(self, fichierNonEnregistre):
        self.fichierNonEnregistre = fichierNonEnregistre
        titre = "BiblioApp"
        if self.nomFichierBiblio is not None:
            titre += "-" + self.nomFichierBiblio
        if fichierNonEnregistre:
            titre += "*"

        self.setWindowTitle(titre)

        self.actionEnregistrer.setEnabled(fichierNonEnregistre)

        self.pushButtonNouveau.setEnabled(True)
        self.pushButtonSauvegarder.setEnabled(False)


    
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
        self.dateEditParution.setDate(self.dateEditParution.minimumDate())
        self.textEditResume.setText("")
        self.doubleSpinBoxPrix.setValue(self.doubleSpinBoxPrix.minimum())
    
    
    def afficherLivre(self, livre):
        self.lineEditTitre.setText(livre.titre)
        self.lineEditAuteur.setText(livre.auteur)
        self.comboBoxGenre.setCurrentText(livre.genre)
        self.lineEditEditeur.setText(livre.editeur)
        self.dateEditParution.setDate(QDate(livre.annee,1,1))
        self.textEditResume.setText(livre.resume)
        self.doubleSpinBoxPrix.setValue(livre.prix)
    
    
    
    
    
    @pyqtSlot()
    def on_actionOuvrir_triggered(self):
        if self.fichierNonEnregistre:
            messageConfirmation = self.tr(""" Modification en cours \n "Etes-vous sur de vouloir continuer" sans enregistrer le fichier ? """)
            response = QMessageBox.question(self, self.tr("Confirmation"), messageConfirmation, QMessageBox.Yes, QMessageBox.No)
            if response == QMessageBox.No:
                return 

        (nomFichierBiblio,  filtre) = QFileDialog.getOpenFileName(
                self,  self.tr("Ouvrir le fichier bibliotheque"),  filter=self.tr("Bibliotheque(*.bib);; Tout(*.*)"))
        if nomFichierBiblio:
            self.modeleTableBiblio = ModeleTableBiblio.creeDepuisFichier(nomFichierBiblio)
            self.treeViewLivres.setModel(self.modeleTableBiblio)
            self.treeViewLivres.selectionModel().selectionChanged.connect(
                    self.on_treeViewLivres_selectionChanged
                )
            self.nomFichierBiblio = nomFichierBiblio
            self.modificationAEnregistrer(False)

    
    @pyqtSlot()
    def on_actionEnregistrer_triggered(self):

        if self.nomFichierBiblio is None:
            (nomFichierBiblio, filtre) = QFileDialog.getSaveFileName(self,
                 self.tr("Enregristrer fichier"), 
                 filter=self.tr("Bibliotheque(*.bib);; Tout (*.*)"))
            if nomFichierBiblio:
                self.nomFichierBiblio = nomFichierBiblio
        if self.nomFichierBiblio is not None:
            self.modeleTableBiblio.enregistreDansFichier(self.nomFichierBiblio)
            self.modificationAEnregistrer(False)



    @pyqtSlot()
    def on_pushButtonNouveau_clicked(self):
        self.treeViewLivres.selectionModel().clearSelection()
        self.effaceLivre()
        self.pushButtonSauvegarder.setEnabled(False)


    @pyqtSlot()
    def on_pushButtonSauvegarder_clicked(self):
        livre = Livre(titre=self.lineEditTitre.text(),
                auteur = self.lineEditAuteur.text(),
                editeur = self.lineEditEditeur.text(),
                genre = self.comboBoxGenre.currentText(),
                annee = self.dateEditParution.date().year(),
                resume = self.textEditResume.toPlainText(),
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
            self.modificationAEnregistrer(True)



    @pyqtSlot()
    def on_pushButtonSupprimer_clicked(self):
        selectionModel = self.treeViewLivres.selectionModel()
        indexesSelectionnes = selectionModel.selectedRows()
        if len(indexesSelectionnes)>0:
            indiceLivreSelectionne = indexesSelectionnes[0].row()
            self.modeleTableBiblio.supprimerLivre(indiceLivreSelectionne)
            self.modificationAEnregistrer(True)


    
    @pyqtSlot()
    def on_actionQuitter_triggered(self):
        self.close()
    
    def closeEvent(self,  event):
        if not self.fichierNonEnregistre:
            event.accept()
        else:

            messageConfirmation = self.tr("""
                    Etes-vous sur de vouloir quitter BiblioApp \n"Sans sauvegarder le fichier ?" """)

            response = QMessageBox.question(self,  self.tr("Confirmation"),  messageConfirmation, QMessageBox.Yes,  QMessageBox.No)
            if response == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

