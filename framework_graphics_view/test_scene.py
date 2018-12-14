#-*- coding:utf-8 -*-

#Standard import 
import sys
from random import random

#Library import
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QBrush, QPen, QColor, QPainter

from PyQt5.QtWidgets import (QApplication, QGraphicsScene,
				 QGraphicsItem, QGraphicsView,
				  QGraphicsRectItem,QGraphicsTextItem,
				  QGraphicsEllipseItem
				 )



app = QApplication(sys.argv)
#Definition de la scène
scene = QGraphicsScene()

rectGris = QGraphicsRectItem(0., 0., 200.,150.)
rectGris.setBrush(QBrush(Qt.blue))
scene.addItem(rectGris)

texte = QGraphicsTextItem("Tous en Scène !")
dy = rectGris.sceneBoundingRect().height() - texte.sceneBoundingRect().height()
texte.setPos(rectGris.x(), rectGris.y()+dy)
texte.setDefaultTextColor(QColor("red"))
texte.setZValue(1)
scene.addItem(texte)

diametre = 48.
ox = 4. #largeur oeil
oy = 6. #hauteur oeil
smiley = QGraphicsEllipseItem(-diametre/2, -diametre/2, diametre,diametre)
smiley.setBrush(QBrush(Qt.yellow))

yeux = [QGraphicsEllipseItem(-ox/2., -oy/2., ox,oy, parent=smiley) for _ in range(2)]
yeux[0].setPos(-diametre/6, -diametre/8)
yeux[1].setPos(+diametre/6, -diametre/8)
brush = QBrush(Qt.black)
for oeil in yeux:
	oeil.setBrush(brush)
smiley.setPos(rectGris.mapToScene(rectGris.rect().center()))

smiley.setScale(1.5)
smiley.setRotation(20.)
smiley.setFlag(QGraphicsItem.ItemIsMovable)
scene.addItem(smiley)



#Définition de la vue
# vue = QGraphicsView(scene)
# vue.resize(800,600)
# vue.fitInView(rectGris, Qt.KeepAspectRatio)
# vue.setRenderHints(QPainter.Antialiasing)
# vue.show()

# vue2 = QGraphicsView(scene)
# vue2.setRenderHints(QPainter.Antialiasing)
# vue2.resize(300,400)
# vue2.rotate(-20)
# vue2.show()
vuesAux = []
for _ in range(4):
	vueAux = QGraphicsView(scene)
	vuesAux.append(vueAux)
	vueAux.setRenderHints(QPainter.Antialiasing)
	vueAux.resize(400,300)
	vueAux.rotate(360*random())
	vueAux.scale(4*random(), 4*random())
	vueAux.show()

sys.exit(app.exec_())