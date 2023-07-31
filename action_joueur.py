import time

import initialisation

nb_joueurs= initialisation.nb_joueurs
Joueurs=initialisation.Joueurs
Tables_1=initialisation.Tables_1
Board=initialisation.Board


def raise_play(MAJ_TOUT, mise_G):
    # Moment des mises
    bet = mise_G.get()
    count=1
    Joueur_prec = None
    while count<nb_joueurs:
        if Joueurs[Tables_1.current_player-count].in_game:
            Joueur_prec= Joueurs[Tables_1.current_player-count]
            break
        count+=1

    bet=int(bet)
    if Joueurs[Tables_1.current_player].stack[0]>=bet>=Tables_1.min_raise + Joueur_prec.stack[1]-\
            Joueurs[Tables_1.current_player].stack[1]:
        Joueurs[Tables_1.current_player].stack[0]-=bet
        Joueurs[Tables_1.current_player].stack[1]+=bet
        Tables_1.pot+=bet
        Tables_1.min_raise=Joueurs[Tables_1.current_player].stack[1]-Joueur_prec.stack[1]
        Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs  # on incremente numero joueurs
        Tables_1.check_ok=False
        Tables_1.check_count=0

    count=1
    while not Joueurs[Tables_1.current_player].in_game and count<nb_joueurs:
        Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs  # on incremente numero joueurs
        count+=1
    MAJ_TOUT()
    return


def call_play(MAJ_TOUT, MAJ_FLOP, MAJ_TURN, MAJ_RIVER, RAZ_BOARD):

    Joueur_prec = None
    END_TURN=None
    count = 1
    while count < nb_joueurs:
        if Joueurs[Tables_1.current_player - count].in_game:
            Joueur_prec = Joueurs[Tables_1.current_player - count]
            break
        count += 1

    if Tables_1.check_ok:
        Tables_1.check_count+=1
        if Tables_1.check_count==player_left(Joueurs):
            END_TURN=True
        Tables_1.current_player = (Tables_1.current_player + 1) % nb_joueurs  # on incremente numero joueurs
        count = 1
        while not Joueurs[Tables_1.current_player].in_game and count < nb_joueurs:
            Tables_1.current_player = (Tables_1.current_player + 1) % nb_joueurs  # on incremente numero joueurs
            count += 1

    else:
        diff_call = Joueur_prec.stack[1] - Joueurs[Tables_1.current_player].stack[1]
        Joueurs[Tables_1.current_player].stack[0] -= diff_call
        Joueurs[Tables_1.current_player].stack[1] += diff_call
        Tables_1.pot += diff_call

        Tables_1.current_player = (Tables_1.current_player + 1) % nb_joueurs  # on incremente numero joueurs
        count=1
        while not Joueurs[Tables_1.current_player].in_game and count<nb_joueurs:
            Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs  # on incremente numero joueurs
            count+=1
    if not Tables_1.check_ok:
        memo= Joueur_prec.stack[1]
        test_call=True
        for i in Joueurs:
            if i.stack[1]!=memo and i.in_game:
                test_call=False
        if test_call:
            END_TURN=True

    if END_TURN:
        reset_end_turn()
        print(Tables_1.temps_jeux)
        Tables_1.check_ok=True
        Tables_1.check_count=0
        if Tables_1.temps_jeux=="flop":
            MAJ_FLOP(Board)
            Tables_1.temps_jeux = "turn"
        elif Tables_1.temps_jeux=="turn":
            MAJ_TURN(Board)
            Tables_1.temps_jeux = "river"
        elif Tables_1.temps_jeux=="river":
            MAJ_RIVER(Board)
            Tables_1.temps_jeux = "end"
        elif Tables_1.temps_jeux=="end":
            disribue_pot()
            time.sleep(2)
            RAZ_BOARD()
            reset_end_main()
            initialisation.distrib_cartes()

    MAJ_TOUT()
    return


def fold_play(MAJ_TOUT, MAJ_FLOP, MAJ_TURN, MAJ_RIVER, RAZ_BOARD):
    Joueur_prec = None
    count=1
    while count < nb_joueurs:
        if Joueurs[Tables_1.current_player - count].in_game:
            Joueur_prec = Joueurs[Tables_1.current_player - count]
            break
        count += 1

    Joueurs[Tables_1.current_player].in_game = False
    Joueurs[Tables_1.current_player].cartes = ["Xx", "Xx"]
    Tables_1.current_player = (Tables_1.current_player + 1) % nb_joueurs  # on incremente numero joueurs

    count=1
    END_TURN=None

    while not Joueurs[Tables_1.current_player].in_game and count<nb_joueurs:
        Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs  # on incremente numero joueurs
        count+=1

    if player_left(Joueurs)==1:
        Tables_1.temps_jeux="end"
    if not Tables_1.check_ok:
        memo= Joueur_prec.stack[1]
        test_call=True
        for i in Joueurs:
            if i.stack[1]!=memo and i.in_game:
                test_call=False
        if test_call:
            END_TURN=True

    if END_TURN:
        reset_end_turn()
        Tables_1.check_ok=True
        Tables_1.check_count=0
        if Tables_1.temps_jeux=="flop":
            MAJ_FLOP(Board)
            Tables_1.temps_jeux = "turn"
        elif Tables_1.temps_jeux=="turn":
            MAJ_TURN(Board)
            Tables_1.temps_jeux = "river"
        elif Tables_1.temps_jeux=="river":
            MAJ_RIVER(Board)

    if Tables_1.temps_jeux=="end":
        disribue_pot()
        time.sleep(2)
        RAZ_BOARD()
        reset_end_main()
        initialisation.distrib_cartes()

    MAJ_TOUT()
    return


def player_left(liste_joueurs):
    nb_left=0
    for i in liste_joueurs:
        if i.in_game == 1:
            nb_left+=1
    return nb_left


def reset_end_turn():
    Tables_1.min_raise=initialisation.BB
    Tables_1.check_ok=False
    for i in Joueurs:
        i.stack[1]=0
        i.force1=0
        i.force2=[]

    Tables_1.current_player=(Tables_1.dealer+1) % nb_joueurs
    while not Joueurs[Tables_1.current_player].in_game:
        Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs


def reset_end_main():
    Tables_1.min_raise=initialisation.BB
    Tables_1.check_ok=False
    Tables_1.check_count=0
    Tables_1.temps_jeux = "flop"
    for i in Joueurs:
        i.stack[1]=0
        i.force1=0
        i.force2=[]
        i.in_game=True
    return


def disribue_pot():
    classement=initialisation.classement_final
    Joueurs_dico=initialisation.Joueurs_dico
    print(classement)
    for i in classement:
        if Joueurs_dico[i].in_game:
            Joueurs_dico[i].stack[0] += Tables_1.pot
            Tables_1.pot=0
    pass
