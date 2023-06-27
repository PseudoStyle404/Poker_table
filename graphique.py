import tkinter as tk

import Jeux
import initialisation
import action_joueur


# Fonction pour créer un conteneur avec des paramètres spécifiques
def create_container(parent, row, column, bg_color):
    container = tk.Frame(parent, bg=bg_color, highlightthickness=0.2)
    container.grid(row=row, column=column, sticky="nsew")
    container.grid_propagate(False)
    return container


def create_label(container, textvariable, font, fg, bg, borderwidth, relief):
    return tk.Label(container, textvariable=textvariable, font=font, fg=fg, bg=bg,
                    borderwidth=borderwidth, relief=relief)


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
Table_Poker.geometry('800x500')
Table_Poker["bg"]='green'


#  Attache l'événement de redimensionnement à la fonction ajuster_conteneurs
# Table_Poker.bind("<Configure>", ajuster_conteneurs)
string_vars = [
    tk.StringVar(Table_Poker) for _ in range(27)
]
(
    Lt_pot_total, Lt_current_player,
    Lt_money_J1, Lt_money_J2, Lt_money_J3, Lt_money_J4, Lt_money_J5, Lt_money_J6,
    Lt_money2_J1, Lt_money2_J2, Lt_money2_J3, Lt_money2_J4, Lt_money2_J5, Lt_money2_J6, Lt_couleur_variable,
    Lt_J1_carte1, Lt_J1_carte2,
    Lt_J2_carte1, Lt_J2_carte2,
    Lt_J3_carte1, Lt_J3_carte2,
    Lt_J4_carte1, Lt_J4_carte2,
    Lt_J5_carte1, Lt_J5_carte2,
    Lt_J6_carte1, Lt_J6_carte2
) = string_vars[:27]


conteneur1 = create_container(Table_Poker, 1, 1, "#008000")
conteneur2 = create_container(Table_Poker, 1, 0, "#6B8E23")
conteneur3 = create_container(Table_Poker, 0, 0, "#008000")
conteneur4 = create_container(Table_Poker, 0, 1, "#6B8E23")
conteneur5 = create_container(Table_Poker, 0, 2, "#008000")
conteneur6 = create_container(Table_Poker, 1, 2, "#6B8E23")

conteneur_J1 = tk.Frame(conteneur1)
conteneur_J2 = tk.Frame(conteneur2)
conteneur_J3 = tk.Frame(conteneur3)
conteneur_J4 = tk.Frame(conteneur4)
conteneur_J5 = tk.Frame(conteneur5)
conteneur_J6 = tk.Frame(conteneur6)

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

conteneur_middle = tk.Frame(Table_Poker, bg="red")
conteneur_middle.place(relx=0.5, rely=0.4, width=120, height=35, anchor=tk.CENTER)

conteneur_middle_play = tk.Frame(Table_Poker, bg="blue")
conteneur_middle_play.place(relx=0.5, rely=0.85, width=204, height=70, anchor=tk.CENTER)

