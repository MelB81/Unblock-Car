import random

class Voiture():
    
    COULEURS = ['red','orange','yellow','green','blue','purple']
    
    def __init__(self,x,y,s):
        self.x0 = x
        self.y0 = y
        self.sens = s
        
    def v_taille(self,pc):
        
        if (self.sens!="horizontal" and self.sens!="vertical"):
            raise Exception("Ce sens n'existe pas.")
        else:
            l_tailles = [pc/2,pc/3]
            taille = random.choice(l_tailles)
            if (self.sens == "horizontal"):
                hauteur = (pc/6)-10
                largeur = taille-10
            else: #self.sens == "vertical"
                largeur = (pc/6)-10
                hauteur = taille-10
            return [largeur,hauteur]
    
    def v_position(self,pc,fl):
        
        if not(0<=self.x0<=5) or not (0 <= self.y0 <= 5):
            raise Exception("self.x0 ou self.y0 n`est pas dans le parking")
        else:
            x = (4*(fl/5)-pc)+(self.x0*(pc/6))+5 # +5 pour centrer la voiture dans sa place, référence au -10 de v_taille(pl,ph)
            y = (self.y0*(pc/6))+5 #idem
            return [x,y]
        
    def v_dessin(self,zd,pc,fl):
        
        couleur = random.choice(Voiture.COULEURS)
        L_taille = self.v_taille(pc)
        L_position = self.v_position(pc,fl)
        x1 = L_position[0] + L_taille[0]
        y1 = L_position[1] + L_taille[1]
        zd.create_rectangle(L_position[0],L_position[1],x1,y1,fill=couleur,outline=couleur)
        
    def clic(event):
        return True     
    
    def pas_clic(event):
        return False
        
    def s_position(event): #à modifier pour que la voiture suive + exception
        return [event.x,event.y]
        
        
        