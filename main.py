import cProfile
import pstats


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





