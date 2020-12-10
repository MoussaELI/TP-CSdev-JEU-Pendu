""" lien Git: https://github.com/MoussaELI/TP-CSdev-JEU-Pendu.git """

"""
Date: 10/12/2020

@author: EL IDRISSI Moussa 3ETI

Statut: fini
"""

""" on importe les ressources nécéssaires """
from tkinter import Tk, Label, Button, PhotoImage, Menu, Entry, StringVar, Canvas
from classe import mot_aleatoire, jeu_du_pendu


""" on vérifie avec cette fct si la lettre proposée est dans le mot recherché """
def check_lettre(lettre_proposee):
    lettre_proposee.mot_aff = ""
    lettre_proposee.Chance = 8
    for lettre in lettre_proposee.mot_au_hasard :
        if lettre in lettre_proposee.liste_lettre : 
            lettre_proposee.mot_aff += " " + lettre
        else :
            lettre_proposee.mot_aff += " " + "_"
    for lettre in lettre_proposee.liste_lettre :
        if lettre not in lettre_proposee.mot_au_hasard :
            lettre_proposee.Chance -= 1
    image_en_jeu(lettre_proposee) 
    mot_en_jeu(lettre_proposee)
    Nombre_chances(lettre_proposee)

""" on prend en considération la lettre que le joueur propose """
def lettre_proposed(lettre,proposee):
    if len(lettre) == 1: 
        proposee.liste_lettre.append(lettre)
        check_lettre(proposee)
        
  
        
""" on affiche le mot en cours de partie selon les choix du joueur """
def mot_en_jeu(proposee):
    MotRecherchEnJeu = Label(proposee.fenetre,
                             text = proposee.mot_aff,
                             fg='white',
                             bg='grey'
                             )
    MotRecherchEnJeu.place(x=200 , y=200 , width=200 , height=20)
  
    
  
""" on affiche le nombre de chance restantes """
def Nombre_chances(proposee):
    Nombre_chances = Label(proposee.fenetre ,
                           text='Chances restantes : ' +
                           str(proposee.Chance) ,
                           bg='grey',
                           fg='white', 
                           font=100
                           )
    Nombre_chances.place(x=400, y=200, width=200, height=20)
    
    

""" on affiche l'image du pendu en cours de partie selon les choix du joueur """
def image_en_jeu(proposee):
    H = 300
    L = 300
    image = Canvas(proposee.fenetre) 
    image.create_image(0,0, anchor = 'nw', image = proposee.liste_image[proposee.Chance-1])
    image.place(x=800, y=200, width=L, height=H)
    
    
    
    




""" FONCTION PRINCIPALE: pendu avec interface graphique """

def jeu_pendu():
    
    
    
    """ fenetre principale : """
    fenetre = Tk()
    fenetre.title('LE JEU DU PENDU (avec interface) ')
    fenetre.geometry('1280x720')

    proposee = jeu_du_pendu(fenetre)
    check_lettre(proposee)



    """ widget menu : """
    menubar = Menu(fenetre)
    menuoption = Menu(menubar,tearoff =0)
    menuoption.add_command(label="Rejouer", command = jeu_pendu) # boutton pour rejouer
    menuoption.add_command(label="Quitter", command = fenetre.destroy) # boutton pour arreter de jouer 
    menubar.add_cascade(label="Option", menu = menuoption)



    """ affichage menu : """
    fenetre.config(menu = menubar)



    """ fond : """
    Fond = Canvas(fenetre, bg='grey')
    Fond.place(x=0, y=0, width=1280, height=720)


    
    """ texte : Proposez un lettre : """
    Lettre = Label(fenetre, text='Proposez un lettre',bg='grey', fg='white')
    Lettre.place(x=20, y=330, width=100, height=50)



    """ zone de saisie de texte pour que le joueur tape une lettre """
    lettre_prop = StringVar()
    Champ = Entry(fenetre, textvariable = lettre_prop, bg='white', fg='black')
    Champ.focus_set()
    Champ.place(x=130, y=350, width=100, height=20)



    """ boutton pour soumettre la lettre proposee : """
    BouttonSoumettre = Button (fenetre,
                               text="Soumettre" ,
                               fg ='grey' ,
                               bg='red' ,
                               command = lambda: lettre_proposed(lettre_prop.get() , proposee)
                               ) 
    BouttonSoumettre.place(x=250, y=350, width=100, height=20)

    mot_en_jeu(proposee)


    
    """ on affiche sur la fenetre le nombre de chances restantes et de l'image du pendu en fonction des choix : """
    Nombre_chances(proposee) 
    image_en_jeu(proposee)



    """ boutton quitter le jeu : """
    boutton_quitter = Button (fenetre, text="QUITTER LE JEU",
                              fg ='grey',
                              bg='red',
                              command = fenetre.destroy
                              )
    boutton_quitter.place(x=20, y=600, width=100, height=50)

    fenetre.mainloop()
               
    
    
        