""" lien Git: https://github.com/MoussaELI/TP-CSdev-JEU-Pendu.git """

"""
Date: 03/12/2020

@author: EL IDRISSI Moussa 3ETI

Statut: fini
"""


from donnees import *
from fonctions import *

continuer_partie = "oui"

while continuer_partie != "non":
    mot_recherché = mot_aléatoire()
    lettres_trouvées = []
    affichage = affichage_en_cours_de_partie(mot_recherché,lettres_trouvées)
    while nb_chance != 0 and mot_recherché != affichage:
        print(affichage , "il vous reste" , nb_chance , "chances")
        lettre = lettre_proposée()
        if lettre in lettres_trouvées:
            print("vous ne pouvez pas proposer deux fois la même lettre")
        elif lettre in mot_recherché:
            lettres_trouvées.append(lettre)
            print("cette lettre est correcte")
        else:
            nb_chance += (-1)
            print("cette lettre n'est pas correcte, il vous reste" , nb_chance , "chances" )
        affichage = affichage_en_cours_de_partie(mot_recherché,lettres_trouvées)
        
    if affichage == mot_recherché:
        print("WINNER ! Bravo vous avez deviné le mot et vous avez gagné... rien")
    else:
        print("GAME OVER LOOSER ! il ne vous reste 0 chances... Le mot était:" , mot_recherché )
    
    continuer_partie = str (input("Retenter sa chance ? (oui/non)"))
    