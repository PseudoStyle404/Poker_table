import tkinter as tk
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


def window(Table_Poker):
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

    conteneur_middle = tk.Frame(Table_Poker, bg="white")
    conteneur_middle.place(relx=0.5, rely=0.4, width=120, height=60, anchor=tk.CENTER)

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

    # Fonction pour créer les labels avec des paramètres communs

    L_pot_total = create_label(conteneur_middle, Lt_pot_total, ("Arial Bold", 15), 'yellow', 'black', 1, "solid")
    L_current_player = create_label(conteneur_middle, Lt_current_player, ("Arial Bold", 15), None, None, 1, "solid")

    L_money_J1 = create_label(conteneur1, Lt_money_J1, ("Arial Bold", 15), None, None, 1, "solid")
    L_money_J2 = create_label(conteneur2, Lt_money_J2, ("Arial Bold", 15), None, None, 1, "solid")
    L_money_J3 = create_label(conteneur3, Lt_money_J3, ("Arial Bold", 15), None, None, 1, "solid")
    L_money_J4 = create_label(conteneur4, Lt_money_J4, ("Arial Bold", 15), None, None, 1, "solid")
    L_money_J5 = create_label(conteneur5, Lt_money_J5, ("Arial Bold", 15), None, None, 1, "solid")
    L_money_J6 = create_label(conteneur6, Lt_money_J6, ("Arial Bold", 15), None, None, 1, "solid")

    L_money2_J1 = create_label(conteneur1, Lt_money2_J1, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
    L_money2_J2 = create_label(conteneur2, Lt_money2_J2, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
    L_money2_J3 = create_label(conteneur3, Lt_money2_J3, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
    L_money2_J4 = create_label(conteneur4, Lt_money2_J4, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
    L_money2_J5 = create_label(conteneur5, Lt_money2_J5, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")
    L_money2_J6 = create_label(conteneur6, Lt_money2_J6, ("Arial Bold", 12), 'yellow', 'black', 1, "solid")

    mise_G = tk.Entry(conteneur1, font=("Arial", 20), bg="white")

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

    bouton_raise = tk.Button(conteneur1, text="RAISE", bg="red", fg="black", command=action_joueur.raise_play)
    bouton_call = tk.Button(conteneur1, text="CALL", bg="green", fg="black", command=action_joueur.call_play)
    bouton_fold = tk.Button(conteneur1, text="FOLD", bg="#556B2F", fg="black", command=action_joueur.fold_play)
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
    bouton_fold.pack(side=tk.LEFT, fill=tk.X, expand=True)
    bouton_call.pack(side=tk.LEFT, fill=tk.X, expand=True)
    bouton_raise.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # Conteneur 2
    conteneur_J2.pack(side="top")
    J2_carte1.pack(side=tk.LEFT, fill=tk.X, expand=True)
    J2_carte2.pack(side=tk.LEFT, fill=tk.X, expand=True)
    L_money2_J2.pack()
    L_money_J2.pack()
    # bouton_start.pack(expand=1)

    # Conteneur 3
    # conteneur_J3.pack(side="top")
    # J3_carte1.pack()
    # J3_carte2.pack()
    # L_money2_J3.pack()
    # L_money_J3.pack()

    # Conteneur 4
    # conteneur_J4.pack(side="top")
    # J4_carte1.pack()
    # J4_carte2.pack()
    # L_money2_J4.pack()
    # L_money_J4.pack()

    # Conteneur 5
    # conteneur_J5.pack(side="top")
    # J5_carte1.pack()
    # J5_carte2.pack()
    # L_money2_J5.pack()
    # L_money_J5.pack()

    # Conteneur 6
    # conteneur_J6.pack(side="top")
    # J6_carte1.pack()
    # J6_carte2.pack()
    # L_money2_J6.pack()
    # L_money_J6.pack()
    # bouton_refresh.pack(expand=1)
    # bouton_fermer.pack(expand=1)

    # Conteneur middle
    # L_current_player.pack()
    # L_pot_total.pack()

    action_joueur.start_game()
    Table_Poker.mainloop()

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