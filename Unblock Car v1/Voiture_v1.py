import random

class Voiture:
        
    def __init__(self,xi,yi,l,h):
        self.x = xi #position initiale en x
        self.y = yi #position initiale en y
        self.largeur = l #sens à déterminer en fct de taille de h et l
        self.hauteur = h
        
    def dessin_voiture(self, z):
        r = random.choice(["pink","tomato","OliveDrab1"])
        z.create_rectangle(self.x,self.y,self.x+self.largeur,self.y+self.hauteur,fill=r)
        
    
    
    #def deplacer(self, clicsouris):
        #if self.sens == ‘vertical’:
            #[…]
        #elif self.sens == ‘horizontal’:
            #[…]
        #else:
            #[exception]

    