L_pot_total = create_label(conteneur_middle, Lt_pot_total, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")

L_money_J1 = create_label(conteneur1, Lt_money_J1, ("Arial Bold", 15), None, None, 1, "solid")
L_money_J2 = create_label(conteneur2, Lt_money_J2, ("Arial Bold", 15), None, None, 1, "solid")
L_money_J3 = create_label(conteneur3, Lt_money_J3, ("Arial Bold", 15), None, None, 1, "solid")
L_money_J4 = create_label(conteneur4, Lt_money_J4, ("Arial Bold", 15), None, None, 1, "solid")
L_money_J5 = create_label(conteneur5, Lt_money_J5, ("Arial Bold", 15), None, None, 1, "solid")
L_money_J6 = create_label(conteneur6, Lt_money_J6, ("Arial Bold", 15), None, None, 1, "solid")

Liste_money_Jx=[L_money_J1, L_money_J2, L_money_J3, L_money_J4, L_money_J5, L_money_J6]

L_money2_J1 = create_label(conteneur1, Lt_money2_J1, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
L_money2_J2 = create_label(conteneur2, Lt_money2_J2, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
L_money2_J3 = create_label(conteneur3, Lt_money2_J3, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
L_money2_J4 = create_label(conteneur4, Lt_money2_J4, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
L_money2_J5 = create_label(conteneur5, Lt_money2_J5, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
L_money2_J6 = create_label(conteneur6, Lt_money2_J6, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")


J1_carte1 = create_label(conteneur_J1, Lt_J1_carte1, ("Arial Bold", 20), None, None, 1, "solid")
J1_carte2 = create_label(conteneur_J1, Lt_J1_carte2, ("Arial Bold", 20), None, None, 1, "solid")
J2_carte1 = create_label(conteneur_J2, Lt_J2_carte1, ("Arial Bold", 15), None, None, 1, "solid")
J2_carte2 = create_label(conteneur_J2, Lt_J2_carte2, ("Arial Bold", 15), None, None, 1, "solid")
J3_carte1 = create_label(conteneur_J3, Lt_J3_carte1, ("Arial Bold", 15), None, None, 1, "solid")
J3_carte2 = create_label(conteneur_J3, Lt_J3_carte2, ("Arial Bold", 15), None, None, 1, "solid")
J4_carte1 = create_label(conteneur_J4, Lt_J4_carte1, ("Arial Bold", 15), None, None, 1, "solid")
J4_carte2 = create_label(conteneur_J4, Lt_J4_carte2, ("Arial Bold", 15), None, None, 1, "solid")
J5_carte1 = create_label(conteneur_J5, Lt_J5_carte1, ("Arial Bold", 15), None, None, 1, "solid")
J5_carte2 = create_label(conteneur_J5, Lt_J5_carte2, ("Arial Bold", 15), None, None, 1, "solid")
J6_carte1 = create_label(conteneur_J6, Lt_J6_carte1, ("Arial Bold", 15), None, None, 1, "solid")
J6_carte2 = create_label(conteneur_J6, Lt_J6_carte2, ("Arial Bold", 15), None, None, 1, "solid")



def MAJ_TOUT():
    # GRAPHIQUE MAJ
    Lt_pot_total.set("Pot: $" + str(Tables_1.pot))
    Lt_current_player.set("J" + str(Tables_1.current_player + 1))
    Lt_money_J1.set(str(Joueurs_dico["J1"].stack[0]))
    Lt_money_J2.set(str(Joueurs_dico["J2"].stack[0]))
    Lt_money_J3.set(str(Joueurs_dico["J3"].stack[0]))
    Lt_money_J4.set(str(Joueurs_dico["J4"].stack[0]))
    Lt_money_J5.set(str(Joueurs_dico["J5"].stack[0]))
    Lt_money_J6.set(str(Joueurs_dico["J6"].stack[0]))

    for i in range(len(Liste_money_Jx)):
        if Tables_1.current_player==i:
            Liste_money_Jx[i].configure(bg="red")
        else:
            Liste_money_Jx[i].configure(bg="white")

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


mise_G = tk.Entry(conteneur_middle_play, font=("Arial", 14), bg="light blue")
bouton_raise = tk.Button(conteneur_middle_play, text="RAISE", bg="yellow", fg="black",
                         command=lambda: action_joueur.raise_play(MAJ_TOUT, mise_G))
bouton_call = tk.Button(conteneur_middle_play, text="CALL", bg="green", fg="black",
                        command=lambda: action_joueur.call_play(MAJ_TOUT))
bouton_fold = tk.Button(conteneur_middle_play, text="FOLD", bg="#556B2F", fg="black",
                        command=lambda: action_joueur.fold_play(MAJ_TOUT))
# bouton_start = tk.Button(conteneur2, text="START", bg="orange", fg="blue")
# bouton_refresh = tk.Button(conteneur6, text="REFRESH", bg="orange", fg="blue", command=MAJ_TOUT)
bouton_fermer = tk.Button(conteneur6, text="FERMER", bg="orange", fg="blue", command=Table_Poker.destroy)

# Conteneur 1

conteneur_J1.pack(side="top")
J1_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J1_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money2_J1.pack()
L_money_J1.pack()
mise_G.pack(expand=1)
bouton_fold.pack(side=tk.LEFT, expand=True)
bouton_call.pack(side=tk.LEFT, expand=True)
bouton_raise.pack(side=tk.LEFT, expand=True)

# Conteneur 2
conteneur_J2.pack(side="top")
J2_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J2_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money2_J2.pack()
L_money_J2.pack()

# Conteneur 3
conteneur_J3.pack(side="top")
J3_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J3_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money2_J3.pack()
L_money_J3.pack()

# Conteneur 4
conteneur_J4.pack(side="top")
J4_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J4_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money2_J4.pack()
L_money_J4.pack()

# Conteneur 5
conteneur_J5.pack(side="top")
J5_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J5_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money2_J5.pack()
L_money_J5.pack()

# Conteneur 6
conteneur_J6.pack(side="top")
J6_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
J6_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
L_money2_J6.pack()
L_money_J6.pack()
# bouton_fermer.pack(expand=1)

# Conteneur middle
L_pot_total.pack(expand=True)


MAJ_TOUT()
Table_Poker.mainloop()
