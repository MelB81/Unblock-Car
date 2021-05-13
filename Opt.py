from tkinter import * 

import time 
import random as alea
from winsound import *


# Option Unblock car 
def rgb(r, g, b):
    return "#%.02x" % r + "%.02x" % g + "%.02x" % b

#______Fenetre opt__________


#___________________Timer__________________

class Timer():

    def __init__(self, canva,x,y, x_image,y_image):
        
        self.xi=x_image
        self.yi=y_image
        self.canva=canva
        self.minutes=0
        self.secondes=0
        self.reussite="Parfait"
        self.stop=False

        self.fichier_t="coquillage.png"
        self.t=PhotoImage(file=self.fichier_t)


        self.txt=Label(self.canva,text="temps: ",font='courrier 25')
        self.txt.place(x=x,y=y)
        self.MAJclock()
        

    def MAJclock(self):

        if self.minutes==0 and self.secondes==30: # passage de 3 à 2 etoiles
            self.reussite="Bien"

        if self.minutes==1 and self.secondes==30: # passage de 2 à 1 etoiles
            self.reussite="Passable..."

        if self.minutes==2 and self.secondes==30: # passage de 1 à 0 etoiles
            self.reussite="Dommage, essaie encore pour gagner des coquillages !"

        if self.secondes==59: #Passage de 59 secondes à 1 minutes en plus
            self.minutes+=1
            self.secondes=0
        
        else:
            self.secondes+=1

        if self.secondes<10: #afficher 1:06 secondes par exemple au lieu de 1:6
            self.txt.configure(text=str(self.minutes)+":0"+ str(self.secondes)+ "\n"+self.reussite,font='courrier 25') 

        else:
            self.txt.configure(text=str(self.minutes)+":"+ str(self.secondes)+ "\n"+self.reussite,font='courrier 25') 


        

        if self.stop: #arret du Timer

            if self.secondes<10: #afficher 1:06 secondes par exemple au lieu de 1:6
                self.txt.configure(text=str(self.minutes)+":0"+ str(self.secondes)+ "\n"+self.reussite,font='courrier 25') 
            else:
                self.txt.configure(text=str(self.minutes)+":"+ str(self.secondes)+ "\n"+self.reussite,font='courrier 25')
        else:
            self.canva.after(1000, self.MAJclock) # apres 1 secondes MAJ du timer
                
            
            
    def coquillage(self):

        if self.reussite=="Parfait !":
            self.canva.image.append(self.t)
            self.canva.create_image(self.xi,self.yi, image=self.t)
            self.canva.create_text(self.xi,self.yi+100,text="x3 "+ self.reussite,  font='courrier 60')
  
        
        if self.reussite=="Bien":
            self.canva.image.append(self.t)
            self.canva.create_image(self.xi,self.yi,image=self.t)
            self.canva.create_text(self.xi,self.yi+100,text="x2 "+ self.reussite)
            

        if self.reussite=="Passable...":
            self.canva.image.append(self.t)
            self.canva.create_image(self.xi,self.yi, image=self.t)
            self.canva.create_text(self.xi,self.yi+100,text="x1 "+ self.reussite, font='courrier 60')


        else:
            self.canva.image.append(self.t)
            self.canva.create_image(self.xi,self.yi, image=self.t)
            self.canva.create_text(self.xi,self.yi+100,text="x0 "+ self.reussite)

#_________________Ajout Musique et bouton ____________
class Musique():

    def __init__(self,canva, x,y):

        self.canva=canva

        self.fichier_m="vagues.wav"
        self.etat="on"

        PlaySound(self.fichier_m, SND_LOOP | SND_ASYNC )
        self.OnOff=Button(self.canva, text="Son on", command=self.play)
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
      









