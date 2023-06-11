import random
import time
import tkinter as tk
import datetime
import Jeux
#import force_score
#from PIL import Image, ImageTK

t1=datetime.datetime.now()

#iNITIALISATION GAME
nb_joueurs=6
Stack_init=10000
SB=100
BB=200
min_raise=BB
nb_dealer=random.randint(0,nb_joueurs-1)

Tables_1=Jeux.class_table()
Tables_1.min_raise=BB

Joueurs = [Jeux.class_joueurs(True, 0, [Stack_init,0], ["Xx", "Xx"], 0, 0) for i in range(1, nb_joueurs+1)]
Joueurs_dico = {}
for i in range(len(Joueurs)):
    nom = "J" + str(i+1)
    Joueurs_dico[nom] = Joueurs[i]

def main_de_poker():
#for i in range(1): #joue une main de POKER
    #DEMMARRE un JEUX et TIRE 2 + 5 CARTES avec N JOUEUR
    games = Jeux.games_init(nb_joueurs) #creation de toutes les cartes
    Cartes_Joueurs = games[0]#liste des mains des joueurs
    flop=games[1]#flop
    turn=games[2]#turn
    river=games[3]#river
    Board = flop + turn + river #toutes les cartes commune aux joueur

    #AFFECTATION DES MAINS AUX JOUEURS
    for i in range(nb_joueurs):
        Joueurs[i].cartes = Cartes_Joueurs[i]

    #AFFECTATION SCORE FORCE 1 DES JOUEUR
    for i in range(nb_joueurs):
        nothing=0
        #on range dans le dictionary clef Jx,la force du joueur = (sa main , le Board)
        #Joueurs[i].force1 = force_score.niveau_main(Joueurs[i].cartes,Board)

    # AFFECTATION SCORE FORCE 2 DES JOUEUR
    for i in range(nb_joueurs):
        nothing=0
        # on range dans le dictionary clef Jx,la force du joueur = (sa main , le Board)
        #Joueurs[i].force2 = force_score.niveau_main2(Joueurs[i].cartes, Board,Joueurs[i].force1)
    #classement_final= force_score.classement_final(Joueurs_dico,nb_joueurs)
    #LES JEUX SONT FAIT ['J1', 'J4', 'J3', 'J2', 'J6', 'J5']
    Joueurs[(nb_dealer+1)%nb_joueurs].stack[0]-=SB# On retire la SB à D +1
    Joueurs[(nb_dealer+1)%nb_joueurs].stack[1]+=SB
    Joueurs[(nb_dealer+2)%nb_joueurs].stack[0]-=BB# On retire la BB à D +2
    Joueurs[(nb_dealer+2)%nb_joueurs].stack[1]+=BB
    Tables_1.pot= SB + BB
    Tables_1.current_player=(nb_dealer+3)%nb_joueurs #integer pour numero du joueur ex : 1 a 6
    #fin des blind

    tour_de_mise()

    MAJ_TOUT()
    if True:
        #print("-----------------------------")
        #for i in range(nb_joueurs):
        #    #if Joueurs["J" + str(i + 1)][4]==5:
        #    print("J" + str(i + 1),Joueurs[i])
        print("-----------------------------")
        print(Board[0]+"-"+Board[1]+"-"+Board[2]+"-"+Board[3]+"-"+Board[4])


def tour_de_mise():
    #Moment des mises
    for ever in range(1):
        bet = mise_G.get()
        time.sleep(0.3)
        count=1
        while count<nb_joueurs:
            if Joueurs[Tables_1.current_player-count].in_game==True:
                Joueur_prec= Joueurs[Tables_1.current_player-count]
                break
            count+=1
        if bet=="f":
            Joueurs[Tables_1.current_player].in_game=False
            Joueurs[Tables_1.current_player].cartes=["Xx","Xx"]
            Tables_1.current_player=(Tables_1.current_player+1)%nb_joueurs#on incremente numero joueurs
        elif bet=="c":
            diff_call=Joueur_prec.stack[1]-Joueurs[Tables_1.current_player].stack[1]
            Joueurs[Tables_1.current_player].stack[0]-=diff_call
            Joueurs[Tables_1.current_player].stack[1]+=diff_call
            Tables_1.pot+=diff_call
            Tables_1.current_player=(Tables_1.current_player+1)%nb_joueurs#on incremente numero joueurs
        elif bet!="":
            bet=int(bet)
            if bet>=Tables_1.min_raise + Joueur_prec.stack[1]-Joueurs[Tables_1.current_player].stack[1]:
                Joueurs[Tables_1.current_player].stack[0]-=bet
                Joueurs[Tables_1.current_player].stack[1]+=bet
                Tables_1.pot+=bet
                Tables_1.min_raise=Joueurs[Tables_1.current_player].stack[1]-Joueur_prec.stack[1]
                Tables_1.current_player=(Tables_1.current_player+1)%nb_joueurs#on incremente numero joueurs

        while Joueurs[Tables_1.current_player].in_game==False:
            Tables_1.current_player=(Tables_1.current_player+1)%nb_joueurs#on incremente numero joueurs

        MAJ_TOUT()
    return

