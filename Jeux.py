import copy
import random
import class_poker


def couleur_carte(carte):
    if carte[1]=="p":
        return "#000000"  # N
    if carte[1]=="c":
        return "#FF0000"  # R
    if carte[1]=="t":
        return "#008000"  # V
    if carte[1]=="a":
        return "#0000FF"  # B
    return "#000000"



def games_init(n):
    jeux = copy.copy(class_poker.class_CST.Jeux_init)
    random.shuffle(jeux)
    nb_joueur = n
    cartes_joueurs = []
    for variable in range(nb_joueur):
        carte_1 = distrib(jeux)
        carte_2 = distrib(jeux)
        cartes_joueurs.append([carte_1, carte_2])
    flop = [distrib(jeux), distrib(jeux), distrib(jeux)]
    turn = [distrib(jeux)]
    river = [distrib(jeux)]

    return cartes_joueurs, flop, turn, river


def distrib(cartes):
    valeur = cartes[0]
    cartes.pop(0)
    return valeur
