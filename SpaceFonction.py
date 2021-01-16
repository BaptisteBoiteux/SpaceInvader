#Header 
"""
quoi : Programme qui comportes les fonctions du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
"""

#Importation des bibilothèques
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu
import random


def Debut():
    messagebox.showinfo("Bienvenue","La partie va être lancé")

def Apropos():
    messagebox.showinfo("A Propos","Ce jeu à été créer par Julien Mercier et Baptiste Boiteux\nIl s'inspire du jeux Space Invader conçu par Tomohiro Nishikado en 1978")

class Alien():
    #Les variables ci-dessous seeont valables pour tous les Alien
    dx = 2 #déplacement horizontale
    dy = 5 #déplacement vertical 
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
        self.vie = 1
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
        """Initialisation de vaisseau"""
        self.x  = 240 # permet de determiner le x afin permettant d'afficher le vaisseau
        self.y  = 280 # permet de determiner le y afin permettant d'afficher le vaisseau
        self.largeur = 40
        self.hauteur = 44
        self.dx= 10
        # initialiser les coordonées du vaisseux
        self.x0 = 220
        self.x1 = 260
        self.y1 = 302
        self.y0 = 258
        self.vie = 3
    def droite(self):
        # mise a jour des coordonées du vaisseux apres un deplacement a droite
        self.x = self.x   + self.dx
        self.x1 = self.x1 + self.dx
        self.x0 = self.x0 + self.dx  
    def gauche(self):       
        # mise a jour des coordonées du vaisseux apres un deplacement a gauche
        self.x  = self.x  - self.dx
        self.x1 = self.x1 - self.dx
        self.x0 = self.x0 - self.dx


class Missile():
    def __init__(self,x,y,sens,largeur,hauteur):
        """Initialisation du missile"""
        self.sens = sens # fais la difference entre missile alien et vaisseau
        self.dy = 8 # deplacement du missile
        self.vie = 1
        self.hauteur = 40
        self.largeur = 40
        if self.sens == 'vaisseau':
            self.x  = x+(largeur/2)# permet de determiner le x afin permettant d'afficher un missile
            self.y  = y-(self.hauteur/2)# permet de determiner le y afin permettant d'afficher un misile
            # initialiser les coordonées du missile
            self.x0 = x
            self.x1 = x+self.largeur
            self.y0 = y-self.hauteur
            self.y1 = y
            self.dy = -self.dy # le dy est inverser car le missile monte
        if self.sens == 'alien':
            self.x  = x+(largeur/2)     # permet de determiner le x afin permettant d'afficher un misile
            self.y  = y+(self.hauteur/2)# permet de determiner le y afin permettant d'afficher un misile
            # initialiser les coordonées du missile
            self.x0 = x+(largeur/2)-(self.largeur/2)
            self.x1 = x+(largeur/2)+(self.largeur/2)
            self.y0 = y
            self.y1 = y+self.hauteur
    def deplacement_missile(self):
            if self.sens == 'vaisseau':
                # mise a jour des coordonées du missile apres le deplacement
                self.y1 = self.y1 + self.dy 
                self.y0 = self.y0 + self.dy 
                self.y  = self.y0 + self.dy 
            if self.sens == 'alien':
                # mise a jour des coordonées du missile apres le deplacement
                self.y1 = self.y1 + self.dy 
                self.y0 = self.y0 + self.dy 
                self.y  = self.y0 + self.dy 


class Ilot :
     def __init__(self,x0,y0):
        self.largeur = 50
        self.hauteur = 10
        self.x0 = 220
        self.x1 = self.x0 + self.largeur
        self.y0 = 350
        self.y1 = self.y0 + self.hauteur
        self.vie = 5



def tir_alien(alien):
    nb_alien_vie=[]
    for invader in alien:
        if invader.vie>0:
            nb_alien_vie.append(invader)
    rand = random.randint (0,len(nb_alien_vie)-1)
    return nb_alien_vie[rand]



