#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
TODO : voir bug debut deplacement et acceleration bouton commencer, regler disparition du vaisseau sur les bords
"""

#Importation des bibilothèques
import SpaceFonction as f
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu



class Vaisseau():
    def __init__(self,master):
        self.master = master
        self.img = PhotoImage(file="Image/Logo_RogerVoyage1.png")
        self.vaisseaux = self.master.create_image(240, 280,image=self.img)
        self.x0 = 220
        self.x1 = 260
        self.y1 = 302
        self.y0 = 258
    def droite(self):
        if (self.x1 <= 470):
            self.master.move(self.vaisseaux,10,0)
            self.x1 = self.x1 + 10
            self.x0 = self.x0 + 10  
    def gauche(self):
        if (self.x0 >= 10):
            self.master.move(self.vaisseaux,-10,0)
            self.x1 = self.x1 - 10
            self.x0 = self.x0 - 10  
class Alien():
    def __init__(self,largeur,hauteur,x,y):
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.rebond = 0
        self.detruit = False

alien0 = Alien(60,20,30,30)
largeur_mw = 480
hauteur_mw = 320
x = alien0.x
y = alien0.y
moitie_x = alien0.largeur/2
moitie_y = alien0.hauteur/2
dx = 5
play = False
rebond = alien0.rebond

def Commencer():
    """Commande qui se lance a l'appui du bouton commencer"""
    global play
    if not play :
        deplacement_alien()
    play = True


def deplacement_alien():
    """ Deplacement de l'alien"""
    global x,dx,y,rebond
    # rebond à droite
    if x+moitie_x+ dx > largeur_mw:
        x = 2*(largeur_mw-moitie_x)-x
        dx = -dx
        rebond += 1
    # rebond à gauche
    if x-moitie_x+dx < 0:
        x = 2*moitie_x-x
        dx = -dx
        rebond +=1
    x = x+dx
    #descente de l'alien
    if rebond == 2:
        y = y + 10
        rebond = 0
    # affichage
    Zone_jeux.coords(alien,x-moitie_x,y-moitie_y,x+moitie_x,y+moitie_y)
    # mise à jour toutes les 200ms
    mw.after(50,deplacement_alien)

# création de la fenêtre graphique
mw = Tk()
score = StringVar()
score.set("score:0")
mw.title('Bretons Invader')
# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur_mw, height = hauteur_mw, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
alien = Zone_jeux.create_rectangle(x-moitie_x,y-moitie_y,x+moitie_x,y+moitie_y)
# Création d'un widget Label (score)
Label1 = Label(mw,textvariable = score)
Label1.pack(side = 'bottom', padx = 5, pady = 5)
# Création d'un widget Button (bouton Quitter)
Button(mw, text ='Quitter' ,command = mw.destroy).pack(side='bottom',padx=5,pady=5)
# Création d'un widget Button (bouton Commencer)
Button(mw, text ='Commencer', command = Commencer).pack(side='bottom',padx=5,pady=5)
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