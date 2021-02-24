from Plateau_v2 import *
from Voiture_v2 import *

plateau = Plateau()

v1 = Voiture(1,3,"vertical")
v1.v_dessin(plateau.z_dessin,plateau.p_cote,plateau.f_largeur)

plateau.fenetre.bind("<Button-1>",Voiture.clic)
plateau.fenetre.bind("<ButtonRelease-1>",Voiture.pas_clic)
plateau.fenetre.bind("<Motion>",Voiture.s_position)
    
plateau.fenetre.mainloop()