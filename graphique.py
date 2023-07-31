import tkinter as tk
from PIL import ImageTk, Image

import Jeux
import initialisation
import action_joueur


# Fonction pour créer un conteneur avec des paramètres spécifiques
def create_container(parent, row, column, bg_color):
    container = tk.Frame(parent, bg=bg_color, highlightthickness=0.2)
    container.grid(row=row, column=column, sticky="nsew")
    container.grid_propagate(False)
    return container


def create_label(container, textvariable, font, fg, bg, borderwidth, relief, width=None, height=None):
    return tk.Label(container, textvariable=textvariable, font=font, fg=fg, bg=bg,
                    borderwidth=borderwidth, relief=relief, bd=2, width=width, height=height)


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


Joueurs_dico=initialisation.Joueurs_dico
Tables_1=initialisation.Tables_1

Table_Poker = tk.Tk()
Table_Poker.title("Table_Poker")
Table_Poker.geometry('1200x720')
Table_Poker["bg"]='green'


#  Attache l'événement de redimensionnement à la fonction ajuster_conteneurs
# Table_Poker.bind("<Configure>", ajuster_conteneurs)
string_vars = [
    tk.StringVar(Table_Poker) for _ in range(33)
]
(
    Lt_pot_total, Lt_boutton_dealer, Lt_current_player,
    Lt_money_J1, Lt_money_J2, Lt_money_J3, Lt_money_J4, Lt_money_J5, Lt_money_J6,
    Lt_money2_J1, Lt_money2_J2, Lt_money2_J3, Lt_money2_J4, Lt_money2_J5, Lt_money2_J6, Lt_couleur_variable,
    Lt_J1_carte1, Lt_J1_carte2,
    Lt_J2_carte1, Lt_J2_carte2,
    Lt_J3_carte1, Lt_J3_carte2,
    Lt_J4_carte1, Lt_J4_carte2,
    Lt_J5_carte1, Lt_J5_carte2,
    Lt_J6_carte1, Lt_J6_carte2,
    Lt_board_carte1, Lt_board_carte2,
    Lt_board_carte3, Lt_board_carte4,
    Lt_board_carte5
) = string_vars[:33]


conteneur1 = create_container(Table_Poker, 1, 1, "#008000")
conteneur2 = create_container(Table_Poker, 1, 0, "#6B8E23")
conteneur3 = create_container(Table_Poker, 0, 0, "#008000")
conteneur4 = create_container(Table_Poker, 0, 1, "#6B8E23")
conteneur5 = create_container(Table_Poker, 0, 2, "#008000")
conteneur6 = create_container(Table_Poker, 1, 2, "#6B8E23")

conteneur_J1 = tk.Frame(conteneur1, bg="#FF6F61")
conteneur_J2 = tk.Frame(conteneur2, bg="#8A6BBE")
conteneur_J3 = tk.Frame(conteneur3, bg="#F0E68C")
conteneur_J4 = tk.Frame(conteneur4, bg="#004C6D")
conteneur_J5 = tk.Frame(conteneur5, bg="#87CEEB")
conteneur_J6 = tk.Frame(conteneur6, bg="#00A878")

# backgroud_image=Image.open("/table_de_poker.jpg")
# backgroud_image=backgroud_image.resize((300,300))
# backgroud_image_tk= ImageTk.PhotoImage(backgroud_image)

# Lt_backgroud=tk.label(Table_Poker,backgroud_image_tk)
# Lt_backgroud.pack()

#  Configuration des options de mise en page pour les conteneurs
Table_Poker.grid_rowconfigure(0, weight=1)
Table_Poker.grid_rowconfigure(1, weight=1)
Table_Poker.grid_columnconfigure(0, weight=1)
Table_Poker.grid_columnconfigure(1, weight=1)
Table_Poker.grid_columnconfigure(2, weight=1)

conteneur_middle = tk.Frame(Table_Poker, bg="green")
conteneur_middle.place(relx=0.5, rely=0.4, width=120, height=65, anchor=tk.CENTER)

conteneur_middle_play = tk.Frame(Table_Poker, bg="#FFE4B5")
conteneur_middle_play.place(relx=0.5, rely=0.85, width=300, height=70, anchor=tk.CENTER)

conteneur_middle_board = tk.Frame(Table_Poker, bg="green")
conteneur_middle_board.place(relx=0.5, rely=0.25, width=204, height=50, anchor=tk.CENTER)

