#! /usr/bin/python3
#-*-condig:utf-8-*-


import sys
from PyQt5 import QtWidgets, QtGui



def window():
	"""
	A remarquer que si le widget ne contient rien
	il a une taille par défaut un peu grande
	Mais si on introduit des éléments à l'interieur
	du widget, le widget se reduit ou s'agradit en fonction
	de son contenu ce quand on a pas encore utilisé la fonction setGeometry
	"""
	app = QtWidgets.QApplication(sys.argv) #Le systeme qui va gérer l'interaction de la fenetre apres le systeme d'esploitaion
	w = QtWidgets.QWidget() #Crétion d'in widget simple

	#Un peut devant on donne un titre à l'interface qui va s'afficher
	w.setWindowTitle("A Hello World à la famille")

	l1 = QtWidgets.QLabel(w) #Il faut noter quand on cré un widget enfant qu'on veut
	#donner à un widget prent il faut mettre le widget parent en argument de la création du widget enfant
	#Maintant ici le widget a des enfant la taille du widget se conforme à sont contenu
	l1.setText("C'est pour vous faire un coucou !")
	l1.move(30,30) #Mise en place de l'élément dans son parent

	l2 = QtWidgets.QLabel(w)
	l2.setPixmap(QtGui.QPixmap("icon_001.eps"))
	l2.setPixmap(QtGui.QPixmap("icon_003.png"))

	l2.move(30, 40)

	w.setGeometry(100,100,200,200) #Les dimension de de la fenêtre

	h_box = QtWidgets.QHBoxLayout()
	h_box.addStretch()
	h_box.addWidget(l1)
	h_box.addStretch()

	v_box = QtWidgets.QVBoxLayout() #La création d'un laout vertical
	v_box.addWidget(l1) #Incsertion des element dans le loyout
	v_box.addWidget(l2) #Insertion encore

	v_box.addLayout(h_box)
	w.setLayout(v_box) #Ici on insert le loyout vertical dans le laout principale de la fenêtre



	w.show() # Ici on affiche le widget

	sys.exit(app.exec_())






window()