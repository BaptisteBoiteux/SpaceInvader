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


largeur = 480
hauteur = 320
x = 20
moitie_alien = 20
dx = 2

def deplacement_alien():
    """ Deplacement de l'alien"""
    global x,dx,largeur,hauteur
    # rebond à droite
    if x+moitie_alien+ dx > largeur:
        x = 2*(largeur-moitie_alien)-x
        dx = -dx
        
    # rebond à gauche
    if x-moitie_alien+dx < 0:
        x = 2*moitie_alien-x
        dx = -dx
    x = x+dx
    # affichage
    Zone_jeux.coords(alien,x-moitie_alien,10,x+moitie_alien,50)
    # mise à jour toutes les 200ms
    mw.after(50,deplacement_alien)

# création de la fenêtre graphique
mw = Tk()
score = StringVar()
score.set("score:0")
mw.title('Bretons Invader')
# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur, height = hauteur, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
alien = Zone_jeux.create_rectangle(x-moitie_alien,10,x+moitie_alien,50)
# Création d'un widget Label (score)
Label1 = Label(mw,textvariable = score)
Label1.pack(side = 'bottom', padx = 5, pady = 5)
# Création d'un widget Button (bouton Quitter)
Button(mw, text ='Quitter' ,command = mw.destroy).pack(side='bottom',padx=5,pady=5)
# Création d'un widget Button (bouton Commencer)
Button(mw, text ='Commencer', command = deplacement_alien ).pack(side='bottom',padx=5,pady=5)
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
#lancement du gestionnaire d'événements
mw.mainloop()