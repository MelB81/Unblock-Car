from tkinter import Tk, Canvas
import random

class Plateau:

    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("Unblock Car")
        self.fenetre.state('zoomed')
        self.cote = self.fenetre.winfo_vrootheight() - 100
        self.dessin = Canvas(self.fenetre, width=self.cote, height=self.cote, bg="light grey")
        self.dessin.pack()
        for i in range(1, 6):
            self.dessin.create_line(i * self.cote / 6, 0, i * self.cote / 6, self.cote)
            self.dessin.create_line(0, i * self.cote / 6, self.cote, i * self.cote / 6)
        self.sortie = [6, 3]
        self.sx0 = (self.sortie[0] - 1) * self.cote / 6
        self.sy0 = (self.sortie[1] - 1) * self.cote / 6
        self.sx1 = self.sx0 + self.cote/6
        self.sy1 = self.sy0 + self.cote/6
        self.dessin.create_line(self.sx0 + self.cote / 18, self.sy0 + self.cote / 12, self.sx0 + self.cote / 6 - self.cote / 18, self.sy0 + self.cote / 12, width=5, arrow='last')

class Voiture:

    COULEURS = ['orange', 'yellow', 'green', 'blue', 'purple']

    def __init__(self, x0, y0, x1, y1, g):
        self.x0 = (x0 - 1) * cote / 6
        self.y0 = (y0 - 1) * cote / 6
        self.x1 = x1 * cote / 6
        self.y1 = y1 * cote / 6
        self.gagnante = g
        if self.gagnante == True:
            self.voiture = dessin.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='red', outline='black')
        else:
            couleur = random.choice(Voiture.COULEURS)
            self.voiture = dessin.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=couleur, outline='black')
        if self.x1 - self.x0 < self.y1 - self.y0:  # ou plus simple : x0==x1, tout dépend d'où on part
            self.sens = "vertical"
        else:
            self.sens = "horizontal"
        self.largeur = self.x1 - self.x0
        self.hauteur = self.y1 - self.y0

    def bouger(self, x, y):
        coords = dessin.coords(self.voiture)
        x00 = coords[0] + x - old[0]
        x01 = coords[2] + x - old[0]
        y00 = coords[1] + (y - old[1])
        y01 = coords[3] + (y - old[1])
        crash = False

        for v in listeVoiture:
            if v != self:
                if (self.sens == "horizontal" and v.sens == "vertical") and (v.y0 <= self.y0 + cote/12 <= v.y1) and ((v.x0 <= x00 <= v.x1) or (v.x0 <= x01 <= v.x1)):
                    crash = True
                elif (self.sens == "vertical" and v.sens == "horizontal") and (v.x0 <= self.x0 + cote/12 <= v.x1) and ((v.y0 <= y01 <= v.y1) or (v.y0 <= y00 <= v.y1)):
                    crash = True
                elif (self.sens == "horizontal" and v.sens == "horizontal") and (v.y0 <= self.y0 + cote/12 <= v.y1 and v.y0 <= self.y1 - cote/12 <= v.y1) and (v.x0 <= x01 <= v.x1 or v.x0 <= x00 <= v.x1):
                    crash = True
                elif (self.sens == "vertical" and v.sens == "vertical") and (v.x0 <= self.x0 + cote/12 <= v.x1 and v.x0 <= self.x1 - cote/12 <= v.x1) and (v.y0 <= y00 <= v.y1 or v.y0 <= y01 <= v.y1):
                    crash = True

        if not(crash):
            if self.sens == "vertical":
                if y00 < 0:
                    self.y0 = 0
                    self.y1 = self.hauteur
                elif y01 > cote:
                    self.y0 = cote - self.hauteur
                    self.y1 = cote
                else:
                    dessin.move(self.voiture, 0, y - old[1])  # 0 car cumul des anciennes coordonnées avec les nouvelles
                    self.y0 = y00
                    self.y1 = y01
            else:
                if x00 < 0:
                    self.x0 = 0
                    self.x1 = self.largeur
                elif x01 > cote:
                    self.x0 = cote - self.largeur
                    self.x1 = cote
                else:
                    dessin.move(self.voiture, x - old[0], 0)
                    self.x0 = x00
                    self.x1 = x01

    def replacer(self):
        coords = dessin.coords(self.voiture)
        for i in range(0, 7):
            if i * cote / 6 <= coords[0] + cote/12 <= ((i + 1) * cote / 6):
                x0 = i * cote / 6
            if i * cote / 6 <= coords[1] + cote/12 <= ((i + 1) * cote / 6):
                y0 = i * cote / 6
        dessin.moveto(self.voiture, x0, y0)
        self.x0 = x0
        self.y0 = y0

    def gagner(self):
        global fin
        if self.gagnante and self.x1 == sx1 and self.y1 == sy1:
            fin = True

def clic(event):
    global clicV
    global old
    for v in listeVoiture:
        if v.x0 <= event.x <= v.x1 and v.y0 <= event.y <= v.y1:
            clicV = v
    old = [event.x, event.y]

def pasClic(event):
    global clicV
    if clicV != None:
        clicV.replacer()
    clicV = None

def deplacer(event):
    global clicV
    global old
    global fin
    if clicV.gagnante:
        clicV.gagner()
    if clicV != None and fin == False:
        clicV.bouger(event.x, event.y)
    old = [event.x, event.y]

old = [None, None]
clicV = None
fin = False

plateau = Plateau()
cote = plateau.cote
dessin = plateau.dessin
sx1 = plateau.sx1
sy1 = plateau.sy1

listeVoiture = [Voiture(3, 1, 3, 3, False),
                Voiture(4, 1, 4, 3, False),
                Voiture(5, 1, 6, 1, False),
                Voiture(5, 2, 5, 3, False),
                Voiture(5, 4, 5, 5, False),
                Voiture(2, 4, 2, 5, False),
                Voiture(3, 5, 4, 5, False),
                Voiture(1, 3, 2, 3, True)]

dessin.bind("<Button-1>", clic)
dessin.bind("<ButtonRelease-1>", pasClic)
dessin.bind("<B1-Motion>", deplacer)

plateau.fenetre.mainloop()