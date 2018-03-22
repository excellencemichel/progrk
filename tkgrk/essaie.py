"""
Le debut avec les interfaces graphiques en utilisant le la bibliothèque
Tkinter
"""

#Tout commence par l'import de Tkinter
from tkinter import *


#Création d'une fenre

fenetre = Tk()

#On  crée un label (ligne de texte)
#Le contructeur d'un label prend en 1er parametre la fenetre
#Et en deuxième lieu le texte dans le parametre nommé text

champ_label = Label(fenetre, text="Bonne et heureuse anné à vous !")

#On affiche le label dans la fenêtre
champ_label.pack()


#La création d'un bouton
bouton =Button(fenetre, text="Quitter", command=fenetre.quit)
bouton.pack()

#Ligne de saisie
var_texte = StringVar() #Pour une ligne
ligne_texte = Entry(fenetre, textvariable = var_texte, width=30)
ligne_texte.pack()
#On peut aussi faire pour multiligne
#champ_text = Text()


cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)

#Cela demarre la boucle Tkinter qui ne s'intérompt qu'à la
#la fermeture de la fenêtre
fenetre.mainloop()
