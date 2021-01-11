#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
TODO : Avoir une seule fonction garphique qui met à jour ici et mettre les classes et les fonxtions logiques dans le SpaceFonction
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


alien0 = f.Alien(0,60,20,20)
alien1 = f.Alien(80,60,20,20)
largeur_mw = 480
hauteur_mw = 320
play = False

def Commencer():
    """Commande qui se lance a l'appui du bouton commencer"""
    alien0.deplacement()
    # affichage
    Zone_jeux.coords(alien0_rec,alien0.x0,alien0.y0,alien0.x1,alien0.y1)
    # mise à jour toutes les 50ms
    mw.after(50,lambda:alien0.deplacement())

# création de la fenêtre graphique
mw = Tk()
score = StringVar()
score.set("score:0")
mw.title('Bretons Invader')
# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur_mw, height = hauteur_mw, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
alien0_rec = Zone_jeux.create_rectangle(alien0.x0,alien0.y0,alien0.x1,alien0.y1)
#alien1 = Zone_jeux.create_rectangle(alien1.x-moitie_x,y-moitie_y,x+moitie_x,y+moitie_y)
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