Table_Poker = tk.Tk()
Table_Poker.title("Table_Poker")
Table_Poker.geometry ( '800x500' )
Table_Poker["bg"]='green'

Lt_pot_total = tk.StringVar(Table_Poker)
Lt_current_player = tk.StringVar(Table_Poker)
Lt_money_J1 = tk.StringVar(Table_Poker)
Lt_money_J2 = tk.StringVar(Table_Poker)
Lt_money_J3 = tk.StringVar(Table_Poker)
Lt_money_J4 = tk.StringVar(Table_Poker)
Lt_money_J5 = tk.StringVar(Table_Poker)
Lt_money_J6 = tk.StringVar(Table_Poker)

Lt_money2_J1 = tk.StringVar(Table_Poker)
Lt_money2_J2 = tk.StringVar(Table_Poker)
Lt_money2_J3 = tk.StringVar(Table_Poker)
Lt_money2_J4 = tk.StringVar(Table_Poker)
Lt_money2_J5 = tk.StringVar(Table_Poker)
Lt_money2_J6 = tk.StringVar(Table_Poker)

Lt_couleur_variable = tk.StringVar(Table_Poker)

Lt_J1_carte1 = tk.StringVar(Table_Poker)
Lt_J1_carte2 = tk.StringVar(Table_Poker)
Lt_J2_carte1 = tk.StringVar(Table_Poker)
Lt_J2_carte2 = tk.StringVar(Table_Poker)
Lt_J3_carte1 = tk.StringVar(Table_Poker)
Lt_J3_carte2 = tk.StringVar(Table_Poker)
Lt_J4_carte1 = tk.StringVar(Table_Poker)
Lt_J4_carte2 = tk.StringVar(Table_Poker)
Lt_J5_carte1 = tk.StringVar(Table_Poker)
Lt_J5_carte2 = tk.StringVar(Table_Poker)
Lt_J6_carte1 = tk.StringVar(Table_Poker)
Lt_J6_carte2 = tk.StringVar(Table_Poker)




def ajuster_conteneurs(event):
    largeur_fenetre = event.width
    hauteur_fenetre = event.height

    # Calcule la taille des conteneurs en fonction de la taille de la fenêtre
    taille_conteneur = largeur_fenetre // 3
    hauteur_conteneur = hauteur_fenetre // 2

    # Ajuste la taille des conteneurs
    conteneur1.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur2.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur3.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur4.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur5.configure(width=taille_conteneur, height=hauteur_conteneur)
    conteneur6.configure(width=taille_conteneur, height=hauteur_conteneur)


# Attache l'événement de redimensionnement à la fonction ajuster_conteneurs
Table_Poker.bind("<Configure>", ajuster_conteneurs)

# Création des conteneurs
conteneur1 = tk.Frame(Table_Poker, bg="red", highlightthickness=0.2)
conteneur1.grid(row=1, column=1, sticky="nsew")
conteneur1.pack_propagate(False)

conteneur2 = tk.Frame(Table_Poker, bg="green", highlightthickness=0.2)
conteneur2.grid(row=1, column=0, sticky="nsew")
conteneur2.pack_propagate(False)

conteneur3 = tk.Frame(Table_Poker, bg="blue", highlightthickness=0.2)
conteneur3.grid(row=0, column=0, sticky="nsew")
conteneur3.pack_propagate(False)

conteneur4 = tk.Frame(Table_Poker, bg="yellow", highlightthickness=0.2)
conteneur4.grid(row=0, column=1, sticky="nsew")
conteneur4.pack_propagate(False)

conteneur5 = tk.Frame(Table_Poker, bg="orange", highlightthickness=0.2)
conteneur5.grid(row=0, column=2, sticky="nsew")
conteneur5.pack_propagate(False)

conteneur6 = tk.Frame(Table_Poker, bg="purple", highlightthickness=0.2)
conteneur6.grid(row=1, column=2, sticky="nsew")
conteneur6.pack_propagate(False)

conteneur_middle = tk.Frame(Table_Poker, bg="white")
conteneur_middle.place(relx=0.5,rely=0.4, width=120,height=60, anchor=tk.CENTER)

#backgroud_image=Image.open("/table_de_poker.jpg")
#backgroud_image=backgroud_image.resize((300,300))
#backgroud_image_tk= ImageTk.PhotoImage(backgroud_image)

