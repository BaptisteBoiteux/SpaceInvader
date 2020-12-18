#Header 
"""
quoi :Programme principal du projet Space Invador
qui : Baptiste Boiteux
quand : 18/12/20
repertoire git : https://github.com/BaptisteBoiteux/SpaceInvader.git
"""

#Importation des bibilothèques
import SpaceFonction as f
from tkinter import Tk, Label, Button, Canvas, Entry, StringVar,messagebox, PhotoImage,filedialog

# création de la fenêtre graphique
mw = Tk()
mw.title('Pendu')
# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(mw, width = Largeur, height =Hauteur, bg ='grey')
Canevas.pack(side = 'right',padx =5, pady =5)
# Création d'un widget Label (score)
Label1 = Label(mw,)
Label1.pack(side = 'bottom', padx = 5, pady = 5)
# Création d'un widget Button (bouton Commencer)
Button(mw, text ='Commencer' ).pack(side='left',padx=5,pady=5)
# Création d'un widget Button (bouton Quitter)
Button(mw, text ='Quitter' ,command = mw.destroy).pack(side='left',padx=5,pady=5)
#lancement du gestionnaire d'événements
mw.mainloop()