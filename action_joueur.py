import initialisation

nb_joueurs= initialisation.nb_joueurs
Joueurs=initialisation.Joueurs
Tables_1=initialisation.Tables_1


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
    if bet>=Tables_1.min_raise + Joueur_prec.stack[1]-Joueurs[Tables_1.current_player].stack[1]:
        Joueurs[Tables_1.current_player].stack[0]-=bet
        Joueurs[Tables_1.current_player].stack[1]+=bet
        Tables_1.pot+=bet
        Tables_1.min_raise=Joueurs[Tables_1.current_player].stack[1]-Joueur_prec.stack[1]
        Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs  # on incremente numero joueurs

    while not Joueurs[Tables_1.current_player].in_game:
        Tables_1.current_player=(Tables_1.current_player+1) % nb_joueurs  # on incremente numero joueurs

    MAJ_TOUT()
    return


def call_play(MAJ_TOUT):
    Joueur_prec = None
    count=1
    while count < nb_joueurs:
        if Joueurs[Tables_1.current_player - count].in_game:
            Joueur_prec = Joueurs[Tables_1.current_player - count]
            break
        count += 1

    diff_call = Joueur_prec.stack[1] - Joueurs[Tables_1.current_player].stack[1]
    Joueurs[Tables_1.current_player].stack[0] -= diff_call
    Joueurs[Tables_1.current_player].stack[1] += diff_call
    Tables_1.pot += diff_call
    Tables_1.current_player = (Tables_1.current_player + 1) % nb_joueurs  # on incremente numero joueurs

    MAJ_TOUT()
    return


def fold_play(MAJ_TOUT):

    Joueurs[Tables_1.current_player].in_game = False
    Joueurs[Tables_1.current_player].cartes = ["Xx", "Xx"]
    Tables_1.current_player = (Tables_1.current_player + 1) % nb_joueurs  # on incremente numero joueurs

    MAJ_TOUT()
    return
