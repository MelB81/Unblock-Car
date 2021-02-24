from tkinter import Tk, Canvas
import random
    
class Voiture:
    
    COULEURS = ['red','orange','yellow','green','blue','purple']
    
    def __init__(self,x0,y0,x1,y1):
        self.x0 = (x0-1)*cote/6
        self.y0 = (y0-1)*cote/6
        self.x1 = x1*cote/6
        self.y1 = y1*cote/6
        couleur = random.choice(Voiture.COULEURS)
        self.voiture = dessin.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill=couleur,outline=couleur)
        if (self.x1-self.x0<self.y1-self.y0): #ou plus simple : x0==x1, tout dépend d'où on part
            self.sens = "vertical"
        else:
            self.sens = "horizontal"
            
    def bouger(self,x,y):
        if self.sens=="vertical":
            y00 = self.y0+y-old[1]
            y01 = self.y1+y-old[1]
            if not(y00<0 or y01>cote):
                dessin.move(self.voiture,0,y-old[1]) # 0 car cumul des anciennes coordonnées avec les nouvelles
                self.y0 = y00
                self.y1 = y01
            elif y01>cote:
                self.y0 = cote-(self.y1-self.y0)
                self.y1 = cote
            else:
                self.y0 = 0
                self.y1 = self.y1-self.y0
        else:
            x00 = self.x0+x-old[0]
            x01 = self.x1+x-old[0]
            if not(x00<0 or x01>cote):
                dessin.move(self.voiture,x-old[0],0)
                self.x0 = x00
                self.x1 = x01
            elif x01>cote:
                self.x0 = cote-(self.x1-self.x0)
                self.x1 = cote
            else:
                self.x0 = 0
                self.x1 = self.x1-self.x0
            
def clic(event):
    global clicV
    global old
    for v in listeVoiture:
        if v.x0<=event.x<=v.x1 and v.y0<=event.y<=v.y1:
            clicV = v
    old = [event.x,event.y]
            
def pasClic(event):
    global clicV
    clicV = None

def deplacer(event):
    global clicV
    global old
    if clicV!=None:
        clicV.bouger(event.x,event.y)
    old = [event.x,event.y]
        
old = [None,None]
clicV = None

fenetre = Tk()
fenetre.title("Unblock Car")

cote = fenetre.winfo_vrootheight()-100
dessin = Canvas(fenetre,width=cote,height=cote,bg="light grey")
dessin.pack()

for i in range(1,6):
    dessin.create_line(i*cote/6,0,i*cote/6,cote)
    dessin.create_line(0,i*cote/6,cote,i*cote/6)

listeVoiture = [Voiture(4,1,6,1),
    Voiture(2,1,2,3),
    Voiture(4,3,5,3),
    Voiture(3,4,3,5),
    Voiture(4,4,6,4),
    Voiture(1,5,2,5),
    Voiture(4,5,4,6),
    Voiture(1,6,2,6)]

dessin.bind("<Button-1>",clic) 
dessin.bind("<ButtonRelease-1>",pasClic)
dessin.bind("<B1-Motion>",deplacer)

fenetre.mainloop()