#Lt_backgroud=tk.label(Table_Poker,backgroud_image_tk)
#Lt_backgroud.pack()


# Configuration des options de mise en page pour les conteneurs
Table_Poker.grid_rowconfigure(0, weight=1)
Table_Poker.grid_rowconfigure(1, weight=1)
Table_Poker.grid_columnconfigure(0, weight=1)
Table_Poker.grid_columnconfigure(1, weight=1)
Table_Poker.grid_columnconfigure(2, weight=1)

# Boucle principale de la fenêtre


L_pot_total = tk.Label(conteneur_middle, textvariable=Lt_pot_total,font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1, relief="solid")
L_current_player = tk.Label(conteneur_middle, textvariable=Lt_current_player, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")
L_money_J1 = tk.Label(conteneur1, textvariable=Lt_money_J1, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")
L_money_J2 = tk.Label(conteneur2, textvariable=Lt_money_J2, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")
L_money_J3 = tk.Label(conteneur3, textvariable=Lt_money_J3, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")
L_money_J4 = tk.Label(conteneur4, textvariable=Lt_money_J4, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")
L_money_J5 = tk.Label(conteneur5, textvariable=Lt_money_J5, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")
L_money_J6 = tk.Label(conteneur6, textvariable=Lt_money_J6, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid")


L_money2_J1 = tk.Label(conteneur1, textvariable=Lt_money2_J1, font = ( "Arial Bold" , 12 ), fg='yellow', bg='black', borderwidth=1, relief="solid")
L_money2_J2 = tk.Label(conteneur2, textvariable=Lt_money2_J2, font = ( "Arial Bold" , 12 ), fg='yellow', bg='black', borderwidth=1, relief="solid")
L_money2_J3 = tk.Label(conteneur3, textvariable=Lt_money2_J3, font = ( "Arial Bold" , 12 ), fg='yellow', bg='black', borderwidth=1, relief="solid")
L_money2_J4 = tk.Label(conteneur4, textvariable=Lt_money2_J4, font = ( "Arial Bold" , 12 ), fg='yellow', bg='black', borderwidth=1, relief="solid")
L_money2_J5 = tk.Label(conteneur5, textvariable=Lt_money2_J5, font = ( "Arial Bold" , 12 ), fg='yellow', bg='black', borderwidth=1, relief="solid")
L_money2_J6 = tk.Label(conteneur6, textvariable=Lt_money2_J6, font = ( "Arial Bold" , 12 ), fg='yellow', bg='black', borderwidth=1, relief="solid")

mise_G = tk.Entry(conteneur1, font=("Arial", 20), bg="white")

#Cartes des joueurs
J1_carte1 = tk.Label(conteneur1, textvariable=Lt_J1_carte1, font = ( "Arial Bold" , 20 ), borderwidth=1, relief="solid", foreground="#000000")
J1_carte2 = tk.Label(conteneur1, textvariable=Lt_J1_carte2, font = ( "Arial Bold" , 20 ), borderwidth=1, relief="solid", foreground="#000000")

J2_carte1 = tk.Label(conteneur2, textvariable=Lt_J2_carte1, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")
J2_carte2 = tk.Label(conteneur2, textvariable=Lt_J2_carte2, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")

J3_carte1 = tk.Label(conteneur3, textvariable=Lt_J3_carte1, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")
J3_carte2 = tk.Label(conteneur3, textvariable=Lt_J3_carte2, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")

J4_carte1 = tk.Label(conteneur4, textvariable=Lt_J4_carte1, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")
J4_carte2 = tk.Label(conteneur4, textvariable=Lt_J4_carte2, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")

J5_carte1 = tk.Label(conteneur5, textvariable=Lt_J5_carte1, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")
J5_carte2 = tk.Label(conteneur5, textvariable=Lt_J5_carte2, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")

J6_carte1 = tk.Label(conteneur6, textvariable=Lt_J6_carte1, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")
J6_carte2 = tk.Label(conteneur6, textvariable=Lt_J6_carte2, font = ( "Arial Bold" , 15 ), borderwidth=1, relief="solid", foreground="#000000")

def MAJ_TOUT():
    #GRAPHIQUE MAJ
    Lt_pot_total.set(str(Tables_1.pot))
    Lt_current_player.set("J"+str(Tables_1.current_player+1))
    Lt_money_J1.set(str(Joueurs_dico["J1"].stack[0]))
    Lt_money_J2.set(str(Joueurs_dico["J2"].stack[0]))
    Lt_money_J3.set(str(Joueurs_dico["J3"].stack[0]))
    Lt_money_J4.set(str(Joueurs_dico["J4"].stack[0]))
    Lt_money_J5.set(str(Joueurs_dico["J5"].stack[0]))
    Lt_money_J6.set(str(Joueurs_dico["J6"].stack[0]))

    Lt_money2_J1.set(str(Joueurs_dico["J1"].stack[1]))
    Lt_money2_J2.set(str(Joueurs_dico["J2"].stack[1]))
    Lt_money2_J3.set(str(Joueurs_dico["J3"].stack[1]))
    Lt_money2_J4.set(str(Joueurs_dico["J4"].stack[1]))
    Lt_money2_J5.set(str(Joueurs_dico["J5"].stack[1]))
    Lt_money2_J6.set(str(Joueurs_dico["J6"].stack[1]))

    Lt_J1_carte1.set(str(Joueurs_dico["J1"].cartes[0]))
    Lt_J1_carte2.set(str(Joueurs_dico["J1"].cartes[1]))
    Lt_J2_carte1.set(str(Joueurs_dico["J2"].cartes[0]))
    Lt_J2_carte2.set(str(Joueurs_dico["J2"].cartes[1]))
    Lt_J3_carte1.set(str(Joueurs_dico["J3"].cartes[0]))
    Lt_J3_carte2.set(str(Joueurs_dico["J3"].cartes[1]))
    Lt_J4_carte1.set(str(Joueurs_dico["J4"].cartes[0]))
    Lt_J4_carte2.set(str(Joueurs_dico["J4"].cartes[1]))
    Lt_J5_carte1.set(str(Joueurs_dico["J5"].cartes[0]))
    Lt_J5_carte2.set(str(Joueurs_dico["J5"].cartes[1]))
    Lt_J6_carte1.set(str(Joueurs_dico["J6"].cartes[0]))
    Lt_J6_carte2.set(str(Joueurs_dico["J6"].cartes[1]))

    J1_carte1.config(fg=Jeux.couleur_carte(Joueurs_dico["J1"].cartes[0]))
    J1_carte2.config(fg=Jeux.couleur_carte(Joueurs_dico["J1"].cartes[1]))
    J2_carte1.config(fg=Jeux.couleur_carte(Joueurs_dico["J2"].cartes[0]))
    J2_carte2.config(fg=Jeux.couleur_carte(Joueurs_dico["J2"].cartes[1]))
    J3_carte1.config(fg=Jeux.couleur_carte(Joueurs_dico["J3"].cartes[0]))
    J3_carte2.config(fg=Jeux.couleur_carte(Joueurs_dico["J3"].cartes[1]))
    J4_carte1.config(fg=Jeux.couleur_carte(Joueurs_dico["J4"].cartes[0]))
    J4_carte2.config(fg=Jeux.couleur_carte(Joueurs_dico["J4"].cartes[1]))
    J5_carte1.config(fg=Jeux.couleur_carte(Joueurs_dico["J5"].cartes[0]))
    J5_carte2.config(fg=Jeux.couleur_carte(Joueurs_dico["J5"].cartes[1]))
    J6_carte1.config(fg=Jeux.couleur_carte(Joueurs_dico["J6"].cartes[0]))
    J6_carte2.config(fg=Jeux.couleur_carte(Joueurs_dico["J6"].cartes[1]))

    return
bouton_mise = tk.Button(conteneur1, text="MISE", bg="orange", fg="blue", command=tour_de_mise)
bouton_start = tk.Button(conteneur2, text="START", bg="orange", fg="blue", command=main_de_poker)
bouton_refresh = tk.Button(conteneur6, text="REFRESH", bg="orange", fg="blue", command=MAJ_TOUT)
bouton_fermer = tk.Button(conteneur6, text="FERMER", bg="orange", fg="blue", command=Table_Poker.destroy)


#Conteneur 1
J1_carte1.pack()
J1_carte2.pack()
L_money2_J1.pack()
L_money_J1.pack()
mise_G.pack(expand=1)
bouton_mise.pack(expand=1)

#Conteneur 2
J2_carte1.pack()
J2_carte2.pack()
L_money2_J2.pack()
L_money_J2.pack()
bouton_start.pack(expand=1)

#Conteneur 3
L_money_J3.pack()
L_money2_J3.pack()
J3_carte1.pack()
J3_carte2.pack()

#Conteneur 4
L_money_J4.pack()
L_money2_J4.pack()
J4_carte1.pack()
J4_carte2.pack()

#Conteneur 5
L_money_J5.pack()
L_money2_J5.pack()
J5_carte1.pack()
J5_carte2.pack()

#Conteneur 6
J6_carte1.pack()
J6_carte2.pack()
L_money2_J6.pack()
L_money_J6.pack()
bouton_refresh.pack(expand=1)
bouton_fermer.pack(expand=1)

#Conteneur middle
L_current_player.pack()
L_pot_total.pack()

Table_Poker.mainloop()
t2=datetime.datetime.now()
#print("TEMPS :", t2-t1)


