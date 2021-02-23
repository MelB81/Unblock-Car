import random
from Plateau import *

class Voiture:
    
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.sens = s
    
    def v_coordonnees():

        x0 = (4*(Plateau.f_largeur/5)-Plateau.p_cote)+(x*(Plateau.p_cote/6))+5 # +5 pour centrer la voiture dans sa place, référence au -10 de v_taille(pl,ph)
        y0 = (self.y*(Plateau.p_cote/6))+5 #idem
        
        TAILLES = [Plateau.p_cote/2,Plateau.p_cote/3]
        taille = random.choice(TAILLES)
        
        if (self.x>=4 and self.y>=4 and self.sens=="horizontal") or (self.x==4 and self.sens=="horizontal"):
            hauteur = (Plateau.p_cote/6)-10
            largeur = (Plateau.p_cote/3)-10 
        elif (self.x>=4 and self.y>=4 and self.sens=="vertical") or (self.y==4 and self.sens=="vertical"):
            hauteur = (Plateau.p_cote/3)-10 
            largeur = (Plateau.p_cote/6)-10
        else:
            if self.sens=="horizontal":
                hauteur = (Plateau.p_cote/6)-10
                largeur = taille-10
            else: #sens == "vertical"
                largeur = (Plateau.p_cote/6)-10
                hauteur = taille-10
        x1 = x0 + largeur
        y1 = y0 + hauteur
        return [x0,y0,x1,y1]
    
    def v_dessin():
    
        if (self.x==5 and self.y==5) or (self.x==5 and self.sens=="horizontal") or (self.y==5 and self.sens=="vertical"):
            raise Exception("Cette position est impossible.")
        elif not(self.sens=="horizontal" or self.sens=="vertical"):
            raise Exception("Ce sens n'existe pas.")
        elif not((0<=self.x<=5) and (0<=self.y<=5)):
            raise Exception("x ou y n'est pas dans le parking")
        else:
            COULEURS = ['red','orange','yellow','green','blue','purple']
            couleur = random.choice(COULEURS)
            L = v_coordonnees()
            voiture = Plateau.z_dessin.create_rectangle(L[0],L[1],L[2],L[3],fill=couleur,outline=couleur)
            return voiture
        
    def clic(event):
    
        c_precedent[0] = event.x
        c_precedent[1] = event.y
    
    def v_deplacement(event): #sens + pas sortir du parking + plus tard : choix de la voiture + pas de collision
        
        x = event.x-c_precedent[0]
        y = event.y-c_precedent[1]   
        
        if event.x<4*(Plateau.f_largeur/5)-Plateau.p_cote:
            xbis = 0 # + la largeur/hauteur de la voiture sinon sort du cadre
        elif 4*(Plateau.f_largeur/5)<event.x:
            xbis = 4*(Plateau.f_largeur/5) # - la largeur/hauteur de la voiture sinon sort du cadre
        else:
            xbis = x
        
        if event.y<0:
            ybis = 0
        elif Plateau.p_cote<event.y:
            ybis = Plateau.p_cote
        else:
            ybis = y
        
        Plateau.z_dessin.move(self,xbis,ybis)
        c_precedent[0] = event.x
        c_precedent[1] = event.y
        
    c_precedent = [None,None]