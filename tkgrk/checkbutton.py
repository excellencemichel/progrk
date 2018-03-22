from tkinter import *

root = Tk()

root.title("Des cases à cocher")


#pour les checkbox

case_chek = Checkbutton(bg="red", text="Faites votre choix")

case_chek.pack()
case_chek2 = Checkbutton(bg="yellow", text="Ici alors")
case_chek2.flash()
case_chek2.select()
case_chek2.pack()


root.mainloop()