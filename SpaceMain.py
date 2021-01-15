#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
TODO :
"""

#Importation des bibilothèques
import SpaceFonction as f
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu



#création des différentes entitées de chaques classes
alinen_bonus = []
alien0 = f.Alien(0,60,20)
alien1 = f.Alien(80,60,20)
alien2 = f.Alien(160,60,20)
roger = f.Vaisseau()
missile = [False,False] # variable qui stocke les classe
missile_graph = [0,0] # variable qui stocke le graphique du missile
nb_alien = 3
#variables globales utilisées dans tout le programme 
largeur_mw = 480
hauteur_mw = 320
play = False

def Commencer():
    """Lancement de la boucle de jeu"""
    global play

    if not play : #on detecte si le jeu à déjà été lancé 
        alien_mort = 0
        mw.bind('<Right>', lambda _:droite())
        mw.bind('<Left>', lambda _:gauche())
        mw.bind('<space>', lambda _:tirer())
        bigloop(alien_mort)
    play = True #on stocke le fait que le jeu ai été lancé

def bigloop (alien_mort):
    #déplacement des différents alien :
    alien  = [alien0,alien1,alien2]
    for invader in alien:
        if missile[0] != False :
            if(invader.vie>0):
                if(f.collision(invader,missile[0])):
                    missile[0]=False
                    Zone_jeux.delete(missile_graph[0])
                    alien_mort += 1
    if (alien_mort>=nb_alien):
        messagebox.showinfo("Les breton batte en retraite","La normandie peut etre fiere de vous")
        Zone_jeux.delete('all')
    elif not roger.vie == 0 :
        alien_missile()
        deplacement_missile()
        if not alien0.vie == 0: 
            alien0.deplacement()
            Zone_jeux.coords(alien0_rec,alien0.x0,alien0.y0,alien0.x1,alien0.y1)#Changements des coordonnées
        else :
            Zone_jeux.delete(alien0_rec)
        if not alien1.vie == 0: 
            alien1.deplacement()
            Zone_jeux.coords(alien1_rec,alien1.x0,alien1.y0,alien1.x1,alien1.y1)
        else :
            Zone_jeux.delete(alien1_rec)
        if not alien2.vie == 0: 
            alien2.deplacement()
            Zone_jeux.coords(alien2_rec,alien2.x0,alien2.y0,alien2.x1,alien2.y1)
        else :
            Zone_jeux.delete(alien2_rec)
        mw.after(50,lambda:bigloop(alien_mort)) #mise à jour toutes les 50 ms
    else:
        messagebox.showinfo("GAME OVER","Vous avez perdu")

def droite():
    # permet de deplacer le vaisseau sur la droite
    if (roger.x1 <= 470):
        roger.droite()
        Zone_jeux.move(roger_vaisseau,10,0) #deplace le vaisseau a droite


def gauche():
    # permet de deplacer le vaisseau sur la gauche
    if (roger.x0 >= 10):
        roger.gauche()
        Zone_jeux.move(roger_vaisseau,-10,0) #deplace le vaisseau a gauche

def alien_missile():
    # fonction qui permet de faire tirer les alien
    alien  = [alien0,alien1,alien2]
    tireur = f.tir_alien(alien) # on choisi qu'elle alien va tirer
    if missile[1] == False: # on detecte si il n'y a pas deja de missile alien
        missile[1] = f.Missile(tireur.x0,tireur.y1,'alien',tireur.largeur,tireur.hauteur) # crée le missile
        missile_graph[1] = Zone_jeux.create_image(missile[1].x,missile[1].y,image= img_missile) # affiche le missile

def tirer():
    # fonction qui permet de faire tirer le vaisseau
    if missile[0] == False: # on detecte si il n'y a pas deja de missile tirer
        missile[0] = f.Missile(roger.x0,roger.y0,'vaisseau',roger.largeur,roger.hauteur) # crée le missile
        missile_graph[0] = Zone_jeux.create_image(missile[0].x,missile[0].y,image= img_missile) # affiche le missile

def deplacement_missile():
    # fonction qui permet faire deplacer les missile
    cpt=0
    while cpt < len(missile):
        if missile[cpt] != False:# on regarde si le missile est tirer
            if missile[cpt].y0 <=10 or missile[cpt].y1 >=310: # on regarde si le missile touche un bord
                Zone_jeux.delete(missile_graph[cpt])# on efface le missile
                missile[cpt] = False# on detruit le missile
            else:
                missile[cpt].deplacement_missile()
                Zone_jeux.move(missile_graph[cpt],0,missile[cpt].dy)# on deplace le missile
        cpt = cpt+1

    

# création de la fenêtre graphique
mw = Tk()
score = StringVar()
score.set("score:0")
mw.title('Bretons Invader')

# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur_mw, height = hauteur_mw, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
img_Mont    = PhotoImage(file='Image/mont_saint_michel.png')
Zone_jeux.create_image(largeur_mw/2,hauteur_mw/2,image= img_Mont)
#Initialisationdes éléments graphiques
alien0_rec = Zone_jeux.create_rectangle(alien0.x0,alien0.y0,alien0.x1,alien0.y1)
alien1_rec = Zone_jeux.create_rectangle(alien1.x0,alien1.y0,alien1.x1,alien1.y1)
alien2_rec = Zone_jeux.create_rectangle(alien2.x0,alien2.y0,alien2.x1,alien2.y1)
img_vaisseau = PhotoImage(file='Image/Logo_RogerVoyage1.png')
img_missile = PhotoImage(file='Image/tha_le_misille.png')
roger_vaisseau = Zone_jeux.create_image(roger.x,roger.y,image= img_vaisseau)

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
#detection des input
#lancement du gestionnaire d'événements
mw.mainloop()