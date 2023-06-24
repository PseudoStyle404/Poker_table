import random
import tkinter as tk
import datetime
import action_joueur
import graphique
from action_joueur import raise_play
import class_poker
import Jeux
# import force_score
# from PIL import Image, ImageTK

t1=datetime.datetime.now()
# INITIALISATION GAME
nb_joueurs=6
Stack_init=10000
SB=100
BB=200
min_raise=BB
nb_dealer=random.randint(0, nb_joueurs-1)

Tables_1=class_poker.class_table()
Tables_1.min_raise=BB

Joueurs = [class_poker.class_joueurs(True, 0, [Stack_init, 0], ["Xx", "Xx"], 0, 0) for i in range(1, nb_joueurs+1)]
Joueurs_dico = {}
for i in range(len(Joueurs)):
    nom = "J" + str(i+1)
    Joueurs_dico[nom] = Joueurs[i]

def ajuster_conteneurs(event):
    largeur_fenetre = event.width
    hauteur_fenetre = event.height

    #  Calcule la taille des conteneurs en fonction de la taille de la fenêtre
    taille_conteneur = largeur_fenetre
    hauteur_conteneur = hauteur_fenetre

    #  Ajuste la taille des conteneurs
    conteneur1.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur2.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur3.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur4.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur5.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur6.configure(width=taille_conteneur, height=hauteur_conteneur)




action_joueur.start_game()

Table_Poker = tk.Tk()
Table_Poker.title("Table_Poker")
Table_Poker.geometry('800x500')
Table_Poker["bg"]='green'


#  Attache l'événement de redimensionnement à la fonction ajuster_conteneurs
Table_Poker.bind("<Configure>", ajuster_conteneurs)

graphique.window(Table_Poker)
