def noeuds_accessibles(liste_adj, noeud_depart):
    visites = set()
    def dfs(noeud):
        if noeud not in visites:
            visites.add(noeud)
            for voisin in liste_adj[noeud]:
                dfs(voisin)
    dfs(noeud_depart)

    return visites
liste_adj = [[1, 3], [2], [0], [4], [3], []]
accessibles_depuis_0 = noeuds_accessibles(liste_adj, 0)
print("Accessible depuis 0:", accessibles_depuis_0)

accessibles_depuis_3 = noeuds_accessibles(liste_adj, 3)
print("Accessible depuis 3:", accessibles_depuis_3)