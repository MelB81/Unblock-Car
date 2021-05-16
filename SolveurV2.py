from Niveaux import *
from Plateau import *


class SolveurV2:

    # position des voitures sur le plateau
    def matrice(self, listeCoords):
        L = []
        for i in range(1, 7):  # de 1 à 7 pour garder numérotation des cases
            L.append([])
            for j in range(1, 7):
                L[i - 1].append(0)

        for i in range(1, len(listeCoords) + 1):
            v = listeCoords[i - 1]
            if v[2] - v[0] > v[3] - v[1]:  # voiture horizontale
                for j in range(v[0], v[2] + 1):
                    L[v[1] - 1][j - 1] = i
            else:  # voiture verticale
                for j in range(v[1], v[3] + 1):
                    L[j - 1][v[0] - 1] = i
        return L

    def mouvPossible(self, voiture, listeCoords, direction, pas):
        x0 = voiture[0]
        y0 = voiture[1]
        x1 = voiture[2]
        y1 = voiture[3]

        if direction == "gauche":
            if x0 - pas > 0:  # ne pas sortir du plateau
                for p in range(1, pas + 1):
                    if self.matrice(listeCoords)[y0 - 1][x0 - p - 1] != 0:  # vérifier qu'il n'y a aucune collision
                        return False
                return True
            else:
                return False

        elif direction == "droite":
            if x1 + pas < 7:
                for p in range(1, pas + 1):
                    if self.matrice(listeCoords)[y0 - 1][x1 + p - 1] != 0:
                        return False
                return True
            else:
                return False

        elif direction == "haut":
            if y0 - pas > 0:
                for p in range(1, pas + 1):
                    if self.matrice(listeCoords)[y0 - p - 1][x0 - 1] != 0:
                        return False
                return True
            else:
                return False

        else:  # direction == "bas"
            if y1 + pas < 7:
                for p in range(1, pas + 1):
                    if self.matrice(listeCoords)[y1 + p - 1][x0 - 1] != 0:
                        return False
                return True
            else:
                return False

    # pour visualiser
    def affichage(self, L):
        for i in range(len(L)):
            print(L[i])

    def sortir(self, listeCoords):
        n = len(listeCoords)
        gagnante = listeCoords[n - 1]
        return gagnante[0] == 5 and gagnante[1] == 3 and gagnante[2] == 6 and gagnante[3] == 3

    # 3 et 4 ne descendent jamais ?! bizarre car mouvPossible marche, pb dans entrée de file ?
    def resoudre(self, listeVoiture):

        # créer la liste de coordonnées de toutes les voitures au départ
        listeCoords = Niveaux().listeCoords(listeVoiture)

        # créer une file, initialisée avec chaque voiture de listeCoords
        file = []
        for v in listeCoords:
            file.append(v)

        # créer une file de la position précédente du plateau, synchrone avec file, initialisée avec listeCoords
        precedent = []
        for l in range(len(listeCoords)):
            precedent.append(listeCoords)

        # créer une liste des états du plateau déjà rencontrés, initialisée avec listeCoords
        deja = [listeCoords]

        # tant que les 2 files ne sont pas vides et qu'on a pas gagné avec le plateau précédent
        while len(file) > 0 and len(precedent) > 0 and not self.sortir(precedent[0]):

            # tests
            self.affichage(self.matrice(precedent[0]))

            # configuration du plateau traité et voiture traitée
            courant = file.pop(0)[:]
            prec = precedent.pop(0)[:]

            # si la voiture est horizontale
            if courant[2] - courant[0] > courant[3] - courant[1]:

                pas = 1
                # mouvement à gauche ?
                while self.mouvPossible(courant, prec, "gauche", pas):

                    # créer un nouvel état du plateau
                    etat = []
                    for v in prec:
                        if v != courant:
                            etat.append(v)
                        else:
                            courant[0] -= 1
                            courant[2] -= 1
                            etat.append(courant)

                    # si on n'a pas déjà rencontré cette configuration avant
                    if etat not in deja:
                        deja.append(etat)
                        # on ajoute les nouvelles positions de voitures dans file pour les traiter ensuite
                        for v in etat:
                            if v != courant:  # sinon retour à la position précédente = perte de temps
                                file.append(v)
                                precedent.append(etat)

                    pas += 1

                pas = 1
                # mouvement à droite ?
                while self.mouvPossible(courant, prec, "droite", pas):

                    # créer un nouvel état du plateau
                    etat = []
                    for v in prec:
                        if v != courant:
                            etat.append(v)
                        else:
                            courant[0] += 1
                            courant[2] += 1
                            etat.append(courant)

                    # si on n'a pas déjà rencontré cette configuration avant
                    if etat not in deja:
                        deja.append(etat)
                        # on ajoute les nouvelles positions de voitures dans file pour les traiter ensuite
                        for v in etat:
                            if v != courant:  # sinon retour à la position précédente = perte de temps
                                file.append(v)
                                precedent.append(etat)

                    pas += 1

            # si la voiture est verticale
            else:

                pas = 1
                # mouvement en haut ?
                while self.mouvPossible(courant, prec, "haut", pas):

                    # créer un nouvel état du plateau
                    etat = []
                    for v in prec:
                        if v != courant:
                            etat.append(v)
                        else:
                            courant[1] -= 1
                            courant[3] -= 1
                            etat.append(courant)

                    # si on n'a pas déjà rencontré cette configuration avant
                    if etat not in deja:
                        deja.append(etat)
                        # on ajoute les nouvelles positions de voitures dans file pour les traiter ensuite
                        for v in etat:
                            if v != courant:  # sinon retour à la position précédente = perte de temps
                                file.append(v)
                                precedent.append(etat)

                    pas += 1

                pas = 1
                # mouvement en bas ?
                while self.mouvPossible(courant, prec, "bas", pas):

                    # créer un nouvel état du plateau
                    etat = []
                    for v in prec:
                        if v != courant:
                            etat.append(v)
                        else:
                            courant[1] += 1
                            courant[3] += 1
                            etat.append(courant)

                    # si on n'a pas déjà rencontré cette configuration avant
                    if etat not in deja:
                        deja.append(etat)
                        # on ajoute les nouvelles positions de voitures dans file pour les traiter ensuite
                        for v in etat:
                            if v != courant:  # sinon retour à la position précédente = perte de temps
                                file.append(v)
                                precedent.append(etat)

                    pas += 1


fenetre = Tk()
canva = Canvas(fenetre, width=600, height=600)
listeVoiture = Niveaux().facile(Plateau(canva))[0]
listeCoords = Niveaux().listeCoords(listeVoiture)
SolveurV2().resoudre(listeVoiture)
