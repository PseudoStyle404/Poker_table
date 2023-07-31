import random
import class_poker
import Jeux
import force_score

# INITIALISATION GAME
nb_joueurs=6
Stack_init=5000
SB=100
BB=200
min_raise=BB
nb_dealer=random.randint(0, nb_joueurs-1)

Tables_1=class_poker.class_table()
Tables_1.min_raise=BB
Tables_1.dealer=nb_dealer

Joueurs = [class_poker.class_joueurs(True, 0, [Stack_init, 0], ["Xx", "Xx"], 0, [0]) for i in range(1, nb_joueurs+1)]
Joueurs_dico = {}
for i in range(len(Joueurs)):
    nom = "J" + str(i+1)
    Joueurs_dico[nom] = Joueurs[i]


# DEMMARRE un JEUX et TIRE 2 + 5 CARTES avec N JOUEUR
games = Jeux.games_init(nb_joueurs)  # creation de toutes les cartes
Cartes_Joueurs = games[0]  # liste des mains des joueurs
flop=games[1]  # flop
# flop=["Ap", "9p", "7p"]
turn=games[2]  # turn
# turn=["Dp"]
river=games[3]  # river
Board = flop + turn + river   # toutes les cartes commune aux joueur

classement_final=None


def distrib_cartes():
    global games
    global Cartes_Joueurs
    global flop
    global turn
    global river
    global Board
    global classement_final
    Tables_1.dealer=(Tables_1.dealer+1) % nb_joueurs

    games = Jeux.games_init(nb_joueurs)  # creation de toutes les cartes
    Cartes_Joueurs = games[0]  # liste des mains des joueurs
    flop = games[1]  # flop
    turn = games[2]  # turn
    river = games[3]  # river
    Board = flop + turn + river  # toutes les cartes commune aux joueur

    # AFFECTATION DES MAINS AUX JOUEURS
    # Cartes_Joueurs[1]=["8p", "Rp"]
    # Cartes_Joueurs[2]=["Jp", "Tp"]
    # Cartes_Joueurs[3]=["2p", "3p"]

    for i in range(nb_joueurs):
        Joueurs[i].cartes = Cartes_Joueurs[i]


    # AFFECTATION SCORE FORCE 1 DES JOUEUR
    for i in range(nb_joueurs):
        # on range dans le dictionary clef Jx,la force du joueur = (sa main , le Board)
        Joueurs[i].force1 = force_score.niveau_main(Joueurs[i].cartes, Board)

    #  AFFECTATION SCORE FORCE 2 DES JOUEUR
    for i in range(nb_joueurs):
        #  on range dans le dictionary clef Jx,la force du joueur = (sa main , le Board)
        Joueurs[i].force2 = force_score.niveau_main2(Joueurs[i].cartes, Board, Joueurs[i].force1)

    classement_final= force_score.classement_final(Joueurs_dico, nb_joueurs)

    Joueurs[(Tables_1.dealer+1) % nb_joueurs].stack[0]-=SB  # On retire la SB à D +1
    Joueurs[(Tables_1.dealer+1) % nb_joueurs].stack[1]+=SB
    Joueurs[(Tables_1.dealer+2) % nb_joueurs].stack[0]-=BB  # On retire la BB à D +2
    Joueurs[(Tables_1.dealer+2) % nb_joueurs].stack[1]+=BB
    Tables_1.pot= SB + BB
    Tables_1.current_player=(Tables_1.dealer+3) % nb_joueurs   # integer pour numero du joueur ex : 1 a 6
    # fin des blind
    return


distrib_cartes()
