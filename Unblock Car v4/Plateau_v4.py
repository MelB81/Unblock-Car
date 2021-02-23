from tkinter import Tk, Canvas
import Voiture_v4

class Plateau:
    
    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("Unblock Car")
                
        self.fenetre.state("zoomed")
        self.fenetre.attributes("-fullscreen",True)
        self.fenetre.bind("<Escape>",ecran_classique) #créer une fonction pour re-rentrer dans le mode plein écran
                
        self.f_largeur = self.fenetre.winfo_screenwidth()
        self.f_hauteur = self.fenetre.winfo_screenheight()
                        
        self.z_dessin = Canvas(self.fenetre,width=self.f_largeur,height=self.f_hauteur,background='white')
        self.z_dessin.pack()
        
        self.z_dessin.create_text(5,5,anchor="nw",text="UNBLOCK CAR",font="Arial 30 bold",fill='blue') #modifier taille font pour que s'adapte à tous les écrans ?
        self.z_dessin.create_text(4*(f_largeur/5)+5,5,anchor="nw",text="Sortir du mode Plein Ecran :\npresser echap",font="Arial 15") #idem
                
        self.p_cote = self.f_hauteur
        
        self.parking()
        
        self.z_dessin.bind("<B1-Motion>",Voiture_v4.v_deplacement)
        self.z_dessin.bind("<Button-1>",Voiture_v4.clic)
        
    def ecran_classique(event):
        self.fenetre.attributes("-fullscreen",False)

    def parking():
            
        xr0 = 4*(self.f_largeur/5)-self.f_hauteur
        yr0 = 0
        xr1 = 4*(self.f_largeur/5)
        yr1 = self.f_hauteur
        self.z_dessin.create_rectangle(xr0,yr0,xr1,yr1,fill='light grey',outline='light grey')
            
        for i in range(1,6):
            #places du haut
            xl = i*(slef.p_cote/6)+xr0
            yl0 = 0
            yl1 = self.p_cote/3
            self.z_dessin.create_line(xl,yl0,xl,yl1,fill='white',width=2)
            #places du bas
            xl = i*(self.p_cote/6)+xr0
            yl0 = 2*self.p_cote/3
            yl1 = self.p_cote
            self.z_dessin.create_line(xl,yl0,xl,yl1,fill='white',width=2)
            
