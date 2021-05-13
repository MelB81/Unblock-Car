from tkinter import * 

import time 
import random as alea
from winsound import *
#from MenuJ import *


# Option Unblock car 
def rgb(r, g, b):
    return "#%.02x" % r + "%.02x" % g + "%.02x" % b


#___________________Timer__________________

class Timer():

    def __init__(self, canva,x,y, x_image,y_image,coquillage):
        
        self.xi=x_image
        self.yi=y_image
        self.canva=canva
        self.minutes=0
        self.secondes=0
        self.reussite=3
        self.etat="Parfait"
        self.coqui=coquillage
        self.stop=False

        self.menu=None

        self.fichier_t="conch.png"
        self.t=PhotoImage(file=self.fichier_t)


        self.txt=Label(self.canva,text="temps: ",font='courrier 20', fg='white',bg=rgb(89, 163, 195))
        self.txt.place(x=x,y=y)
        self.MAJclock()
        

    def MAJclock(self):

        if self.minutes==0 and self.secondes==5: # passage de 3 à 2 etoiles
            self.reussite=2
            self.etat="Bien"

        if self.minutes==0 and self.secondes==10: # passage de 2 à 1 etoiles
            self.reussite=1
            self.etat="C'est déjà ça"

        if self.minutes==0 and self.secondes==15: # passage de 1 à 0 etoiles
            self.reussite=0
            self.etat="Dommage,\n pas de coquillage"
        
        if self.minutes==0 and self.secondes==20:
            self.reussite=-1
            self.etat="Perdu"
            self.stop=True

        if self.secondes==59: #Passage de 59 secondes à 1 minutes en plus
            self.minutes+=1
            self.secondes=0
        
        else:
            self.secondes+=1

        if self.secondes<10: #afficher 1:06 secondes par exemple au lieu de 1:6
            self.txt.configure(text=str(self.minutes)+":0"+ str(self.secondes)+ "\n"+self.etat) 

        else:
            self.txt.configure(text=str(self.minutes)+":"+ str(self.secondes)+ "\n"+self.etat) 


        if self.stop: #arret du Timer
            if self.reussite==-1:
                #self.menu=MenuJ()
                #self.menu.resolu()
                pass
            if self.secondes<10: #afficher 1:06 secondes par exemple au lieu de 1:6
                self.txt.configure(text=str(self.minutes)+":0"+ str(self.secondes)+ "\n"+self.etat) 
            else:
                self.txt.configure(text=str(self.minutes)+":"+ str(self.secondes)+ "\n"+self.etat)
            

        else:
            self.canva.after(1000, self.MAJclock) # apres 1 secondes MAJ du timer
                
            
            
    def coquillage(self):

        
        self.coqui+=self.reussite
        print(self.coqui)
            
        self.canva.image.append(self.t)
        self.canva.create_image(self.xi,self.yi, image=self.t)
        self.canva.create_text(self.xi,self.yi+100,text="x"+ str(self.reussite) +" "+self.etat,  font='courrier 20', fill='white')

        self.canva.create_text(self.xi,self.yi,text="Tu as "+ str(self.coqui)+" Coquillage(s)",font='courrier 20', fill='white')
        
        return self.coqui


#_________________Ajout Musique et bouton ____________
class Musique():

    def __init__(self,canva, x,y):

        self.canva=canva

        self.fichier_m="vagues.wav"
        self.etat="on"

        PlaySound(self.fichier_m, SND_LOOP | SND_ASYNC )
        self.OnOff=Button(self.canva, text="Son on", command=self.play,font='courrier 20',bg=rgb(89, 163, 195))
        self.OnOff.place(x=x,y=y)


    def play(self):
        
        if self.etat=="off":
            PlaySound(self.fichier_m, SND_LOOP | SND_ASYNC ) # jouer en boucle et ne pas obstruer le prog principal
            self.OnOff.config(text="Son on")
            self.etat="on"
        else:
            PlaySound(None, SND_PURGE) #couper provisoirement
            self.OnOff.config(text="Son off")
            self.etat="off"
      









