#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
TODO : Voir nombres de vies vaisseaux
Remarques : les erreurs sont dû à l'apparition du missile mais n'empèchent pas le bon fonctionement du jeu
"""

#Importation des bibilothèques
import SpaceFonction as f
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu


#variables globales utilisées dans tout le programme 
largeur_mw = 480
hauteur_mw = 320
play = False

#création des différentes entitées de chaques classes
alinen_bonus = []
alien0 = f.Alien(0,60,20)
alien1 = f.Alien(80,60,20)
alien2 = f.Alien(160,60,20)
ilot0 = f.Ilot((largeur_mw/5)-50,200)
ilot1 = f.Ilot((2*largeur_mw/5)-50,200)
ilot2 = f.Ilot((3*largeur_mw/5),200)
ilot3 = f.Ilot((4*largeur_mw/5),200)
roger = f.Vaisseau()
missile = [False,False] # variable qui stocke les classe (0 pour le vaisseau est 1 pour le missile)
missile_graph = [0,0] # variable qui stocke le graphique du missile
nb_alien = 3
score = 0

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
    global score,play
    #déplacement des différents alien :
    alien  = [alien0,alien1,alien2]
    for invader in alien:
        if missile[0] != False :
            if(invader.vie>0):
                if(collision(invader)):
                    missile[0]=False
                    Zone_jeux.delete(missile_graph[0])
                    alien_mort += 1
                    score = alien_mort*25
    if (alien_mort >= nb_alien):
        messagebox.showinfo("Les bretons battent en retraite !","La normandie peut être fière de vous")
        Zone_jeux.delete('all')
    elif not roger.vie == 0 :
        alien_missile()
        deplacement_missile()
        #Test des collion entre les missiles et les différents éléments
        if missile[1] != False: 
            if collision(roger):
                missile[1] = False
                Zone_jeux.delete(missile_graph[1])
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
        ilot = [ilot0,ilot1,ilot2,ilot3]
        for abri in ilot:
            if abri.vie > 0:
                if collision(abri):
                    if missile[1] != False and collision(missile[1]):
                        abri.touche_alien()
                        missile[1] = False
                        Zone_jeux.delete(missile_graph[1])
                    if missile[0] != False and collision(missile[0]):
                        abri.touche_vaisseau()
                        missile[0] = False
                        Zone_jeux.delete(missile_graph[0])
                    Zone_jeux.coords(ilot0_rec,ilot0.x0,ilot0.y0,ilot0.x1,ilot0.y1)#Changements des coordonnées
                    Zone_jeux.coords(ilot1_rec,ilot1.x0,ilot1.y0,ilot1.x1,ilot1.y1)
                    Zone_jeux.coords(ilot2_rec,ilot2.x0,ilot2.y0,ilot2.x1,ilot2.y1)
                    Zone_jeux.coords(ilot3_rec,ilot3.x0,ilot3.y0,ilot3.x1,ilot3.y1)
        if ilot0.vie == 0 :
            Zone_jeux.delete(ilot0_rec)
        if ilot1.vie == 0 :
            Zone_jeux.delete(ilot1_rec)
        if ilot2.vie == 0 :
            Zone_jeux.delete(ilot2_rec)
        if ilot3.vie == 0 :
            Zone_jeux.delete(ilot3_rec)
        
        score_aff.set("score: "+str(score))
        vie_aff.set("vie: "+str(roger.vie))
        mw.after(50,lambda:bigloop(alien_mort)) #mise à jour toutes les 50 ms
    else:
        messagebox.showinfo("GAME OVER","Vous avez perdu")
        Zone_jeux.delete('all')
        play = False


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
    global nb_alien
    if nb_alien !=0:
        alien  = [alien0,alien1,alien2]
        tireur = f.tir_alien(alien) # on choisi quel alien va tirer
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
            if missile[cpt].y0 <=10 or missile[cpt].y1 >= 310: # on regarde si le missile touche un bord
                Zone_jeux.delete(missile_graph[cpt])# on efface le missile
                missile[cpt] = False# on detruit le missile
            else:
                missile[cpt].deplacement_missile()
                Zone_jeux.move(missile_graph[cpt],0,missile[cpt].dy)# on deplace le missile
        cpt = cpt+1

def collision(objet) :
    chevauchement = Zone_jeux.find_overlapping(objet.x0, objet.y0, objet.x1, objet.y1)
    if len(chevauchement) > 2:
        objet.vie -= 1
        return True
    return False

    

# création de la fenêtre graphique
mw = Tk()
score_aff = StringVar()
score_aff.set("score:0")
vie_aff = StringVar()
vie_aff.set("vie:3")
mw.title('Bretons Invader')

# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur_mw, height = hauteur_mw, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
img_Mont = PhotoImage(file='Image/mont_saint_michel.png')
Zone_jeux.create_image(largeur_mw/2,hauteur_mw/2,image= img_Mont)
#Initialisationdes éléments graphiques
alien0_rec = Zone_jeux.create_rectangle(alien0.x0,alien0.y0,alien0.x1,alien0.y1)
alien1_rec = Zone_jeux.create_rectangle(alien1.x0,alien1.y0,alien1.x1,alien1.y1)
alien2_rec = Zone_jeux.create_rectangle(alien2.x0,alien2.y0,alien2.x1,alien2.y1)
ilot0_rec = Zone_jeux.create_rectangle(ilot0.x0,ilot0.y0,ilot0.x1,ilot0.y1, fill = 'black')
ilot1_rec = Zone_jeux.create_rectangle(ilot1.x0,ilot1.y0,ilot1.x1,ilot1.y1, fill = 'black')
ilot2_rec = Zone_jeux.create_rectangle(ilot2.x0,ilot2.y0,ilot2.x1,ilot2.y1, fill = 'black')
ilot3_rec = Zone_jeux.create_rectangle(ilot3.x0,ilot3.y0,ilot3.x1,ilot3.y1, fill = 'black')
img_vaisseau = PhotoImage(file='Image/Logo_RogerVoyage1.png')
img_missile = PhotoImage(file='Image/tha_le_misille.png')
roger_vaisseau = Zone_jeux.create_image(roger.x,roger.y,image= img_vaisseau)

# Création d'un widget Label (score)
Label1 = Label(mw,textvariable = score_aff)
Label1.pack(side = 'right', padx = 5, pady = 5)
# Création d'un widget Label (vie)
Label1 = Label(mw,textvariable = vie_aff)
Label1.pack(side = 'right', padx = 5, pady = 5)

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