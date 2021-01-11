#Header 
"""
quoi : Programme qui comportes les fonctions du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
"""

#Importation des bibilothèques
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu


def Debut():
    messagebox.showinfo("Bienvenue","La partie va être lancé")

def Apropos():
    messagebox.showinfo("A Propos","Ce jeu à été créer par Julien Mercier et Baptiste Boiteux\nIl s'inspire du jeux Space Invader conçu par Tomohiro Nishikado en 1978")

class Alien():
    def __init__(self,largeur,hauteur,x,y):
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.rebond = 0
        self.dx = 5
        self.detruit = False

class Vaisseau():
    def __init__(self):
        self.x  = 240
        self.x0 = 220
        self.x1 = 260
        self.y  = 280
        self.y1 = 302
        self.y0 = 258
    def droite(self):
        self.x = self.x + 10
        self.x1 = self.x1 + 10
        self.x0 = self.x0 + 10  
    def gauche(self):       
        self.x  = self.x - 10
        self.x1 = self.x1 - 10
        self.x0 = self.x0 - 10  


class Missile():
    def __init__(self,master,x0,y0,sens):
        self.master = master
        self.sens = sens
        self.img = PhotoImage(file="Image/tha_le_misille.png")
        if self.sens == 'vaisseau':
            self.x0 = x0
            self.x1 = x0+40
            self.y0 = y0-40
            self.y1 = y0
            self.misille = self.master.create_image(self.x1-20,self.y1-20,image = self.img)
        if self.sens == 'alien':
            self.x0 = x0+20
            self.x1 = x0+40
            self.y0 = y0+40
            self.y1 = y0
            self.misille = self.master.create_image(self.x1-20,self.y1-20,image = self.img)
    def deplacement_missile(self):
            if self.sens == 'vaisseau':
                if self.x0 > 10:
                    self.master.move(self.misille,0,-10)
                    self.x1 = self.y1 - 10
                    self.x0 = self.y0 - 10  
                    self.master.after(1000,self.deplacement_missile())