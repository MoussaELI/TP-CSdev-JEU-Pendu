""" lien Git: https://github.com/MoussaELI/TP-CSdev-JEU-Pendu.git """

"""
Date: 10/12/2020


@author: EL IDRISSI Moussa 3ETI

Statut: fini
"""


from tkinter import PhotoImage
import random as rd


""" depuis notre base de données mots.txt, cette fct récupère un mot aléatoire """
def mot_aleatoire():
    fichier=open('mots.txt','r' , encoding="utf-8")
    lignes = fichier.readlines()
    nb_aleatoire = rd.randint(0,len(lignes))
    fichier.close()
    return (lignes[nb_aleatoire].strip('\n'))

class jeu_du_pendu:
    def __init__(self, fenetre):
        self.mot_au_hasard = mot_aleatoire() 
        self.liste_lettre = [self.mot_au_hasard[0]]
        self.mot_aff = ""
        self.fenetre = fenetre
        self.Chance = 8
        
        self.photo1 = PhotoImage(file='bonhomme1.gif')
        self.photo2 = PhotoImage(file='bonhomme2.gif')
        self.photo3 = PhotoImage(file='bonhomme3.gif')
        self.photo4 = PhotoImage(file='bonhomme4.gif')
        self.photo5 = PhotoImage(file='bonhomme5.gif')
        self.photo6 = PhotoImage(file='bonhomme6.gif')
        self.photo7 = PhotoImage(file='bonhomme7.gif')
        self.photo8 = PhotoImage(file='bonhomme8.gif')
        
        self.liste_image = [self.photo8,
                            self.photo7,
                            self.photo6,
                            self.photo5,
                            self.photo4,
                            self.photo3,
                            self.photo2,
                            self.photo1
                            ]