from Niveaux import *
from Opt import Musique, Timer

def rgb(r, g, b):
    return "#%.02x" % r + "%.02x" % g + "%.02x" % b


class MenuJ:  # on ne l'appelle pas Menu car cette classe existe déjà, et on aurait des messages d'erreur sinon

    def __init__(self):

        self.fenetre = Tk()                             #creation de la fenetre menu
        self.fenetre.title("Unblock Sea")
        self.fenetre.wm_state('zoomed')
        self.hauteur = self.fenetre.winfo_screenheight()
        self.largeur = self.fenetre.winfo_screenwidth()

        self.frame = Frame(self.fenetre)  # creation d'une sous-fenetre dans la fenetre 
        self.frame.pack()

        self.canva = Canvas(self.frame, width=self.largeur, height=self.hauteur, bg=rgb(89, 163, 195)) # creation d'un canva dans cette sous fenetre
        self.canva.pack()

        self.plateau = None             # pas de niveau choisi donc pas de plateau genere
        self.listeVoiture = None        # pas de coord atribué
        self.nivSuivant = None          # pas de niveau suivant
        self.niveau_j=None

        #Musique et Timer
        self.musique=None
        self.coqui=0
        self.time=None

        # personnage intro
        self.crabe = PhotoImage(file="grosCrabe.png")
        self.fondChoix = PhotoImage(file="choix.png")
        self.crabeContent = PhotoImage(file="grosCrabeContent.png")

    def intro(self): # creation de la page d'explication
        self.canva.create_image(2 * self.largeur / 3 + 50, 2 * self.hauteur / 3, image=self.crabe)
        txt = "Bienvenue dans Unblock Sea !"
        self.canva.create_text(self.largeur / 2, (self.hauteur / 2) - 250, text=txt,
                               font='courrier 40 bold',
                               fill='white')

        txt = "La circulation dans l'océan est vraiment compliquée ...\nTu veux bien aider Louis le crabe à trouver son chemin ?"
        self.canva.create_text(self.largeur / 3, (self.hauteur / 2) - 100, text=txt, font='courrier 20', fill='white')

        go = Button(self.frame, text="C'est parti !", font='courrier 15', command=self.choix, bg='white')  # bouton pour allez choicir un niveau 
        go.place(x=self.largeur / 4, y=2 * self.hauteur / 3)   

    def effacer(self):  # efface la page d'introp
        for element in self.frame.winfo_children(): # kézako 
            if element != self.canva: # element qui fait pas parti du canva plateau
                element.destroy()

    def choix(self): # page de choix des niveaux
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveaux")
        self.canva.create_image(self.largeur / 2, self.hauteur / 2, image=self.fondChoix)
        self.canva.create_text(self.largeur / 2, (self.hauteur / 2) - 250, text="Choisis ton niveau !",
                               font='courrier 40 bold',
                               fill='white')
          # affichage des niveaux :
        self.nivFacile()
        self.nivInter()
        self.nivDiff()

    def nivFacile(self): # Mise en page des choix pour niveau facile 
        rect = self.canva.create_rectangle(100, (self.hauteur / 2) - 150, ((self.largeur - 300) / 3) + 100,
                                           self.hauteur - 100, outline='white', width=5)
        coord = self.canva.coords(rect)
        self.canva.create_text((coord[0] + coord[2]) / 2, coord[1] + 75, text="Facile", font='courrier 25',
                               fill='white')

        # bouton attribué à une fonction par level 
        niv11 = Button(self.frame, text="Niveau 1", font='courrier 15', bg='white', command=self.niveau11) 
        niv11.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 50)
        niv12 = Button(self.frame, text="Niveau 2", font='courrier 15', bg='white', command=self.niveau12)
        niv12.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 100)
        niv13 = Button(self.frame, text="Niveau 3", font='courrier 15', bg='white', command=self.niveau13)
        niv13.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 150)

    def nivInter(self): # idem niveau inter
        rect = self.canva.create_rectangle(((self.largeur - 300) / 3) + 150, (self.hauteur / 2) - 150,
                                           (2 * (self.largeur - 300) / 3) + 150, self.hauteur - 100, outline='white',
                                           width=5)
        coord = self.canva.coords(rect)
        self.canva.create_text((coord[0] + coord[2]) / 2, coord[1] + 75, text="Intermédiaire", font='courrier 25',
                               fill='white')
        niv21 = Button(self.frame, text="Niveau 1", font='courrier 15', bg='white', command=self.niveau21)
        niv21.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 50)
        niv22 = Button(self.frame, text="Niveau 2", font='courrier 15', bg='white', command=self.niveau22)
        niv22.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 100)
        niv23 = Button(self.frame, text="Niveau 3", font='courrier 15', bg='white', command=self.niveau23)
        niv23.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 150)

    def nivDiff(self): # idem niveau difficile
        rect = self.canva.create_rectangle((2 * (self.largeur - 300) / 3) + 200, (self.hauteur / 2) - 150,
                                           self.largeur - 300 + 200, self.hauteur - 100, outline='white', width=5)
        coord = self.canva.coords(rect)
        self.canva.create_text((coord[0] + coord[2]) / 2, coord[1] + 75, text="Difficile", font='courrier 25',
                               fill='white')
        niv31 = Button(self.frame, text="Niveau 1", font='courrier 15', bg='white', command=self.niveau31)
        niv31.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 50)
        niv32 = Button(self.frame, text="Niveau 2", font='courrier 15', bg='white', command=self.niveau32)
        niv32.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 100)
        niv33 = Button(self.frame, text="Niveau 3", font='courrier 15', bg='white', command=self.niveau33)
        niv33.place(x=(coord[0] + coord[2]) / 2 - 50, y=(self.hauteur / 2) + 150)

    def niveau(self):
        for i in range(len(self.listeVoiture)):  # pour tous les voiture 
            self.listeVoiture[i].dessiner(self.plateau) # les dessiner 
        
        
        # lancer la musique 
        self.musique=Musique(self.canva,self.largeur - 200, 100)

        choix = Button(self.frame, text="Choisir un autre niveau", font='courrier 15', bg='white', command=self.choix ) # Bouton pour quitter le jeu
        choix.place(x=self.largeur - 250, y=10)
        
        # lancer le Timer
    
        self.time=Timer(self.plateau.canva, self.plateau.debut / 6 +20, 100, self.plateau.debut + self.plateau.cote / 2-100, self.hauteur / 2, self.coqui)
        


    def niveau11(self): # mise en place du niv 1 Facile
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 1 (facile)")
        self.plateau = Plateau(self.canva)                      # création du plateau sur la canva
        self.listeVoiture = Niveaux().facile(self.plateau)[0]   # attribution des position des voitures
        self.niveau()                                          #enclenché le jeu
        self.niveau_j=self.niveau11 
        self.nivSuivant = self.niveau12                         # attribution du niveau suivant 

    def niveau12(self): # mise en place du niv 2 Facile
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 2 (facile)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().facile(self.plateau)[1]
        self.niveau()
        self.niveau_j=self.niveau12 
        self.nivSuivant = self.niveau13

    def niveau13(self): # mise en place du niv 3 Facile
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 3 (facile)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().facile(self.plateau)[2]
        self.niveau()
        self.niveau_j=self.niveau13 
        self.nivSuivant = self.niveau21

    def niveau21(self): # mise en place du niv 1 Intermédiaire
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 1 (intermédiaire)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().intermediaire(self.plateau)[0]
        self.niveau()
        self.niveau_j=self.niveau21 
        self.nivSuivant = self.niveau22

    def niveau22(self):  # mise en place du niv 2 Intermédiaire
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 2 (intermédiaire)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().intermediaire(self.plateau)[1]
        self.niveau()
        self.niveau_j=self.niveau22
        self.nivSuivant = self.niveau23

    def niveau23(self):  # mise en place du niv 3 Intermédiaire
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 3 (intermédiaire)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().intermediaire(self.plateau)[2]
        self.niveau()
        self.niveau_j=self.niveau23
        self.nivSuivant = self.niveau31

    def niveau31(self):  # mise en place du niv 1 Difficile
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 1 (difficile)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().difficile(self.plateau)[0]
        self.niveau()
        self.niveau_j=self.niveau31
        self.nivSuivant = self.niveau32

    def niveau32(self):  # mise en place du niv 2 Difficile
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 2 (difficile)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().difficile(self.plateau)[1]
        self.niveau()
        self.niveau_j=self.niveau32
        self.nivSuivant = self.niveau33

    def niveau33(self):  # mise en place du niv 3 Difficile
        self.effacer()
        self.fenetre.title("Unblock Sea - Niveau 3 (difficile)")
        self.plateau = Plateau(self.canva)
        self.listeVoiture = Niveaux().difficile(self.plateau)[2]
        self.niveau()
        self.niveau_j=self.niveau33
        self.nivSuivant = None

    def resolu(self): # affichafe du panneau fin de la paretie

        #self.time.txt.place_forget()
        # affichage des coquillages
        
        self.canva.create_rectangle(self.plateau.debut, 0, self.plateau.debut + self.plateau.cote, self.plateau.cote,
                                    fill=rgb(89, 163, 195), outline=rgb(89, 163, 195))

        if self.time.reussite==-1:
            
            txt3 = "tu as mis trop de temps,\n Louis s'est mis à pleurer, \n essaie de nouveau !"

            self.canva.create_text(self.plateau.debut + self.plateau.cote / 2, (self.hauteur / 2) - 150, text=txt3,
                                    font='courrier 20',
                                    fill='white')
            suivant = Button(self.frame, text="Recommençons", font='courrier 15', bg='white', command=self.niveau_j)
            suivant.place(x=self.plateau.debut + 30, y=(self.hauteur / 2) + 150)

            self.plateau.canva.image.append(self.crabe)
            self.canva.create_image(2 * self.largeur / 3 + 50, 2 * self.hauteur / 3, image=self.crabe)
        else:
            self.time.stop=True # arret timer 
            
            self.coqui=self.time.coquillage()

            txt1 = "Bravo !\nTu as libéré Louis le crabe !"
            self.canva.create_text(self.plateau.debut + self.plateau.cote / 2, self.hauteur / 7, text=txt1,
                               font='courrier 35 bold',
                               fill='white')
            if self.nivSuivant != None:  # Si le niveau suivant existe 
                txt2 = "Tu peux maintenant passer au niveau suivant, ou\nchoisir un autre niveau."
                self.canva.create_text(self.plateau.debut + self.plateau.cote / 2, (self.hauteur / 2) - 150, text=txt2,
                                    font='courrier 20',
                                    fill='white')
                suivant = Button(self.frame, text="Au suivant !", font='courrier 15', bg='white', command=self.nivSuivant)
                suivant.place(x=self.plateau.debut + 30, y=(self.hauteur / 2) + 150)
            else:  # si le niveau suivant existe pas
                txt2 = "Tu as terminé le jeu ! Si tu es téméraire, tu peux\nrecommencer et finir chaque niveau le plus\nrapidement possible.\nMerci d'avoir joué !                                             "
                self.canva.create_text(self.plateau.debut + self.plateau.cote / 2, (self.hauteur / 2) - 100, text=txt2,
                                    font='courrier 20',
                                    fill='white')
                recommencer = Button(self.frame, text="C'est reparti !", font='courrier 15', bg='white',
                                    command=self.niveau11)
                recommencer.place(x=self.plateau.debut + 30, y=(self.hauteur / 2) + 150)

            self.plateau.canva.image.append(self.crabeContent)
            self.canva.create_image(2 * self.largeur / 3 + 50, 2 * self.hauteur / 3, image=self.crabeContent)


            
