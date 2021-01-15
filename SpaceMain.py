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
import random


#création des différentes entitées de chaques classes
alien0 = f.Alien(0,60,20)
alien1 = f.Alien(80,60,20)
alien2 = f.Alien(160,60,20)
roger = f.Vaisseau()

missile = [False,False]
missile_graph = [0,0]
nb_alien = 3

#variables globales utilisées dans tout le programme 
largeur_mw = 480
hauteur_mw = 320
play = False

def Commencer():
    """Lancement de la boucle de jeu"""
    global play

    if not play : #on detecte si le jeu à déjà été lancé 
        bigloop()
    play = True #on stocke le fait que le jeu ai été lancé

def bigloop ():
    f.collision(alien0,roger)
    f.collision(alien1,roger)
    f.collision(alien2,roger)
    #déplacement des différents alien :

    if not roger.detruit :
        alien_missile()
        deplacement_missile()
        if not alien0.detruit: 
            alien0.deplacement()
            Zone_jeux.coords(alien0_rec,alien0.x0,alien0.y0,alien0.x1,alien0.y1)#Changements des coordonnées
        else :
            Zone_jeux.delete(alien0_rec)
        if not alien1.detruit: 
            alien1.deplacement()
            Zone_jeux.coords(alien1_rec,alien1.x0,alien1.y0,alien1.x1,alien1.y1)
        else :
            Zone_jeux.delete(alien1_rec)
        if not alien2.detruit: 
            alien2.deplacement()
            Zone_jeux.coords(alien2_rec,alien2.x0,alien2.y0,alien2.x1,alien2.y1)
        else :
            Zone_jeux.delete(alien2_rec)
        mw.after(50,lambda:bigloop()) #mise à jour toutes les 50 ms
    else:
        messagebox.showinfo("GAME OVER","Vous avez perdu")

def droite():
    if (roger.x1 <= 470):
        roger.droite()
        Zone_jeux.move(roger_vaisseau,10,0)


def gauche():
    if (roger.x0 >= 10):
        roger.gauche()
        Zone_jeux.move(roger_vaisseau,-10,0)

def alien_missile():
    alien =[alien0,alien1,alien2]
    if missile[1] == False:
        rand = random.randint (0,nb_alien-1)
        missile[1] = f.Missile(alien[rand].x0,alien[rand].y1,'alien',alien[rand].largeur,alien[rand].hauteur)
        missile_graph[1] = Zone_jeux.create_image(missile[1].x,missile[1].y,image= img_missile)

def tirer():
    if missile[0] == False:
        missile[0] = f.Missile(roger.x0,roger.y0,'vaisseau')
        missile_graph[0] = Zone_jeux.create_image(missile[0].x,missile[0].y,image= img_missile)

def deplacement_missile():
    cpt=0
    while cpt < len(missile):
        if missile[cpt] != False:
            if missile[cpt].y0 <=10 or missile[cpt].y1 >=310:
                Zone_jeux.delete(missile_graph[cpt])
                missile[cpt] = False
            else:
                missile[cpt].deplacement_missile()
                Zone_jeux.move(missile_graph[cpt],0,missile[cpt].dy)
        cpt = cpt+1


# création de la fenêtre graphique
mw = Tk()
score = StringVar()
score.set("score:0")
mw.title('Bretons Invader')

# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur_mw, height = hauteur_mw, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)

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
mw.bind('<Right>', lambda _:droite())
mw.bind('<Left>', lambda _:gauche())
mw.bind('<space>', lambda _:tirer())

#detection des input
#lancement du gestionnaire d'événements
mw.mainloop()