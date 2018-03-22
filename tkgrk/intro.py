#Le chargement du module
from tkinter import *


"""
Tout commence par la construction d'une fenêtre
"""
root = Tk()

#Ajout d'un titre
root.title("Un simpe titre comme exemple")


root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


#Création d'un label
lab = Label(root,  text="Le label qui tourne", height=30)
lab.grid(row=8, column=43, columnspan=10, ipadx=89, padx=7888, rowspan=12, sticky="s")
lab.grid_forget()
#Affichage du label dans la fenêtre
lab.pack()

#Création d'un bouton
but = Button(root, activebackground="red", bd="8", bg="yellow", text="Quitter", command=root.quit, fg="green", underline=1, width=30)
# but.grid(row=0, column=0, sticky="nw")
but.flash()


#Et on place le bouton dans la fenêtre
but.pack()



#On lance la fenêtre avec la boucle mainloop()
root.mainloop()





root1 = Tk()
root1.title("La roote 2")

qb = Button(root1, text="Sortir", command=root1.quit)
qb.pack()

# root1.mainloop()
