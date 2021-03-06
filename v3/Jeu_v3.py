from tkinter import Tk, Canvas
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
    
def v_coordonnees(x,y,sens):

    x0 = (4*(f_largeur/5)-p_cote)+(x*(p_cote/6))+5 # +5 pour centrer la voiture dans sa place, référence au -10 de v_taille(pl,ph)
    y0 = (y*(p_cote/6))+5 #idem
    
    TAILLES = [p_cote/2,p_cote/3]
    taille = random.choice(TAILLES)
    
    if (x>=4 and y>=4 and sens=="horizontal") or (x==4 and sens=="horizontal"):
        hauteur = (p_cote/6)-10
        largeur = (p_cote/3)-10 
    elif (x>=4 and y>=4 and sens=="vertical") or (y==4 and sens=="vertical"):
        hauteur = (p_cote/3)-10 
        largeur = (p_cote/6)-10
    else:
        if sens=="horizontal":
            hauteur = (p_cote/6)-10
            largeur = taille-10
        else: #sens == "vertical"
            largeur = (p_cote/6)-10
            hauteur = taille-10
    x1 = x0 + largeur
    y1 = y0 + hauteur
    return [x0,y0,x1,y1]
        
def v_dessin(x,y,sens):
    
    if (x==5 and y==5) or (x==5 and sens=="horizontal") or (y==5 and sens=="vertical"):
        raise Exception("Cette position est impossible.")
    elif not(sens=="horizontal" or sens=="vertical"):
        raise Exception("Ce sens n'existe pas.")
    elif not((0<=x<=5) and (0<=y<=5)):
        raise Exception("x ou y n'est pas dans le parking")
    else:
        COULEURS = ['red','orange','yellow','green','blue','purple']
        couleur = random.choice(COULEURS)
        L = v_coordonnees(x,y,sens)
        voiture = z_dessin.create_rectangle(L[0],L[1],L[2],L[3],fill=couleur,outline=couleur)
        return voiture
    
def clic(event):
    
    c_precedent[0] = event.x
    c_precedent[1] = event.y
    
def v_deplacement(event): #sens + pas sortir du parking + plus tard : choix de la voiture + pas de collision
    
    x = event.x-c_precedent[0]
    y = event.y-c_precedent[1]   
    
    if event.x<4*(f_largeur/5)-p_cote:
        xbis = 0 # + la largeur/hauteur de la voiture sinon sort du cadre
    elif 4*(f_largeur/5)<event.x:
        xbis = 4*(f_largeur/5) # - la largeur/hauteur de la voiture sinon sort du cadre
    else:
        xbis = x
    
    if event.y<0:
        ybis = 0
    elif p_cote<event.y:
        ybis = p_cote
    else:
        ybis = y
    
    z_dessin.move(v1,xbis,ybis)
    c_precedent[0] = event.x
    c_precedent[1] = event.y
    
def ecran_classique(event):
    fenetre.attributes("-fullscreen",False)
 
c_precedent = [None,None]

fenetre = Tk()
fenetre.title("Unblock Car")
        
fenetre.state("zoomed")
fenetre.attributes("-fullscreen",True)
fenetre.bind("<Escape>",ecran_classique) #créer une fonction pour re-rentrer dans le mode plein écran
        
f_largeur = fenetre.winfo_screenwidth()
f_hauteur = fenetre.winfo_screenheight()
                
z_dessin = Canvas(fenetre,width=f_largeur,height=f_hauteur,background='white')
z_dessin.pack()

z_dessin.create_text(5,5,anchor="nw",text="UNBLOCK CAR",font="Arial 30 bold",fill='blue') #modifier taille font pour que s'adapte à tous les écrans ?
z_dessin.create_text(4*(f_largeur/5)+5,5,anchor="nw",text="Sortir du mode Plein Ecran :\npresser echap",font="Arial 15") #idem
        
p_cote = f_hauteur

parking()

v1 =v_dessin(0,0,"horizontal")

z_dessin.bind("<B1-Motion>",v_deplacement)
z_dessin.bind("<Button-1>",clic)

fenetre.mainloop()