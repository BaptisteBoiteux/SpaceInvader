#Header 
"""
quoi : Programme qui comportes les fonctions du projet Space Invador
qui : Baptiste Boiteux
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
"""

#Importation des bibilothèques
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu


def Debut():
    messagebox.showinfo("Bienvenue","La partie va être lancé")

def Apropos():
    messagebox.showinfo("A Propos","Ce jeu à été créer par Julien Mercier et Baptiste Boiteux\nIl s'inspire du jeux Space Invader conçu par Tomohiro Nishikado en 1978")