L_pot_total = create_label(conteneur_middle, Lt_pot_total, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")


L_boutton_dealer_J1 = tk.Label(conteneur1, text="D", font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1,
                               relief="solid")
L_boutton_dealer_J2 = tk.Label(conteneur2, text="D", font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1,
                               relief="solid")
L_boutton_dealer_J3 = tk.Label(conteneur3, text="D", font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1,
                               relief="solid")
L_boutton_dealer_J4 = tk.Label(conteneur4, text="D", font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1,
                               relief="solid")
L_boutton_dealer_J5 = tk.Label(conteneur5, text="D", font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1,
                               relief="solid")
L_boutton_dealer_J6 = tk.Label(conteneur6, text="D", font=("Arial Bold", 15), fg='yellow', bg='black', borderwidth=1,
                               relief="solid")

L_money_J1 = create_label(conteneur1, Lt_money_J1, ("Arial Bold", 20), None, "#C0C0C0", 1, "solid", width=8, height=2)
L_money_J2 = create_label(conteneur2, Lt_money_J2, ("Arial Bold", 20), None, "#C0C0C0", 1, "solid", width=8, height=2)
L_money_J3 = create_label(conteneur3, Lt_money_J3, ("Arial Bold", 20), None, "#C0C0C0", 1, "solid", width=8, height=2)
L_money_J4 = create_label(conteneur4, Lt_money_J4, ("Arial Bold", 20), None, "#C0C0C0", 1, "solid", width=8, height=2)
L_money_J5 = create_label(conteneur5, Lt_money_J5, ("Arial Bold", 20), None, "#C0C0C0", 1, "solid", width=8, height=2)
L_money_J6 = create_label(conteneur6, Lt_money_J6, ("Arial Bold", 20), None, "#C0C0C0", 1, "solid", width=8, height=2)

Liste_money_Jx=[L_money_J1, L_money_J2, L_money_J3, L_money_J4, L_money_J5, L_money_J6]

L_money2_J1 = create_label(conteneur_J1, Lt_money2_J1, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")
L_money2_J2 = create_label(conteneur_J2, Lt_money2_J2, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")
L_money2_J3 = create_label(conteneur_J3, Lt_money2_J3, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")
L_money2_J4 = create_label(conteneur_J4, Lt_money2_J4, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")
L_money2_J5 = create_label(conteneur_J5, Lt_money2_J5, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")
L_money2_J6 = create_label(conteneur_J6, Lt_money2_J6, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")


J1_carte1 = create_label(conteneur_J1, Lt_J1_carte1, ("Arial Bold", 25), None, None, 1, "solid")
J1_carte2 = create_label(conteneur_J1, Lt_J1_carte2, ("Arial Bold", 25), None, None, 1, "solid")
J2_carte1 = create_label(conteneur_J2, Lt_J2_carte1, ("Arial Bold", 25), None, None, 1, "solid")
J2_carte2 = create_label(conteneur_J2, Lt_J2_carte2, ("Arial Bold", 25), None, None, 1, "solid")
J3_carte1 = create_label(conteneur_J3, Lt_J3_carte1, ("Arial Bold", 25), None, None, 1, "solid")
J3_carte2 = create_label(conteneur_J3, Lt_J3_carte2, ("Arial Bold", 25), None, None, 1, "solid")
J4_carte1 = create_label(conteneur_J4, Lt_J4_carte1, ("Arial Bold", 25), None, None, 1, "solid")
J4_carte2 = create_label(conteneur_J4, Lt_J4_carte2, ("Arial Bold", 25), None, None, 1, "solid")
J5_carte1 = create_label(conteneur_J5, Lt_J5_carte1, ("Arial Bold", 25), None, None, 1, "solid")
J5_carte2 = create_label(conteneur_J5, Lt_J5_carte2, ("Arial Bold", 25), None, None, 1, "solid")
J6_carte1 = create_label(conteneur_J6, Lt_J6_carte1, ("Arial Bold", 25), None, None, 1, "solid")
J6_carte2 = create_label(conteneur_J6, Lt_J6_carte2, ("Arial Bold", 25), None, None, 1, "solid")


Board_carte1 = create_label(conteneur_middle_board, Lt_board_carte1, ("Arial Bold", 20), None, None, 1, "solid")
Board_carte2 = create_label(conteneur_middle_board, Lt_board_carte2, ("Arial Bold", 20), None, None, 1, "solid")
Board_carte3 = create_label(conteneur_middle_board, Lt_board_carte3, ("Arial Bold", 20), None, None, 1, "solid")
Board_carte4 = create_label(conteneur_middle_board, Lt_board_carte4, ("Arial Bold", 20), None, None, 1, "solid")
Board_carte5 = create_label(conteneur_middle_board, Lt_board_carte5, ("Arial Bold", 20), None, None, 1, "solid")



def MAJ_TOUT():
    # GRAPHIQUE MAJ
    Lt_pot_total.set("Pot: $" + str(Tables_1.pot)+ "\n" + str(round(Tables_1.pot/initialisation.BB, 1))+"BB")
    Lt_current_player.set("J" + str(Tables_1.current_player + 1))
    Lt_money_J1.set(str(Joueurs_dico["J1"].stack[0]) + "\n" + str(round(Joueurs_dico["J1"].stack[0]/initialisation.BB,
                                                                        1))+"BB")
    Lt_money_J2.set(str(Joueurs_dico["J2"].stack[0]) + "\n" + str(round(Joueurs_dico["J2"].stack[0]/initialisation.BB,
                                                                        1))+"BB")
    Lt_money_J3.set(str(Joueurs_dico["J3"].stack[0]) + "\n" + str(round(Joueurs_dico["J3"].stack[0]/initialisation.BB,
                                                                        1))+"BB")
    Lt_money_J4.set(str(Joueurs_dico["J4"].stack[0]) + "\n" + str(round(Joueurs_dico["J4"].stack[0]/initialisation.BB,
                                                                        1))+"BB")
    Lt_money_J5.set(str(Joueurs_dico["J5"].stack[0]) + "\n" + str(round(Joueurs_dico["J5"].stack[0]/initialisation.BB,
                                                                        1))+"BB")
    Lt_money_J6.set(str(Joueurs_dico["J6"].stack[0]) + "\n" + str(round(Joueurs_dico["J6"].stack[0]/initialisation.BB,
                                                                        1))+"BB")

    for i in range(len(Liste_money_Jx)):
        if Tables_1.current_player==i:
            Liste_money_Jx[i].configure(bg="yellow")
        else:
            Liste_money_Jx[i].configure(bg="#C0C0C0")

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

    if Tables_1.check_ok:
        bouton_call.config(text="CHECK")
        bouton_raise.config(text="BET")
    else:
        bouton_call.config(text="CALL")
        bouton_raise.config(text="RAISE")

    MAJ_bouton_dealer()
    return


def MAJ_FLOP(Board):
    # GRAPHIQUE MAJ
    Lt_board_carte1.set(Board[0])
    Lt_board_carte2.set(Board[1])
    Lt_board_carte3.set(Board[2])

    Board_carte1.config(fg=Jeux.couleur_carte(Board[0]))
    Board_carte2.config(fg=Jeux.couleur_carte(Board[1]))
    Board_carte3.config(fg=Jeux.couleur_carte(Board[2]))
    return


def MAJ_TURN(Board):
    # GRAPHIQUE MAJ
    Lt_board_carte4.set(Board[3])
    Board_carte4.config(fg=Jeux.couleur_carte(Board[3]))
    return


def MAJ_RIVER(Board):
    # GRAPHIQUE MAJ
    Lt_board_carte5.set(Board[4])
    Board_carte5.config(fg=Jeux.couleur_carte(Board[4]))
    return


def RAZ_BOARD():
    Lt_board_carte1.set("")
    Lt_board_carte2.set("")
    Lt_board_carte3.set("")
    Lt_board_carte4.set("")
    Lt_board_carte5.set("")
    return


def placer_bouton_dealer(tk_label, text, color):
    tk_label.place(relx=0.72, rely=0.2, width=40, height=35, anchor=tk.CENTER)
    tk_label.config(text=text, bg=color, fg="black")


def MAJ_bouton_dealer():
    L_boutton_dealer_J1.place_forget()
    L_boutton_dealer_J2.place_forget()
    L_boutton_dealer_J3.place_forget()
    L_boutton_dealer_J4.place_forget()
    L_boutton_dealer_J5.place_forget()
    L_boutton_dealer_J6.place_forget()
    if Tables_1.dealer==0:
        placer_bouton_dealer(L_boutton_dealer_J1, "DL", "#808080")
        placer_bouton_dealer(L_boutton_dealer_J2, "SB", "#0000FF")
        placer_bouton_dealer(L_boutton_dealer_J3, "BB", "#FF0000")
    if Tables_1.dealer==1:
        placer_bouton_dealer(L_boutton_dealer_J2, "DL", "#808080")
        placer_bouton_dealer(L_boutton_dealer_J3, "SB", "#0000FF")
        placer_bouton_dealer(L_boutton_dealer_J4, "BB", "#FF0000")
    if Tables_1.dealer==2:
        placer_bouton_dealer(L_boutton_dealer_J3, "DL", "#808080")
        placer_bouton_dealer(L_boutton_dealer_J4, "SB", "#0000FF")
        placer_bouton_dealer(L_boutton_dealer_J5, "BB", "#FF0000")
    if Tables_1.dealer==3:
        placer_bouton_dealer(L_boutton_dealer_J4, "DL", "#808080")
        placer_bouton_dealer(L_boutton_dealer_J5, "SB", "#0000FF")
        placer_bouton_dealer(L_boutton_dealer_J6, "BB", "#FF0000")
    if Tables_1.dealer==4:
        placer_bouton_dealer(L_boutton_dealer_J5, "DL", "#808080")
        placer_bouton_dealer(L_boutton_dealer_J6, "SB", "#0000FF")
        placer_bouton_dealer(L_boutton_dealer_J1, "BB", "#FF0000")
    if Tables_1.dealer==5:
        placer_bouton_dealer(L_boutton_dealer_J6, "DL", "#808080")
        placer_bouton_dealer(L_boutton_dealer_J1, "SB", "#0000FF")
        placer_bouton_dealer(L_boutton_dealer_J2, "BB", "#FF0000")
    return


MAJ_bouton_dealer()

mise_G = tk.Entry(conteneur_middle_play, font=("Arial", 14), bg="light blue")
bouton_raise = tk.Button(conteneur_middle_play, text="RAISE", bg="red", fg="black",
                         command=lambda: action_joueur.raise_play(MAJ_TOUT, mise_G))
bouton_call = tk.Button(conteneur_middle_play, text="CALL", bg="green", fg="black",
                        command=lambda: action_joueur.call_play(MAJ_TOUT, MAJ_FLOP, MAJ_TURN, MAJ_RIVER, RAZ_BOARD))
bouton_fold = tk.Button(conteneur_middle_play, text="FOLD", bg="#556B2F", fg="black",
                        command=lambda: action_joueur.fold_play(MAJ_TOUT, MAJ_FLOP, MAJ_TURN, MAJ_RIVER, RAZ_BOARD))
# bouton_start = tk.Button(conteneur2, text="START", bg="orange", fg="blue")
# bouton_refresh = tk.Button(conteneur6, text="REFRESH", bg="orange", fg="blue", command=MAJ_TOUT)
bouton_fermer = tk.Button(conteneur6, text="FERMER", bg="orange", fg="blue", command=Table_Poker.destroy)

# Conteneur 1

conteneur_J1.pack(side="top")
L_money2_J1.pack()
J1_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J1_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money_J1.pack()
mise_G.pack(expand=1)
mise_G.focus()
bouton_fold.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
bouton_call.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
bouton_raise.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Conteneur 2
conteneur_J2.pack(side="top")
L_money2_J2.pack()
J2_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J2_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money_J2.pack()

# Conteneur 3
conteneur_J3.pack(side="top")
L_money2_J3.pack()
J3_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J3_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money_J3.pack()

# Conteneur 4
conteneur_J4.pack(side="top")
L_money2_J4.pack()
J4_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J4_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money_J4.pack()

# Conteneur 5
conteneur_J5.pack(side="top")
L_money2_J5.pack()
J5_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J5_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money_J5.pack()

# Conteneur 6
conteneur_J6.pack(side="top")
L_money2_J6.pack()
J6_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J6_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money_J6.pack()
# bouton_fermer.pack(expand=1)

# Conteneur middle
L_pot_total.pack(expand=True)

# Conteneur board
Board_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
Board_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
Board_carte3.pack(side=tk.LEFT, fill=tk.X, expand=True)
Board_carte4.pack(side=tk.LEFT, fill=tk.X, expand=True)
Board_carte5.pack(side=tk.LEFT, fill=tk.X, expand=True)

MAJ_TOUT()
Table_Poker.mainloop()
