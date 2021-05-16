

from tkinter import* 
from Voiture import dessiner # depend de la version de retour

def rgb(r, g, b):
    return "#%.02x" % r + "%.02x" % g + "%.02x" % b

class Mouvement():
    def __init__(self,canva) :

        self.canva=canva
        self.mvt=0
        self.Lmouv=[]
        self.bouton=Button(self.canva, text= "position initiale",command=self.retour(self.mvt),font='courrier 15',bg=rgb(89, 163, 195)) #ou retourV2 ...
        self.bouton.place(x=100,y=300)
        canva.bind("<Button-1>", self.clic1)
        self.canva.bind("<ButtonRelease-1>", self.clic2 | self.ajout)

    def clic1(event):
        global clic1
        clic1=[event.x,event.y]
        return clic1  # return qui sert pas je crois...

    def clic2(event):
        global clic2
        clic2=[event.x,event.y]
        return clic2


    def ajout(self,clic1, clic2,ListeVoiture):# si la position du clic et du relachement sont different /!\ verifie pas si c'est sur une voiture
        if clic2!=clic1 :                       # du coup appel dans Bouger qui le verif avant d'ajouter ?
            self.mvt+=1
            self.Lmouv.append(ListeVoiture)
            self.afficher(self.mvt)
            return self.Lmouv # retour pour retourV2


    def afficher(self):
        if self.mvt>0:
            self.bouton.configure(text="vous avez fait: "+str(self.mvt))
        if self.mvt==0:
           self.bouton.configure(text="Vous êtes \n en position initiale !")   #marche pour mvt>0 mais pas pour mvt==0 ??? why ?????

    
    def retour(self):   # je suis coincé car il y une boucle j'importe Voiture dans mouvement et mouvement dans voiture ! Il veut pas le monsieur !!!!
        if self.mvt>0:
            Lvoi=self.Lmouv[self.mvt]
            Lvoi.dessiner(self.canva)
            self.Lmouv.pop()
            self.mvt-=1
            self.afficher(self.mvt)
            

    def retourV2(self,mvt,Lmouv):   # V2 pour la mettre dans la class voiture en utilisant les return de la class Voiture
        if mvt>=0:
            Lvoi=Lmouv[self.mvt]
            Lvoi.dessiner(self.pl.canva)
            self.mvt-=1
            self.Lmouv.pop()
            self.afficher(self.mvt)
 

        

