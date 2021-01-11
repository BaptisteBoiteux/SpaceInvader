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