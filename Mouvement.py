

from tkinter import* 

def rgb(r, g, b):
    return "#%.02x" % r + "%.02x" % g + "%.02x" % b

class Mouvement():
    def __init__(self,canva) :
        self.canva=canva
        self.mvt=0
        self.Lmouv=[]
        self.bouton=Button(self.canva, text= "position initiale",command=self.retour(self.mvt),font='courrier 15',bg=rgb(89, 163, 195))
        self.bouton.place(x=100,y=300)
        canva.bind("<Button-1>", self.clic1)
        self.canva.bind("<ButtonRelease-1>", self.clic2 | self.ajout)

    def clic1(event):
        global clic1
        clic1=[event.x,event.y]
        return clic1

    def clic2(event):
        global clic2
        clic2=[event.x,event.y]
        return clic2


    def ajout(self,clic1, clic2):
        if clic2!=clic1:
            self.mvt+=1


    def afficher(self,mvt):

        if mvt>0:
            self.bouton.configure(text="vous avez fait: "+str(mvt))
        if mvt==0:
           self.bouton.configure(text="Vous êtes \n en position initiale !")   #marche pour mvt>0 mais pas pour mvt==0 ??? why ?????

    
    def retour(self,mvt):
        if mvt>0:
            mvt-=1
        
        return mvt
