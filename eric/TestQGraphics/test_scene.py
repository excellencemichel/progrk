#-*- coding:utf-8 -*-

#Standard import



#Library import
from PyQt5.QtWidgets import (QMainWindow, QGraphicsScene,
				QGraphicsItem, QGraphicsView,
				QGraphicsEllipseItem, QColorDialog
				)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QBrush, QPainter, QPen


#locale import
from Ui_test_scene import Ui_MainWindow



#Content programme

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.scene = QGraphicsScene()
		self.remplirScene()
		self.show()
		for vue in (self.vuePrincipale, self.vueGlobale):
			vue.setScene(self.scene)
			vue.setRenderHints(QPainter.Antialiasing)
			vue.fitInView(self.rectGris, Qt.KeepAspectRatio)

		self.vueGlobale.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.vueGlobale.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.vuePrincipale.setDragMode(QGraphicsView.RubberBandDrag)

		self.angleVue = 0.0
		self.zoomPctVue = 1.0

		self.horizontalSliderZoom.setValue(100)
		self.lineEditTexte.setText("Tous en scène !")

		self.scene.selectionChanged.connect(
			self.onSceneSelectionChanged)
		self.onSceneSelectionChanged()



	def onSceneSelectionChanged(self):
		nbElementSelectionnes = len(self.scene.selectedItems())
		self.pushButtonChangerCouleur.setEnabled(nbElementSelectionnes > 0)
		msg = "%d éléments sélectionnés"%nbElementSelectionnes
		self.statusBar.showMessage(msg)


	def remplirScene(self):
		scene = self.scene
		rectGris = scene.addRect(0,0,200,150, brush=QBrush(Qt.lightGray))
		self.rectGris = rectGris
		self.texte = scene.addText("")
		dy = rectGris.rect().height()-self.texte.sceneBoundingRect().height()
		self.texte.setPos(rectGris.x(), rectGris.y()+dy)
		self.texte.setDefaultTextColor(Qt.cyan)
		scene.addItem(self.texte)
		diametre = 48 #Diametre de smiley
		ox = 4. #Largeur
		oy = 6. #hauteur
		smiley = scene.addEllipse(-diametre/2, -diametre/2, diametre, diametre, brush=QBrush(Qt.yellow))
		yeux = [QGraphicsEllipseItem(-ox/2., -oy/2., ox, oy, parent=smiley) for _ in range(2)]
		yeux[0].setPos(-diametre/6, -diametre/8)
		yeux[1].setPos(+diametre/6, -diametre/8)
		brush = QBrush(Qt.black)
		for oeil in yeux:
			oeil.setBrush(brush)


		smiley.setPos(rectGris.mapToScene(rectGris.rect().center()))
		smiley.setRotation(20)
		smiley.setScale(1.5)
		for item in scene.items():
			item.setFlag(QGraphicsItem.ItemIsMovable)
			item.setFlag(QGraphicsItem.ItemIsSelectable)



	@pyqtSlot()
	def on_pushButtonCreerDisque_clicked(self):
		disque = self.scene.addEllipse(0,0,20,20,brush=QBrush(Qt.white), pen=QPen(Qt.NoPen))
		disque.setFlag(QGraphicsItem.ItemIsMovable)
		disque.setFlag(QGraphicsItem.ItemIsSelectable)



	@pyqtSlot()
	def on_lineEditTexte_textChanged(self, msg):
		self.texte.setPlainText(msg)



	@pyqtSlot()
	def on_pushButtonChangerCouleur_clicked(self):
		itemsSelectionnes = self.scene.selectedItems()
		couleurInit = itemsSelectionnes[0].brush().color()
		couleur = QColorDialog.getColor(couleurInit, self, "Changer la couleur")
		if couleur.isValid():
			brosse = QBrush(couleur)
			for item in itemsSelectionnes:
				item.setBrush(brosse)



	@pyqtSlot(int)
	def on_dialRotation_valueChanged(self, nouvelAngleVue):
		self.vuePrincipale.rotate(nouvelAngleVue-self.angleVue)
		self.angleVue = nouvelAngleVue


	@pyqtSlot()
	def on_horizontalSliderZoom_valueChanged(self, nouvZoomPctVue):
		f = (nouvZoomPctVue/100.)/self.zoomPctVue
		self.vuePrincipale.scale(f,f)
		self.zoomPctVue = nouvZoomPctVue/100.