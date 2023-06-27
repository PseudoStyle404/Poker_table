import random
import class_poker
import Jeux

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

# for i in range(1): joue une main de POKER
# DEMMARRE un JEUX et TIRE 2 + 5 CARTES avec N JOUEUR
games = Jeux.games_init(nb_joueurs)  # creation de toutes les cartes
Cartes_Joueurs = games[0]  # liste des mains des joueurs
flop=games[1]  # flop
turn=games[2]  # turn
river=games[3]  # river
Board = flop + turn + river   # toutes les cartes commune aux joueur

# AFFECTATION DES MAINS AUX JOUEURS
for i in range(nb_joueurs):
    Joueurs[i].cartes = Cartes_Joueurs[i]

# AFFECTATION SCORE FORCE 1 DES JOUEUR
# for i in range(nb_joueurs):
    # on range dans le dictionary clef Jx,la force du joueur = (sa main , le Board)
    # Joueurs[i].force1 = force_score.niveau_main(Joueurs[i].cartes,Board)

#  AFFECTATION SCORE FORCE 2 DES JOUEUR
# for i in range(nb_joueurs):
    #  on range dans le dictionary clef Jx,la force du joueur = (sa main , le Board)
    # Joueurs[i].force2 = force_score.niveau_main2(Joueurs[i].cartes, Board,Joueurs[i].force1)
    # classement_final= force_score.classement_final(Joueurs_dico,nb_joueurs)
    # LES JEUX SONT FAIT ['J1', 'J4', 'J3', 'J2', 'J6', 'J5']

Joueurs[(nb_dealer+1) % nb_joueurs].stack[0]-=SB  # On retire la SB à D +1
Joueurs[(nb_dealer+1) % nb_joueurs].stack[1]+=SB
Joueurs[(nb_dealer+2) % nb_joueurs].stack[0]-=BB  # On retire la BB à D +2
Joueurs[(nb_dealer+2) % nb_joueurs].stack[1]+=BB
Tables_1.pot= SB + BB
Tables_1.current_player=(nb_dealer+3) % nb_joueurs   # integer pour numero du joueur ex : 1 a 6
# fin des blind
