def liste_adj(l_arcs):
    """ Création d'un graphe représenté par une liste d'adjacence et initialisé avec les arcs donnés dans 'listeArcs'
    """
    gr = {}
    for (orig, extr) in l_arcs:
        if orig in gr:
            gr[orig].append(extr)
        else:
            gr[orig] = [extr]
        if extr not in gr:
            gr[extr] = []
    return gr


def ens_sommets(l_arcs):
    """Retourne la liste de sommets"""
    sommets = set()
    for orig, extr in l_arcs:
        sommets.add(orig)
        sommets.add(extr)
    return sommets


def ens_successeurs(l_arcs, n):
    """Retourne l'ensemble des successeurs de n"""
    return [extr for orig, extr in l_arcs if orig == n]


def ens_predecesseurs(l_arcs, n):
    """Retourne l'ensemble des prédecesseurs de n"""
    return [orig for orig, extr in l_arcs if extr == n]


def puits(l_arcs):
    """Retourne l'ensemble des puits du graphe"""
    origines = set()
    extremites = set()
    for orig, extr in l_arcs:
        origines.add(orig)
        extremites.add(extr)
    return extremites - origines


def sources(l_arcs):
    """Retourne l'ensemble des sources du graphe"""
    origines = set()
    extremites = set()
    for orig, extr in l_arcs:
        origines.add(orig)
        extremites.add(extr)
    return (origines - extremites)


if __name__ == '__main__':
    l_arcs = [('andreas', 'bernard'), ('Fred', 'andreas'), ('bernard', 'andreas'), ('cathie', 'andreas'),
              ('cathie', 'daniel'), ('bernard', 'cathie'), ('bernard', 'daniel'), ('bernard', 'emmanuel'),
              ('daniel', 'emmanuel')]
    print(1, liste_adj(l_arcs))
    print(2, ens_sommets(l_arcs))
    print(3, ens_predecesseurs(l_arcs, 'emmanuel'))
    print(4, ens_successeurs(l_arcs, 'bernard'))
    print(5, puits(l_arcs))
    print(6, sources(l_arcs))
