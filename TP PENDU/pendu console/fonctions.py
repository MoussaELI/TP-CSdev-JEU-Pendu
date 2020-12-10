""" lien Git: https://github.com/MoussaELI/TP-CSdev-JEU-Pendu.git """

"""
Date: 03/12/2020

@author: EL IDRISSI Moussa 3ETI

Statut: fini
"""

import random


""" fct qui prend un mot aléatoire du fichier mots.txt """
def mot_aléatoire():
    fichier=open('mots.txt','r' , encoding="utf-8")
    lignes = fichier.readlines()
    nb_aléatoire = random.randint(0,len(lignes))
    fichier.close()
    return (lignes[nb_aléatoire].strip('\n'))


""""fct qui reccupère la lettre proposée"""
def lettre_proposée():
    lettre = input("proposez une lettre: ")
    return lettre



"""affichage du mot qui est en train d'etre deviné en cours de partie"""
def affichage_en_cours_de_partie(mot_choisi,lettres_trouvées):
    mot_recherché = ""
    for l in mot_choisi:
        if l in lettres_trouvées:
            mot_recherché += l
        else:
            mot_recherché +="_"
    return mot_recherché
    








