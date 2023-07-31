import class_poker
import initialisation


def niveau_main(Main, Board):
    Hauteur=check_hauteur(Main, Board)
    Couleur=check_couleur(Main, Board)
    # [2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 3] X 13 (deux as 3 deux et 8 et 9)
    # [4, 2, 1, 0] X 4 (4 coeur, 2 carreau, 1 pique 0 trefle
    lvl=0
    for i in range(13):  # i ittere tout les multiple de carte
        if Hauteur[i]==2:
            if lvl<1:
                lvl=1
            for j in range(13):
                if j!=i:
                    if Hauteur[j]==2:
                        if lvl<2:
                            lvl=2
        if Hauteur[i]==3:
            if lvl<3:
                lvl=3
            for j in range(13):
                if j!=i:
                    if Hauteur[j]==2 or Hauteur[j]==3:
                        if lvl<6:
                            lvl=6
        if Hauteur[i]==4:
            lvl=7

    for i in range(4):
        if Couleur[i]>=5:
            if lvl<5:
                lvl=5

    for i in range(8):
        if Hauteur[i]>0 and Hauteur[i+1]>0 and Hauteur[i+2]>0 and Hauteur[i+3]>0 and Hauteur[i+4]>0:
            if lvl<4:
                lvl=4
    return lvl


def niveau_main2(Main, Board, lvl1=0):
    Hauteur=check_hauteur(Main, Board)
    Couleur=check_couleur(Main, Board)
    # [2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 3] X 13 (deux as 3 deux et 8 et 9)
    # [4, 2, 1, 0] X 4 (4 coeur, 2 carreau, 1 pique 0 trefle

    lvl2=[]
    memo1 = None
    memo2 = None
    color = None
    count=0
    if lvl1==0:
        for i in range(13):
            if Hauteur[i]>0 and count<5:
                lvl2.append(12-i)
                count+=1
    if lvl1==1:
        for i in range(13):  # on cherche la paire
            if Hauteur[i]==2 and count<4:
                lvl2.append(12-i)
                memo1=i
                count+=1
        for i in range(13):  # on cherche les 3 autre hauteur
            if memo1!=i:
                if Hauteur[i]>0 and count<4:
                    lvl2.append(12-i)
                    count+=1
    if lvl1==2:
        for i in range(13):  # on cherche la paire 1
            if Hauteur[i]==2 and count<1:
                lvl2.append(12-i)
                memo1=i
                count+=1
        for i in range(13):  # on la deuxiemme paire
            if memo1!=i:
                if Hauteur[i] == 2 and count < 3:
                    lvl2.append(12 - i)
                    memo2 = i
                    count += 1
        for i in range(13):  # on cherche la hauteur
            if memo1!=i and memo2!=i:
                if Hauteur[i]>0 and count<3:
                    lvl2.append(12-i)
                    count+=1
    if lvl1==3:
        for i in range(13):  # on cherche le brelan
            if Hauteur[i]==3 and count<1:
                lvl2.append(12-i)
                memo1=i
                count+=1
        for i in range(13):  # on cherche les 2 autre hauteur
            if memo1!=i:
                if Hauteur[i]>0 and count<3:
                    lvl2.append(12-i)
                    count+=1
    if lvl1==4:
        for i in range(13-4):  # on cherche le brelan
            if Hauteur[i]>0 and Hauteur[i+1]>0 and Hauteur[i+2]>0 and Hauteur[i+3]>0 and Hauteur[i+4]>0 and count<1:
                lvl2.append(12-i)
                count+=1
    if lvl1==5:
        Liste_carte=Main+Board  # L = carte en jeux
        for j in range(4):
            if Couleur[j]>4:
                color=class_poker.class_CST.Couleur[j]  # color =c a, p, t

        lvl2=[]
        for i in range(13):
            # creation liste des plus haute carte present (de 2 a 14)
            if Hauteur[i]>0:
                if class_poker.class_CST.Hauteur[i]+color in Liste_carte:
                    lvl2.append(12-i)
        lvl2=lvl2[:5]

    if lvl1==6:
        for i in range(13):  # on cherche le brelan
            if Hauteur[i]==3 and count<1:
                lvl2.append(12-i)
                memo1=i
                count+=1
        for i in range(13):  # on cherche la paire
            if memo1!=i:
                if Hauteur[i]>=2 and count<2:
                    lvl2.append(12-i)
                    count+=1
    if lvl1==7:
        for i in range(13):  # on cherche le carre
            if Hauteur[i]==4 and count<1:
                lvl2.append(12-i)
                memo1=i
                count+=1
        for i in range(13):  # on cherche la hauteur
            if memo1!=i:
                if Hauteur[i]>0 and count<2:
                    lvl2.append(12-i)
                    count+=1

    for i in range(len(lvl2)):
        lvl2[i]+=2
    return lvl2


def check_hauteur(Main, Board):
    # fait uniquement pour 2 cartes
    force = [0] * len(class_poker.class_CST.Hauteur)
    cartes = Main + Board
    for i in range(len(cartes)):
        for j in range(len(class_poker.class_CST.Hauteur)):
            if cartes[i][0] == class_poker.class_CST.Hauteur[j]:
                force[j] += 1
    return force


def check_couleur(Main, Board):
    # fait uniquement pour 2 cartes
    force = [0] * len(class_poker.class_CST.Couleur)
    cartes = Main + Board
    for i in range(len(cartes)):
        for j in range(len(class_poker.class_CST.Couleur)):
            if cartes[i][1] == class_poker.class_CST.Couleur[j]:
                force[j] += 1
    return force


def classement_final(Joueurs_dico, nb_joueurs):
    Classement=["J1"]
    for i in range(1, nb_joueurs):
        joueur_OK=False
        for j in range(len(Classement)):
            # comparaison de deux joueur, si plus fort on insère dans le classement
            if force_joueur(Joueurs_dico["J" + str(i + 1)], Joueurs_dico[Classement[j]]) and not joueur_OK:
                Classement.insert(j, "J" + str(i + 1))
                joueur_OK = True

        if not joueur_OK:  # pas assez fort, a la fin !
            Classement.append("J" + str(i + 1))
    return Classement


def force_joueur(joueur1, joueur2):
    f1_J1=joueur1.force1  # Integer
    f2_J1=joueur1.force2  # liste integer
    f1_J2=joueur2.force1  # Integer
    f2_J2=joueur2.force2  # liste integer

    if f1_J1 > f1_J2:
        return True
    if f1_J1 < f1_J2:
        return False


    if f1_J1 == f1_J2:
        if len(f2_J1)!=len(f2_J2):
            raise ValueError("Ceci est une erreur de valeur.")

        for i in range(len(f2_J1)):
            if f2_J1[i]>f2_J2[i]:
                return True
            if f2_J1[i]<f2_J2[i]:
                return False
