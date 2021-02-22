from tkinter import *
from Voiture_test import *

#création de la fenêtre
fenetre = Tk()
zone_dessin = Canvas(fenetre,width=600,height=600,bg="white",bd=8) #kesako bd=8 #fct taille écran
zone_dessin.pack()
fenetre.title("Level 1")


#création ligne parking
zone_dessin.create_rectangle(0,0,600,600,fill="grey23")
for i in range(6):
    a = (i*100,0)
    b = (i*100,200)
    zone_dessin.create_line(a,b,fill="snow")
    
for i in range(6):
    a = (i*100,600)
    b = (i*100,300)
    zone_dessin.create_line(a,b,fill="snow")

#créer voiture  
gagnante = Voiture(0,200,200,100)
gagnante.dessin_voiture(zone_dessin)

print(zone_dessin.coords(g))

#bouger voiture /!\ c'est du recopier donc juste test et à réadapter au sujet
old=[None, None]

def clic(event):
    old[0]=event.x
    old[1]=event.y

def glisser(event):
    a,b,c,d=zone_dessin.coords(g)
    
    if (c < UP and c > DOWN) or event.x>old[0]:
        zone_dessin.move(g, event.x-old[0], 0)
        old[0]=event.x
        old[1]=event.y
   
zone_dessin.bind("<B1-Motion>",glisser)
zone_dessin.bind("<Button-1>",clic)


fenetre.mainloop() #toujours à la fin