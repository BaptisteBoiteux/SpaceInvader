#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
"""

#Importation des bibilothèques
import SpaceFonction as f
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu



class Vaisseau():
    def __init__(self,master):
        self.master = master
        self.img = PhotoImage(file="Image/Logo_RogerVoyage1.png")
        self.vaisseaux = self.master.create_image(260, 280,image=self.img)

    def droite(self):
        self.master.move(self.vaisseaux,10,0)
    def gauche(self):
        self.master.move(self.vaisseaux,-10,0)

# création de la fenêtre graphique
mw = Tk()
score = StringVar()
score.set("score:0")
mw.title('Space Invader')
# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Zone_jeux = Canvas(mw, width = Largeur, height =Hauteur, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
# Création d'un widget Label (score)
Label1 = Label(mw,textvariable = score)
Label1.pack(side = 'bottom', padx = 5, pady = 5)
# Création d'un widget Button (bouton Quitter)
Button(mw, text ='Quitter' ,command = mw.destroy).pack(side='bottom',padx=5,pady=5)
# Création d'un widget Button (bouton Commencer)
Button(mw, text ='Commencer', command = f.Debut ).pack(side='bottom',padx=5,pady=5)
# Création d'un widget Menu
menubar = Menu(mw)
menuoptions = Menu(menubar,tearoff = 0)
menuoptions.add_command(label = "Quitter",command = mw.destroy)
menubar.add_cascade(label = "Options", menu = menuoptions)
menuaide = Menu(menubar,tearoff = 0)
menuaide.add_command(label = "A propos",command = f.Apropos)
menubar.add_cascade(label = "Aide", menu = menuaide)
# Affichage du menu
mw.config(menu = menubar)
#vaisseaux
roger = Vaisseau(Zone_jeux)
#detection des input
mw.bind('<Right>', lambda _:roger.droite())
mw.bind('<Left>', lambda _:roger.gauche())

#lancement du gestionnaire d'événements
mw.mainloop()