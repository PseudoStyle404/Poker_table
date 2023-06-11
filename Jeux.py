import copy
import random
# CONSTANTE
global Hauteur_CST
Hauteur_CST = ["A", "R", "D", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
global Couleur_CST
Couleur_CST = ["c", "a", "p", "t"]
global Jeux_init_CST
Jeux_init_CST = []
for i in Hauteur_CST:
    for j in Couleur_CST:
        Jeux_init_CST.append(i + j)
# CONSTANTE

class class_table:
    def __init__(self):
        self.pot=0
        self.current_player=0
        self.min_raise=0

    def __str__(self):
        return f"in_game: {self.pot}, position: {self.current_player}, stack: {self.min_raise}"

#Joueur_data = [True, 0, [Stack_init,0], ["Xx", "Xx"], 0, 0]


class class_joueurs:
    def __init__(self, in_game, position, stack, cartes, force1, force2):
        self.name="J"+str(position+1)
        self.in_game = in_game
        self.position = position
        self.stack = stack
        self.cartes = cartes
        self.force1 = force1
        self.force2 = force2

    def __str__(self):
        return f"in_game: {self.in_game}, position: {self.position}, stack: {self.stack}, cartes: {self.cartes}, force1: {self.force1}, force2: {self.force2}"

#Joueur_data = [True, 0, [Stack_init,0], ["Xx", "Xx"], 0, 0]


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
    jeux = copy.copy(Jeux_init_CST)
    random.shuffle(jeux)
    nb_joueur = n
    cartes_joueurs = []
    for i in range(nb_joueur):
        carte_1 = distrib(jeux)
        carte_2 = distrib(jeux)
        cartes_joueurs.append([carte_1, carte_2])
    flop = [distrib(jeux), distrib(jeux), distrib(jeux)]
    turn = [distrib(jeux)]
    river = [distrib(jeux)]

    return cartes_joueurs,flop,turn,river
def distrib(cartes):
    valeur = cartes[0]
    cartes.pop(0)
    return valeur
