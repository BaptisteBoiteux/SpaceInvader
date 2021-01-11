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
    def __init__(self,x0,largeur,y0,hauteur):
        self.x0 = x0
        self.largeur = largeur
        self.x1 = x0 + largeur
        self.y0 = y0
        self.hauteur = hauteur
        self.y1 = y0 + hauteur
        self.rebond = 0
        self.dx = 5
        self.detruit = False
    def deplacement(self):
        """ Deplacement de l'alien"""
        largeur_mw = 480
        # rebond à droite
        if self.x1 + self.dx > largeur_mw:
            self.x0 = largeur_mw-self.largeur
            self.dx = -self.dx
            self.rebond += 1
        # rebond à gauche
        if self.x0 + self.dx < 0:
            self.x0 = 0
            self.dx = -self.dx
            self.rebond +=1
        self.x0 += self.dx
        self.x1 = self.x0 + self.largeur
        #descente de l'alien
        if self.rebond == 2:
            self.y0 += 10
            self.y1 = self.y0 + self.hauteur
            self.rebond = 0