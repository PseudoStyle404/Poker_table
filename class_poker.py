import tkinter as tk

class class_CST:
    Hauteur = ["A", "R", "D", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    Couleur = ["c", "a", "p", "t"]
    Jeux_init=[]
    for i in Hauteur:
        for j in Couleur:
            Jeux_init.append(i+j)


class class_table:
    def __init__(self):
        self.pot=0
        self.current_player=0
        self.min_raise=0

    def __str__(self):
        return f"in_game: {self.pot}, position: {self.current_player}, stack: {self.min_raise}"

# Joueur_data = [True, 0, [Stack_init,0], ["Xx", "Xx"], 0, 0]


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
        return f"in_game: {self.in_game}, position: {self.position}, stack: {self.stack}, cartes: {self.cartes}," \
               f" force1: {self.force1}, force2: {self.force2}"

# Joueur_data = [True, 0, [Stack_init,0], ["Xx", "Xx"], 0, 0]

