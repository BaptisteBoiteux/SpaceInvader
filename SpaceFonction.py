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
    #Les variables ci-dessous seeont valables pour tous les Alien
    dx = 10 #déplacement horizontale
    dy = 50 #déplacement vertical 
    rebond = 0 #nombres de rebond effectué en tout par le Alien
    y0 = 20 #position verticale des Aliens, elle est général car doit changer en même temps pour tous les Alien

    def __init__(self,x0,largeur,hauteur):
        """Initialisation de l'alien"""
        self.x0 = x0
        self.largeur = largeur
        self.x1 = x0 + largeur
        self.y0 = Alien.y0
        self.hauteur = hauteur
        self.y1 = Alien.y0 + hauteur
        self.detruit = False
    def deplacement(self):
        """ Deplacement de l'alien"""
        largeur_mw = 480 #on rapelle ici la largeur de la fenêtre tkinter
        # rebond à droite
        if self.x1 + Alien.dx > largeur_mw: #on detecte si l'Alien sort de la fenêtre à son prochain déplacement
            self.x0 = largeur_mw - (self.largeur - 2*Alien.dx) #on replace l'alien de droite à sa position en fin de fenêtre (on enlève 2*dx pour éviter le rapprochement des aliens)
            Alien.dx = -Alien.dx # on change le déplacement de sens pour tous les Alien
            Alien.rebond += 1
        # rebond à gauche (même fonctionement que ci-dessus)
        if self.x0 + Alien.dx < 0:
            self.x0 = 0
            Alien.dx = -Alien.dx
            Alien.rebond +=1
        #descente de l'alien
        if Alien.rebond == 2: #on detecte un aller-retour des Aliens
            Alien.y0 += Alien.dy #changement de la postion de tous les Alien
            Alien.rebond = 0
        #Affectation des attributs généraux à l'alien "appelé"
        self.x0 += Alien.dx
        self.x1 = self.x0 + self.largeur
        self.y0 = Alien.y0
        self.y1 = self.y0 + self.hauteur

class Vaisseau():
    def __init__(self):
        self.x  = 240
        self.x0 = 220
        self.x1 = 260
        self.y  = 280
        self.y1 = 302
        self.y0 = 258
        self.detruit = False
    def droite(self):
        self.x = self.x + 10
        self.x1 = self.x1 + 10
        self.x0 = self.x0 + 10  
    def gauche(self):       
        self.x  = self.x - 10
        self.x1 = self.x1 - 10
        self.x0 = self.x0 - 10  


class Missile():
    def __init__(self,x0,y0,sens):
        self.sens = sens
        self.vie = 3
        self.detruit = False
        if self.sens == 'vaisseau':
            self.x0 = x0
            self.x1 = x0+40
            self.y0 = y0-40
            self.y1 = y0
            self.x  = x0+20
            self.y  = y0-20
            self.dy   = -2
        if self.sens == 'alien':
            self.x0 = x0+20
            self.x1 = x0+60
            self.y0 = y0+40
            self.y1 = y0+80
            self.x  = x0+20
            self.y  = y0-20
            self.dy   = 2
    def deplacement_missile(self):
            if self.sens == 'vaisseau':
                self.y1 = self.y1 + self.dy 
                self.y0 = self.y0 + self.dy 
                self.y  = self.y0 + self.dy 
            if self.sens == 'alien':
                self.y1 = self.y1 + self.dy 
                self.y0 = self.y0 + self.dy 
                self.y  = self.y0 + self.dy 


class Abri :
     def __init__(self,x0,y0):
        self.largeur = 50
        self.hauteur = 10
        self.x0 = 220
        self.x1 = self.x0 + self.largeur
        self.y0 = 350
        self.y1 = self.y0 + self.hauteur
        self.vie = 5

def collision(objet1,objet2) :
    if objet1.y1 >= objet2.y0:
        objet1.detruit = True
        objet2.detruit = True

