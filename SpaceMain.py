#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux, Mercier Julien
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
TODO : Changer les alien en drapeaux bretons
Remarques : Des erreurs s'affichent sur VSCODE : elles sont dûes à l'apparition du missile mais n'empèchent pas le bon fonctionement du jeu
"""

#Importation des bibilothèques
import SpaceFonction as f
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog, Menu


#variables globales utilisées dans tout le programme 
largeur_mw = 480
hauteur_mw = 320
play = False

#création des différentes entitées de chaques classes
alien_bonus = []
alien_bonus_graph = [0]
#les ilots sont régulièrements espacés grâce à la largeur de la fenêtre
ilot0 = f.Ilot((largeur_mw/5)-50,200)
ilot1 = f.Ilot((2*largeur_mw/5)-50,200)
ilot2 = f.Ilot((3*largeur_mw/5),200)
ilot3 = f.Ilot((4*largeur_mw/5),200)
alien0 = f.Alien_normal(0,60,32)
alien1 = f.Alien_normal(80,60,32)
alien2 = f.Alien_normal(160,60,32)
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
        cpt = 0
        mw.bind('<Right>', lambda _:droite())
        mw.bind('<Left>', lambda _:gauche())
        mw.bind('<space>', lambda _:tirer())
        bigloop(alien_mort,cpt)
    play = True #on stocke le fait que le jeu ai été lancé

def bigloop (alien_mort,cpt):
    global score, play
    # on gere l'alien bonus pour qu'il apparaise toute les 10 seconde et disparaise apres 5 seconde
    if cpt==200:
        alien_bonus.append(f.Alien_bonus(0,0,40,15,5))
        alien_bonus_graph[0]= Zone_jeux.create_rectangle(alien_bonus[0].x0,alien_bonus[0].y0,alien_bonus[0].x1,alien_bonus[0].y1, fill = 'red')
    if cpt==375:
        if alien_bonus:
            alien_bonus.pop(0)
            Zone_jeux.delete(alien_bonus_graph[0])
        cpt = 0
    #detecte si l'alien bonus se fait toucher
    if (not alien_bonus) == False:
        if missile[0] != False :
            if(collision(alien_bonus[0])): #on détecte si l'alien bonus à été touché
                missile[0]=False
                Zone_jeux.delete(missile_graph[0])
                Zone_jeux.delete(alien_bonus_graph[0]) 
                score += 150 #on incrémente le score
                alien_bonus.pop(0)
    #detecte si les alien se font toucher    
    alien  = [alien0,alien1,alien2]
    for invader in alien:
        if missile[0] != False :
            if(invader.vie>0):
                if(collision(invader)):
                    missile[0]=False
                    Zone_jeux.delete(missile_graph[0])
                    alien_mort += 1
                    score += 25 #on incrémente le score
    if (alien_mort >= nb_alien):
        # bravo vous avez tué tous les aliens
        messagebox.showinfo("Les bretons battent en retraite !","La normandie peut être fière de vous")
        Zone_jeux.delete('all')
        play = False
        fin_jeux()
    # on regarde si le vaisseau a toujours des vie
    elif not roger.vie == 0:
        #Detection des aliens qui descende au niveau du vaisseau
        if alien0.y1 > roger.y0 or alien1.y1 > roger.y0 or alien1.y1 > roger.y0:
                roger.vie = 0
        if (cpt%100 == 0):
            alien_missile()
        deplacement_missile()
        #Test des collion entre les missiles et les différents éléments
        if missile[1] != False: 
            if collision(roger):
                missile[1] = False
                Zone_jeux.delete(missile_graph[1])
        if (not alien_bonus) == False:
            alien_bonus[0].deplacement()
            Zone_jeux.coords(alien_bonus_graph[0],alien_bonus[0].x0,alien_bonus[0].y0,alien_bonus[0].x1,alien_bonus[0].y1)
        #Déplacement des aliens si ils sont encore en vie et destruction de l'image sinon
        if not alien0.vie == 0:
            alien0.deplacement()
            Zone_jeux.move(alien0_rec,alien0.dx,alien0.dy)
        else :
            Zone_jeux.delete(alien0_rec)
        if not alien1.vie == 0: 
            alien1.deplacement()
            Zone_jeux.move(alien1_rec,alien1.dx,alien0.dy)
        else :
            Zone_jeux.delete(alien1_rec)
        if not alien2.vie == 0: 
            alien2.deplacement()
            Zone_jeux.move(alien2_rec,alien2.dx,alien0.dy)
        else :
            Zone_jeux.delete(alien2_rec)
        #gestion de la destruction des ilots
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
                    #Changements des coordonnées
                    Zone_jeux.coords(ilot0_rec,ilot0.x0,ilot0.y0,ilot0.x1,ilot0.y1)
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
        #mise à jour de l'affichage du score
        score_aff.set("score: "+str(score))
        vie_aff.set("vie: "+str(roger.vie))
        cpt += 1
        mw.after(50,lambda:bigloop(alien_mort,cpt)) #mise à jour toutes les 50 ms
    else:
        #fin de partie perdu
        messagebox.showinfo("GAME OVER","Vous avez perdu")
        Zone_jeux.delete('all')
        fin_jeux()

def fin_jeux():
    # cette fonction permet de remetre les alien et le vaissseau a leur place de depart pour pouvoir recommencer le jeux
    global play, score, ilot0, ilot1, ilot2, ilot3, alien0, alien1, alien2, roger, ilot0_rec, ilot1_rec, ilot2_rec, ilot3_rec, roger_vaisseau, alien0_rec, alien1_rec ,alien2_rec
    play = False # on met a False pour faire recommencer le jeux quand on clique sur play
    score = 0
    # on remet le fond
    Zone_jeux.create_image(largeur_mw/2,hauteur_mw/2,image= img_Mont)
    # on réinitialise les ilots
    ilot0 = f.Ilot((largeur_mw/5)-50,200)
    ilot1 = f.Ilot((2*largeur_mw/5)-50,200)
    ilot2 = f.Ilot((3*largeur_mw/5),200)
    ilot3 = f.Ilot((4*largeur_mw/5),200)
    # on réinitialise les aliens
    alien_bonus = []
    alien_bonus_graph = [0]
    alien0 = f.Alien_normal(0,60,20)
    alien1 = f.Alien_normal(80,60,20)
    alien2 = f.Alien_normal(160,60,20)
    alien0.y0 = 20
    alien0.y1 = 40
    alien0.y = 30
    alien1 = f.Alien_normal(80,60,20)
    alien1.y0 = 20
    alien1.y1 = 40
    alien1.y = 30
    alien2 = f.Alien_normal(160,60,20)
    alien2.y0 = 20
    alien2.y1 = 40
    alien2.y = 30
    roger = f.Vaisseau()
    alien0_rec = Zone_jeux.create_image(alien0.x,alien0.y,image= img_alien)
    alien1_rec = Zone_jeux.create_image(alien1.x,alien1.y,image= img_alien)
    alien2_rec = Zone_jeux.create_image(alien2.x,alien2.y,image= img_alien)
    # on réinitialise le vaisseau
    roger = f.Vaisseau()
    # on réinitialise l'affichage des ilos
    ilot0_rec = Zone_jeux.create_rectangle(ilot0.x0,ilot0.y0,ilot0.x1,ilot0.y1, fill = 'black')
    ilot1_rec = Zone_jeux.create_rectangle(ilot1.x0,ilot1.y0,ilot1.x1,ilot1.y1, fill = 'black')
    ilot2_rec = Zone_jeux.create_rectangle(ilot2.x0,ilot2.y0,ilot2.x1,ilot2.y1, fill = 'black')
    ilot3_rec = Zone_jeux.create_rectangle(ilot3.x0,ilot3.y0,ilot3.x1,ilot3.y1, fill = 'black')
    # on réinitialise l'affichage du vaisseau
    roger_vaisseau = Zone_jeux.create_image(roger.x,roger.y,image= img_vaisseau)


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
    """gère la collision sur un objet et lui enlève une vie"""
    chevauchement = Zone_jeux.find_overlapping(objet.x0, objet.y0, objet.x1, objet.y1)
    if len(chevauchement) > 2:
        objet.vie -= 1
        return True
    return False

    

# création de la fenêtre graphique
mw = Tk()
score_aff = StringVar()
score_aff.set("score: 0")
vie_aff = StringVar()
vie_aff.set("vie: 3")
mw.title('Bretons Invader')

# Création d'un widget Canvas (zone graphique)
Zone_jeux = Canvas(mw, width = largeur_mw, height = hauteur_mw, bg ='grey')
Zone_jeux.pack(side = 'top',padx =5, pady =5)
img_Mont = PhotoImage(file='Image/mont_saint_michel.png')
Zone_jeux.create_image(largeur_mw/2,hauteur_mw/2,image= img_Mont)
#Initialisationdes éléments graphiques
ilot0_rec = Zone_jeux.create_rectangle(ilot0.x0,ilot0.y0,ilot0.x1,ilot0.y1, fill = 'black')
ilot1_rec = Zone_jeux.create_rectangle(ilot1.x0,ilot1.y0,ilot1.x1,ilot1.y1, fill = 'black')
ilot2_rec = Zone_jeux.create_rectangle(ilot2.x0,ilot2.y0,ilot2.x1,ilot2.y1, fill = 'black')
ilot3_rec = Zone_jeux.create_rectangle(ilot3.x0,ilot3.y0,ilot3.x1,ilot3.y1, fill = 'black')
img_alien = PhotoImage(file='Image/drapeau_breton.png')
alien0_rec = Zone_jeux.create_image(alien0.x,alien0.y,image= img_alien)
alien1_rec = Zone_jeux.create_image(alien1.x,alien1.y,image= img_alien)
alien2_rec = Zone_jeux.create_image(alien2.x,alien2.y,image= img_alien)
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