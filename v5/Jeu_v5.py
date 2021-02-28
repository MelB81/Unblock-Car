from tkinter import Tk, Canvas
import random

class Voiture:

    COULEURS = ['orange', 'yellow', 'green', 'blue', 'purple']

    def __init__(self, x0, y0, x1, y1, g):
        self.x0 = (x0 - 1) * cote / 6
        self.y0 = (y0 - 1) * cote / 6
        self.x1 = x1 * cote / 6
        self.y1 = y1 * cote / 6
        self.gagnante = g
        if self.gagnante == True:
            self.voiture = dessin.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='red', outline='red')
        else:
            couleur = random.choice(Voiture.COULEURS)
            self.voiture = dessin.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=couleur, outline=couleur)
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
        global sx0
        global sy0
        if self.gagnante and self.x0 == sx0 and self.y0 == sy0:
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
    clicV.gagner()
    if clicV != None and fin == False:
        clicV.bouger(event.x, event.y)
    old = [event.x, event.y]

old = [None, None]
clicV = None
fin = False

fenetre = Tk()
fenetre.title("Unblock Car")
fenetre.state('zoomed')

cote = fenetre.winfo_vrootheight() - 100
dessin = Canvas(fenetre, width=cote, height=cote, bg="light grey")
dessin.pack()

for i in range(1, 6):
    dessin.create_line(i * cote / 6, 0, i * cote / 6, cote)
    dessin.create_line(0, i * cote / 6, cote, i * cote / 6)

listeVoiture = [Voiture(3, 1, 3, 3, False),
                Voiture(4, 1, 4, 3, False),
                Voiture(5, 1, 6, 1, False),
                Voiture(5, 2, 5, 3, False),
                Voiture(5, 4, 5, 5, False),
                Voiture(2, 4, 2, 5, False),
                Voiture(3, 5, 4, 5, False),
                Voiture(1, 3, 2, 3, True)]

#listeVoiture = [Voiture(1, 1, 1, 3, False),
                #Voiture(1, 4, 2, 4, False),
                #Voiture(1, 6, 2, 6, False),
                #Voiture(3, 4, 3, 5, False),
                #Voiture(4, 4, 4, 6, False),
                #Voiture(5, 2, 5, 4, False),
                #Voiture(5, 5, 6, 5, False),
                #Voiture(3, 3, 4, 3, True)]

sortie = [6, 3]
sx0 = (sortie[0]-1)*cote/6
sy0 = (sortie[1]-1)*cote/6

dessin.create_line(sx0 + cote/18, sy0 + cote/12, sx0 + cote/6 - cote/18, sy0 + cote/12, width=5, arrow='last')

dessin.bind("<Button-1>", clic)
dessin.bind("<ButtonRelease-1>", pasClic)
dessin.bind("<B1-Motion>", deplacer)

fenetre.mainloop()