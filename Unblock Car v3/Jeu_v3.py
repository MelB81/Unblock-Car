from tkinter import *
import random


def parking():
        
    xr0 = 4*(f_largeur/5)-f_hauteur
    yr0 = 0
    xr1 = 4*(f_largeur/5)
    yr1 = f_hauteur
    z_dessin.create_rectangle(xr0,yr0,xr1,yr1,fill='light grey',outline='light grey')
        
    for i in range(1,6):
        #places du haut
        xl = i*(p_cote/6)+xr0
        yl0 = 0
        yl1 = p_cote/3
        z_dessin.create_line(xl,yl0,xl,yl1,fill='white',width=2)
        #places du bas
        xl = i*(p_cote/6)+xr0
        yl0 = 2*p_cote/3
        yl1 = p_cote
        z_dessin.create_line(xl,yl0,xl,yl1,fill='white',width=2)
            
def v_taille(sens): #pas besoin en fait
 
    TAILLES = [p_cote/2,p_cote/3]
    taille = random.choice(TAILLES)
    if (sens == "horizontal"):
        hauteur = (p_cote/6)-10
        largeur = taille-10
    else: #self.sens == "vertical"
        largeur = (p_cote/6)-10
        hauteur = taille-10
    return [largeur,hauteur]
    
def v_coordonnees(x,y,sens): #attention aux cas !!!

    x0 = (4*(f_largeur/5)-p_cote)+(x*(p_cote/6))+5 # +5 pour centrer la voiture dans sa place, référence au -10 de v_taille(pl,ph)
    y0 = (y*(p_cote/6))+5 #idem
    
    if x>=4 and y>=4:
        if (sens == "horizontal"):
            hauteur = (p_cote/6)-10
            largeur = (p_cote/3)-10
        else: #self.sens == "vertical"
            largeur = (p_cote/6)-10
            hauteur = (p_cote/3)-10
    elif x==4 and sens=="horizontal":
         hauteur = (p_cote/6)-10
         largeur = (p_cote/3)-10
    elif
    
    L_taille = v_taille(sens)
    x1 = x0 + L_taille[0]
    y1 = y0 + L_taille[1]
    
    return [x0,y0,x1,y1]
        
def v_dessin(x,y,sens):
    
    if (sens!="horizontal" and sens!="vertical"):
        raise Exception("Ce sens n'existe pas.")
    elif not(0<=x<=5) or not (0<=y<=5) or (x==5 and y==5):
        raise Exception("x ou y n'est pas dans le parking")
    else:
        COULEURS = ['red','orange','yellow','green','blue','purple']
        couleur = random.choice(COULEURS)
        L = v_coordonnees(x,y,sens)
        z_dessin.create_rectangle(L[0],L[1],L[2],L[3],fill=couleur,outline=couleur)
    
def clic(event):
    return True     
    
def pas_clic(event):
    return False
    
def s_position(event):
    return [event.x,event.y]


fenetre = Tk()
fenetre.title("Unblock Car")
        
fenetre.state("zoomed")
        
f_largeur = fenetre.winfo_screenwidth()
f_hauteur = fenetre.winfo_screenheight()
                
z_dessin = Canvas(fenetre,width=f_largeur,height=f_hauteur,background='white')
z_dessin.pack()
        
p_cote = f_hauteur

parking()

v_dessin(1,5,"vertical")

fenetre.bind("<Button-1>",clic)
fenetre.bind("<ButtonRelease-1>",pas_clic)
fenetre.bind("<Motion>",s_position)

fenetre.mainloop()