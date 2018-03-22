from os import *

from PIL import Image, ImageTk
import  PIL.Image
from tkinter import *

"""
Les canvas sont des zones rectangulaires des tinées à
contenir des dessins et d'autres figures conplexes

Aussi ces canvas peuvent contenir d'autres composants
widgets comme des frames, mais aussi des textes

#Les fonctions liées aux canvas
    -create_arc(): Pour créeer les arcs
    -create_bitmap(): pour créer les image bitmap
    -create_image(): pour créer les image
    -create_line() : pour faire une ou plusieurs lignes
    -create_oval(): les oval
    -create_polygine(): Un polygone
    -create_rectangle(): Un rectangle
    -create_text(): Pour insérer des texte
     -create_window(): Une fênetre

    
"""

#Fonction pour le traitement des images avec PIL inclu dans Pillow
def charger_image_from_PIL(filename, resize=None):
    image = PIL.Image.open(filename)

    if resize is not None:
        image = image.resize(resize, PIL.Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)

#Un simplement chargement de photo
def charger_image_from_TK(filename):
    return PhotoImage(file=filename)


#La fenêtre principale qui va être le parent du canvas
root = Tk()

root.title("Un arc")


#Création d'un objet de type Canvas
w = 1000
h = 2000
canvas = Canvas(root, width=w, height=h)
"""
        Les paramètres sont:
            bd ou borderwidth: laugeur de la bordure du canvas
            
            bg ou background:couleur arrière plan
            
            closeenough: Un flottant qui précise la distance minimale entre la souris et un item pour considérer que la souris est sur l'item
            
            confine: Si True (vf) il n'est pas possible de faire défiler le canvas en déhors de sa zone de visualisation
            
            cursor: pointeur de la souris utiliser sur le canvas
            
            height: hauteur du cancas
            
            hightlightbackground : couleur de la ligne de focus lorsque le canvas n'a pas le focus
            
            hightlightcolor: couleur de la ligne de focus lorsque le canvas à le focus
            
            hightlightthickness: Epeisseur de la ligne de focus (vf est 1)
            
            relief : Le style de relief du canvas (vf est "flat")
            
            scrollregion : Un tuple (s, w, n, s) qui indique ou définit la zone du canvas accessible pour défiler en sachant que : w:Ouest(gauche), e:Est(droite), n:Nord(Haut), S:Sud(Bas)
            
            selectbackground: Couleur de fond utulisée pour afficher l'item selectionné
            
            selectborderwidth: L'épaisseur de la bordure de l'item selectionné
            
            selectforeground : La couleur d'avant plan utilisée pour mettre en valeur l'item selectionné
            
            takefocus: Par defaut le focus est obtenu en utilisant la touche Tab seulemnt si un evenement a été prévu pour cela, si on lui donne la valeur 1 le canvas obtiendra le focus de manière ordinaire mais si on lui donne la valeur ("") on option le comportment normal donc avec la gestion de Tab
            
            width : La largeur du canvas
            
            xscrollincrement : Norlement le scroll se fait horizontalement à n'importe quelle position , ce comportement c'est par défaut et corespond à la valeur 0, pour une valeur positive de ce paramètre le scrolle en des position qui seront les multiple de cette valeur
            
            xscrollcommand :Si le canvas estt mini d'une bare de défilement, on peut positionner cette option en utilisant la méthode set() de la barre
            
            yscrollincrement: Même effet que xscrollincrement mais verticalement
            
            yscrollcommand: Même effet que xscrellcommand mais verticalemnt
            
            Les coodonnées
                Les coordonnées d'un point dans la fenêtre de vu correpond au coin superieur gauche de la fenêtre de vu
                Les coordonnées d'un point dans le canvas corespond au coin superieur gauche du canvas lui-même
                
            Liste d'affichage:
                 Par défaut, lorsqu’un item est créé, il est placé tout en haut de la liste d’affichage (et donc il apparaît au dessus des items déjà affichés), mais il est possible de ré-ordonner la liste d’affichage.
            
            Les identifiant numériques:
                Chaque item sur le canvas possède un identifiants numérique(un simple entier)unique, il s'agit de la valeur retounée par le contructeur  create_*() lors de la créatin d'un item
            
            
            Les marques (tags):
                Une marque est une chaine de caractère qu'on peut associer à plusieurs items du canvas
                Une peut être associée à autant d'items que l'on veutsur le canvas, 0 inclus
                Un items peut avoir autant de marques que souhaité, 0 inclus
            
            
            
    
            
            
                        
"""

#Cration d'un bitmaps
canvas.create_arc(100, 400, 400, 1200,start=45, dash=(7, 5), outline="yellow", fill="black", activedash=(8,1,), state="normal", stipple="gray25", style="chord", tags="Michel", width=7)

#Création d'un bitmap : C'est un image qui ne possède que deux couleurs : bg(vaut:0) fb(vaut:1)
# canvas.create_bitmap(350, 1000, anchor="sw", bitmap="hourglass", background="red")

#Récupération d'une image
img = charger_image_from_PIL("mic.jpg", resize=(300,400))

#Un canvas pour image
canvas.create_image(170, 250,image=img)


#Un canvas pour ligne
canvas.create_line(400,400,450,450, arrow="first", width="7")


#Création d'un cercle ou elipse
canvas.create_oval(350,350,490,500, width="12")

#Création d'un polygone
pts = [(400,150), (550,12), (700,150), (550,280)]
canvas.create_polygon(pts, dash=(4,2), fill="magenta", outline="yellow", width="7")

#Création d'un rectangle
canvas.create_rectangle(20,320, 350, 380, fill="gray")

#Création d'un texte
canvas.create_text(20, 550,text="C'est Excellence Michel le Seigneur Jésus est au controle", fill="red")

#Création d'une fenêtre
# canvas.create_window(800,600, window=root) #ça merde d'abord



canvas["bg"]= "green"

# print(un_arc)

canvas.pack()
but = Button(root, text="Sortir", command=root.quit, bg="yellow")
but.pack()

root.mainloop()

