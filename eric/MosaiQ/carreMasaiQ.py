#-*-codng:utf-8 -*-

from random import randint

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import (QBrush, QPen,
						 QPainter, QColor,
						  QCursor
						  )
from PyQt5.QtWidgets import (QApplication,
							 QGraphicsView,
							 QGraphicsScene,
							  QGraphicsRectItem,
							  QFileDialog

							 )


#Paramètres de configuration 

#couleur du fond de la scène
COULEUR_FOND = "white"

#couleur utiliser pour le contour des carrés 
COULEUR_CONTOUR = (0,0,0)

#plage (min, max) pour les composants de RGB de la couleur des carrés
PLAGE_COULEURS = (50,250)

#pourcentage utilisé pour éclairer les carrés survolés
FACTEUR_ECLAIRCISSEMENT = 150

#Facteur de zoom
FACTUER_ZOOM_FIN = 1.02


#La classe proprement dite

class CarreMosaiQ(QGraphicsRectItem):
	_pen = QPen(QColor(*COULEUR_CONTOUR))
	_pen.setCosmetic(True)

	def __init__(self, x, y, c):
		QGraphicsRectItem.__init__(self, 0,0,c,c)
		self.setPos(x,y)
		self.setPen(CarreMosaiQ._pen)
		couleur = QColor(*(randint(*PLAGE_COULEURS) for _ in "RGB"))
		self.brush = QBrush(couleur)
		self.setBrush(self.brush)
		self.setCursor(Qt.OpenHandCursor)
		self.setAcceptHoverEvents(True)


	def hoverEnterEvent(self, event):
		couleur = self.brush.color().lighter(FACTEUR_ECLAIRCISSEMENT)
		self.setBrush(QBrush(couleur))



	def hoverLeaveEvent(self, event):
		self.setBrush(self.brush)



	def mousePressEvent(self, mouseEvent):
		if mouseEvent.button() == Qt.LeftButton:
			self.fragmente()
		else:
			QGraphicsRectItem.mousePressEvent(self, mouseEvent)
	def fragmente(self):
		c = self.rect().width()/2
		x = self.x()
		y = self.y()
		scene = self.scene()
		scene.removeItem(self)
		for (dx, dy) in ((0,0), (c,0), (0,c), (c,c)):
			scene.addItem(CarreMosaiQ(x+dx, y+dy, c))




class SceneMosaiQ(QGraphicsScene):
	def __init__(self):
		QGraphicsScene.__init__(self)
		size = 2.0**32
		self.CarreMosaiQUnivers = CarreMosaiQ(0,0,size)
		self.addItem(self.CarreMosaiQUnivers)



class VueMosaiQ(QGraphicsView):
	def __init__(self, scene):
		QGraphicsView.__init__(self, scene)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.setBackgroundBrush(QColor(COULEUR_FOND))
		self.setWindowTitle("MosaiQ en action")
		self.resize(800,600)
		self.fitInView(scene.CarreMosaiQUnivers, Qt.KeepAspectRatio)
		self.setTransformationAnchor(QGraphicsView.NoAnchor)

		self.hScrollBar = self.horizontalScrollBar()
		self.vScrollBar = self.verticalScrollBar()



	def wheelEvent(self, event):
		self.zoom(event.angleDelta().y()/100.0)

	def zoom(self, facteur):
		if facteur<0.0:
			facteur = -1.0/facteur
		posVue1 = self.mapFromGlobal(QCursor.pos())
		posScene = self.mapToScene(posVue1)
		self.scale(facteur, facteur)
		posVue2 = self.mapFromScene(posScene)
		dxVue = posVue2.x() - posVue1.x()
		dyVue = posVue2.y() - posVue1.y()
		self.hScrollBar.setValue(self.hScrollBar.value()+dxVue)
		self.vScrollBar.setValue(self.vScrollBar.value()+dyVue)


	def keyPressEvent(self, keyEvent):
		key = keyEvent.key()
		if key == Qt.Key_A:
			self.zoom(FACTUER_ZOOM_FIN)
		elif key == Qt.Key_Q:
			self.zoom(-FACTUER_ZOOM_FIN)

		elif key == Qt.Key_F11:
			self.showFullScreen()
		elif key == Qt.Key_Escape:
			self.showNormal()

		elif keyEvent.modifiers() == Qt.ControlModifier and Qt.Key_P:
			(nomfichier) = QFileDialog.getSaveFileName(self, "Sauvegarder l'image", filter="PNG(*.png);;JPEG(*.jpg);;BMP(*bmp)")
			if nomfichier:
				pixmap = self.grab()
				pixmap.save(nomfichier)
		else:
			QGraphicsView.keyPressEvent(self, keyEvent)



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	sceneMosaiQ = SceneMosaiQ()
	vueMosaiQ = VueMosaiQ(sceneMosaiQ)
	vueMosaiQ.show()
	sys.exit(app.exec_())