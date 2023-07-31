import cProfile
import pstats
import networkx as nx
import importlib
import matplotlib.pyplot as plt






# Création d'un objet graphe orienté
G = nx.DiGraph()

G.add_node("distrib_cartes", color="red")
G.add_node("raise_play", color="green")
G.add_node("call_play", color="green")
G.add_node("fold_play", color="green")
G.add_node("player_left", color="green")
G.add_node("reset_turn", color="green")
G.add_node("reset_main", color="green")
G.add_node("games_init", color="yellow")
G.add_node("distrib", color="yellow")
G.add_node("couleur_carte", color="yellow")
G.add_node("GRAPHIQUE", color="blue")
G.add_node("MAJ_TOUT", color="blue")
G.add_node("MAJ_FLOP", color="blue")
G.add_node("MAJ_TURN", color="blue")
G.add_node("MAJ_RIVER", color="blue")
G.add_node("RAZ_BOARD", color="blue")

G.add_edge("distrib_cartes", "call_play")
G.add_edge("distrib_cartes", "fold_play")
G.add_edge("player_left", "call_play")
G.add_edge("player_left", "fold_play")
G.add_edge("reset_turn", "call_play")
G.add_edge("reset_turn", "fold_play")
G.add_edge("reset_main", "call_play")
G.add_edge("reset_main", "fold_play")
G.add_edge("raise_play", "GRAPHIQUE")
G.add_edge("call_play", "GRAPHIQUE")
G.add_edge("fold_play", "GRAPHIQUE")
G.add_edge("couleur_carte", "GRAPHIQUE")
G.add_edge("distrib", "games_init")
G.add_edge("games_init", "distrib_cartes")
G.add_edge("MAJ_TOUT", "call_play")
G.add_edge("MAJ_FLOP", "call_play")
G.add_edge("MAJ_TURN", "call_play")
G.add_edge("MAJ_RIVER", "call_play")
G.add_edge("MAJ_TOUT", "call_play")
G.add_edge("RAZ_BOARD", "call_play")
G.add_edge("MAJ_TOUT", "fold_play")
G.add_edge("MAJ_FLOP", "fold_play")
G.add_edge("MAJ_TURN", "fold_play")
G.add_edge("MAJ_RIVER", "fold_play")
G.add_edge("MAJ_TOUT", "fold_play")
G.add_edge("RAZ_BOARD", "fold_play")

# Définir les couleurs des nœuds
node_colors = [G.nodes[node]["color"] for node in G.nodes]

# Affichage du graphe avec les flèches directionnelles et les couleurs des nœuds
pos = nx.shell_layout(G)  # Positionnement circulaire des nœuds
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500)
nx.draw_networkx_labels(G, pos, font_size=13)
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->', connectionstyle='arc3,rad=0.5', arrowsize=80)

plt.axis('off')
#plt.show()





if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()

    import initialisation
    import action_joueur
    import graphique

    profiler.disable()

    # Générer les statistiques d'appel de fonction
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('ncalls')  # Tri des statistiques par nombre d'apelle

    stats.print_stats()

    # Afficher les appels de fonction





