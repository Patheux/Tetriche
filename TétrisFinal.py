## Entête
#                                           #
# Jeu: Tetris                               #
#                                           #
#                                           #
# Projet Informatique: Projet de I2         #

## Importation de tous les modules

from tkinter import*                    # pour l'affichage
from random import*                     # pour le choix des pieces et des couleurs
import tkinter.font as tkFont           # pour les polices d'écritures
from os import chdir                    # pour pouvoir importer des images

## Variables

#TODO: modifier la direction des fichiers, en fonction de l'endoit sur votre ordinateur ;-)

chdir("D:\INFO\Projet\Mise en forme")      # on pose ici la direction de nos fichiers

PIECE = 2       #vous découvrirez l'utilisation de ces variables assez vite ;-)
BLOC = 1
VIDE = 0

##Classes

class Menu():
    def __init__(self):                                     #fenetre d'introduction au jeu, permet au joueur de se préparer à jouer
        self.MENUfenetre = Tk()
        self.MENUfenetre.title('Tétris Menu')
        self.MENUfenetre['bg']='black'

        self.Menu=Canvas(self.MENUfenetre,height=1062,width=1534)
        self.Menu.pack(side = LEFT, padx = 10, pady = 10)
        self.image=PhotoImage(file="Menu.png", master=self.Menu)
        self.Menu.create_image(0,0,anchor=NW,image=self.image)                # Affichage du fond pour les menus

        self.Commandes=Canvas(self.MENUfenetre,height=1100,width=40)          # commandes et boutons apparents (fonction bouton)
        self.Commandes.pack(side = LEFT, padx = 0, pady = 10)
        self.Bouton()

        self.MENUfenetre.mainloop()

    def Bouton (self):
        police = tkFont.Font(family='Helvetica', size=36, weight='bold')

        bouton_jouer=Button(self.Commandes,command=self.jouer, bg='black', font = police, text="Play", fg='yellow') # bouton permettant de lancer le jeu
        bouton_jouer.configure(height=10, width=15, relief = FLAT, overrelief = RIDGE)
        bouton_jouer.pack(side= BOTTOM,padx=0,pady=0)

        bouton_quitter=Button(self.Commandes,command=self.MENUfenetre.destroy,bg='red', font = police, text="X", fg='white') # bouton permettant de quitter le programme
        bouton_quitter.configure(height=10, width=15, relief = SUNKEN, overrelief = RAISED)
        bouton_quitter.pack(side = TOP, padx=0, pady=0)

    def jouer (self) :
        self.MENUfenetre.destroy()
        Panoramix=Programme()


class Programme():
    def __init__ (self):
        ## Les variables de définition

        self.taille=50 # variable fixant la taille d'un carreau du grillage (on peut l'agrandir ou la rétrécir)

        self.delai=400
        self.delai_start=300

        self.Compteur_Final = 0                                                         # latence des boucles futures (fonction descente)

        l=0 #variables pour les compteur lignes (l) et colonnes (c)
        c=0

        self.a=0 #repère axe des ordonnées
        self.b=4 #repère axe des abscisses
        self.r=0 #repère de rotation (allant de 0 à 3)

        ## la fenêtre principale
        self.fenetre = Tk()
        self.fenetre.title('Tétris')
        self.fenetre['bg']='black'
                                                                                # ici vient s'ajouter le module de jeu
        self.Jeu= Canvas(self.fenetre,height=20*self.taille,width=10*self.taille)
        self.Jeu.pack(side = LEFT, padx = 200, pady = 10)

        ## La Grille

        self.Grille1 = self.grille()

        self.k = [[0,0,0,0,0,0,0,0,0,0],            # constante pour chaque carreau qui permet de voir si il est occupé, plein, et la couleur de celui-ci
            [0,0,0,0,0,0,0,0,0,0],                                              # de plus, on pose les coordonnées: k[ligne][colonnes]
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1]]

        for ligne in self.k:
            for i in range(len(ligne)):
                ligne[i] = [ligne[i], 0]

        ## Fenêtre des Scores

        police = tkFont.Font(family='Helvetica', size=36, weight='bold')

        self.Score = Canvas(self.fenetre, height=100, width=600, bg='black')
        self.Score.pack(side = TOP, padx = 10, pady = 10)

        self.texte = self.Score.create_text((235,50), font=police, text="Nombre de pièces : ", fill='yellow')

        self.chiffre= self.Score.create_text((490,50), font=police, text=str(self.Compteur_Final), fill='yellow')

       ## Fenêtre des Règles

        self.Regle = Canvas(self.fenetre, height=853 , width=752, bg='black')
        self.Regle.pack(side=BOTTOM, padx=100, pady=10)
        self.image_regles=PhotoImage(file="regle.png", master=self.Regle)
        self.Regle.create_image(0,0,anchor=NW,image=self.image_regles)

        ## Les Touches
        self.Jeu.focus_set()
        self.Jeu.bind("<Escape>",self.touches)

        self.Jeu.bind('<Up>',self.touches)
        self.Jeu.bind('<Down>',self.touches)

        self.Jeu.bind('<Right>',self.touches)
        self.Jeu.bind('<Left>',self.touches)

        ## Insertion des fonctions

    # Début de jeu:
        self.pieces()
        self.creation_piece()
    # Boucle du jeu
        self.descente()

        self.fenetre.mainloop()

## Les Fonctions

    def CompteurFinal(self):
            self.Compteur_Final=self.Compteur_Final+1
            #print(self.Compteur_Final)
            self.Score.itemconfig(self.chiffre,text=str(self.Compteur_Final))

    def touches(self,event): # on programme toutes les touches en vue d'un usage futur

        touches = event.keysym

        if touches == "Escape":
            self.Retour_Menu()

        if touches == "Right":
            self.droite()

        if touches == "Left":
            self.gauche()

        if touches == "Down":
            self.delai=self.delai-10
            #print (self.delai)

        if touches == "Up":
            self.rotation()
            #print(self.r)


    def grille (self):                                                    # fonction pour la création de la grille
        for i in range (0,10):
            for j in range (0,20):
                self.carreau=self.Jeu.create_rectangle(i*self.taille,j*self.taille,(i+1)*self.taille,(j+1)*self.taille,fill="#FFFFFF")

    def type(self):
        self.I=[[[self.a,self.b-1],[self.a,self.b],[self.a,self.b+1],[self.a,self.b+2]],       #barre                   # création de chaque pièces ainsi que tirage de chacunes.
                [[self.a+3,self.b],[self.a+2,self.b],[self.a+1,self.b],[self.a,self.b]],                                # on fait un index : [nbre du carré][ligne(0) ou colonnes(1)]
                [[self.a,self.b-1],[self.a,self.b],[self.a,self.b+1],[self.a,self.b+2]],
                [[self.a+3,self.b],[self.a+2,self.b],[self.a+1,self.b],[self.a,self.b]]
                ]
        self.J=[[[self.a,self.b-1],[self.a+1,self.b-1],[self.a+1,self.b],[self.a+1,self.b+1]],   #L
                [[self.a+2,self.b],[self.a+1,self.b],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+1,self.b+1],[self.a,self.b-1],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+2,self.b],[self.a+2,self.b+1],[self.a+1,self.b+1],[self.a,self.b+1]]
                ]
        self.L=[[[self.a+1,self.b-1],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b+1]],  #L inversé
                [[self.a+2,self.b],[self.a+2,self.b+1],[self.a+1,self.b],[self.a,self.b]],
                [[self.a+1,self.b-1],[self.a,self.b-1],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+2,self.b+1],[self.a+1,self.b+1],[self.a,self.b+1],[self.a,self.b]]
                ]
        self.O=[[[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b],[self.a,self.b+1]],      #carré
                [[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b],[self.a,self.b+1]]
                ]
        self.S=[[[self.a+1,self.b-1],[self.a+1,self.b],[self.a,self.b],[self.a,self.b+1]],      # Z inversé
                [[self.a+2,self.b+1],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b]],
                [[self.a+1,self.b-1],[self.a+1,self.b],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+2,self.b+1],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b]]
                ]
        self.T=[[[self.a+1,self.b-1],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b]],    # T inversé
                [[self.a+2,self.b],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b]],
                [[self.a+1,self.b],[self.a,self.b-1],[self.a,self.b],[self.a,self.b+1]],
                [[self.a+2,self.b],[self.a+1,self.b],[self.a+1,self.b-1],[self.a,self.b]],
                ]

        self.Z=[[[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b-1],[self.a,self.b]],      # Z
                [[self.a+2,self.b],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b+1]],
                [[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b-1],[self.a,self.b]],
                [[self.a+2,self.b],[self.a+1,self.b],[self.a+1,self.b+1],[self.a,self.b+1]],
                ]


    def pieces (self): #cette fonction permet de faire le tirage au sort de la pièce qui va apparaitre ainsi que de sa couleur
        self.type()
        couleurs = 'blue', 'grey', 'red', 'green'

        self.liste_pieces=[self.I,self.J,self.L,self.O,self.S,self.T,self.Z]

        self.sortie=randint(0,len(self.liste_pieces)-1)                               # tirage au sort du type de pièce
        self.couleur=choice(couleurs)                                                 # on choisit la couleur du bloc au hasard

    def creation_piece (self): # permet de faire apparaitre la pièce à un point dans le repère et dans la grille
        self.type()
        self.liste_pieces=[self.I,self.J,self.L,self.O,self.S,self.T,self.Z]

        #self.M=self.I #permet de visualiser simplement la partie destruction.

        self.M = self.liste_pieces[self.sortie]

        for i in range(4):
            l = self.M[self.r][i][0]
            c = self.M[self.r][i][1]
            self.k[l][c] = [PIECE, self.Jeu.create_rectangle((c)*self.taille,(l)*self.taille,(c+1)*self.taille,(l+1)*self.taille,fill=self.couleur,tag='piecemouv')]

    def destruction_piece (self): #permet de supprimer la pièce mobile du repère et de la grille pour pouvoir la déplacer plus facilement
        for l in range(len(self.k)-1, -1, -1):
            for c in range(len(self.k[l])):
                type, carre = self.k[l][c]
                if type == PIECE :
                    self.Jeu.delete('piecemouv')
                    self.k[l][c] = [VIDE, 0]

    def rotation(self):
            self.r=(((self.r)+1) % 4)       # permet de définir un indice de rotation toujours compris entre 0 et 3 (congruences: modulo 4)
            self.destruction_piece()        # une fois le nouvel indice posé, on supprime l'ancienne  pièce pour imprimer la nouvelle
            self.creation_piece()

    def peut_descendre (self):  # permet de vérifier que le bloc ne sortira pas de la griller (comme toutes les fonctions de type "peut")
        if (self.a)==20:
            return False

        for l in range(len(self.k)):
            for c in range(len(self.k[l])):
                if self.k[l][c][0] == PIECE and self.k[l+1][c][0] == BLOC : # on termine la grille en bas avec une ligne de BLOC qui permet d'indiquer la fin de la grille
                    return False
        return True

    def peut_droite (self):
        self.type()

        if self.M[self.r] in [self.I[0] , self.I[2]]:
            if (self.b+3) == 10:
                return False
            else:
                return True

        elif self.M[self.r] in [self.I[1] , self.I[3] , self.T[3]]:
            if (self.b+1) >= 10:
                return False
            else:
                return True

        elif self.M[self.r] in [self.J[0] , self.J[1] , self.J[2] , self.J[3] , self.L[0] , self.L[1] , self.L[2] , self.L[3] , self.O[0] , self.S[0] , self.S[1] , self.S[2] , self.S[3] , self.T[0] , self.T[1] , self.T[2] , self.Z[0] , self.Z[1] , self.Z[2] , self.Z[3]]:
            if (self.b+2) >= 10:
                return False
            else:
                return True

        else:
            for l in range(len(self.k)):
                for c in range(len(self.k[l])):
                    if self.k[l][c][0]==PIECE and self.k[l][c+1][0]==BLOC:
                        return False

    def peut_gauche (self):
        self.type()

        if self.M[self.r] in [self.I[0] , self.I[2] , self.J[0] , self.J[1] , self.L[0] , self.L[2] , self.S[1] , self.T[0] , self.T[2] , self.T[3] , self.Z[0] , self.Z[2]]:
            if (self.b-1) <= 0:
                return False
            else:
                return True

        elif self.M[self.r] in [self.I[1] , self.I[3] , self.J[2] , self.J[3] , self.O[0] , self.L[1] , self.L[3] , self.S[1] , self.S[2] , self.S[3] , self.T[1] , self.Z[1] , self.Z[3]]:
            if (self.b) <= 0:
                return False
            else:
                return True
        else:
            for l in range(len(self.k)):
                for c in range(len(self.k[l])):
                    if self.k[l][c][0]==PIECE and self.k[l][c-1][0]==BLOC:
                        return False
                    else:
                        return True

    def droite (self):                  # on fait bouger le point de repère de l'impression des pièces avec self.b , on détruit et on réimprime le tout
        if self.peut_droite():
            self.destruction_piece()
            self.b=self.b+1
            self.creation_piece()

    def gauche (self):                  # même fonctionnement que la fonction droite
        if self.peut_gauche():
            self.destruction_piece()
            self.b=self.b-1
            self.creation_piece()

    def detruire_ligne (self):          # on vérifie tout d'abord que la ligne est belle et bien pleinne
        destruction=False
        self.compteur=0
        for self.compteur in range (len(self.k)-2, -1, -1):
            somme=0
            for c in range(len(self.k[self.compteur])):
                if self.k[self.compteur][c][0]==BLOC:
                    somme=somme+1
                if somme==10: # si la ligne est pleinne, on supprime le carrée de la matrice k et de la grille d'affichage, ligne par ligne, colonne par colonne
                    for c in range (len(self.k[self.compteur])):
                        self.k[0][c][0]=VIDE

                    for c in range (len(self.k[self.compteur])): #ici, on fait redescendre les cubes présents au dessus
                        self.Jeu.delete(self.k[self.compteur][c][1])
                    for l in range ((self.compteur)-1,0,-1):
                        for c in range (len(self.k[self.compteur-1])):
                            self.k[l+1][c]=self.k[(l)][c]
                            self.Jeu.move(self.k[l][c][1],0,self.taille)



    def descente (self):

        self.detruire_ligne() # on applique la fonction de vérification et destruction des lignes, à chaque nouveau déplacement

        for ligne in self.k: #print(ligne)                          # permet de visionner les erreurs vues par le passé
            perdu = False

        if self.peut_descendre():
            #print("Descente")
            self.destruction_piece()
            self.a=(self.a)+1
            #print (self.a)
            self.creation_piece()

        else:   #print("Blocage")
            for l in range(len(self.k)):
                for c in range(len(self.k[l])):
                    type, carre = self.k[l][c]
                    if type == PIECE :
                        self.Jeu.itemconfig(carre, tag='piecefixe') #on change le tag de la pièce pour ne pas qu'il soit supprimé ultérieurement
                        self.k[l][c] = [BLOC, carre]

                        if l < 3:
                            perdu = True
            if not perdu:                                       # si on n'a pas perdu, il relance une nouvelle pièce
                self.a=0
                self.b=4
                self.r=0
                self.delai=self.delai_start
                self.pieces()
                self.creation_piece()
                self.CompteurFinal()

        if perdu:                                               # si on a perdu, il lance l'animation de fin (ultime pièce) et coupe le jeu
            self.a=0
            self.b=5
            self.delai=self.delai_start
            self.pieces()
            self.creation_piece()
            self.fin_du_jeu()
        else:                                                   # si la pièce est en cours de descente, il met un temps de pause, pour que le joueur puisse voir la pièce descendre et reprend la descente
            self.Jeu.after(self.delai,self.descente)

    def fin_du_jeu(self):
        self.fenetre.destroy()
        Panoramix=Fin()

    def Retour_Menu(self):
        self.fenetre.destroy()
        Panoramix=Menu()

class Fin():                                                    # rien de particulié, simplement de la mise en page et 1 bouton
    def __init__(self):
        self.FINfenetre = Tk()
        self.FINfenetre.title('Tétris FIN')
        self.FINfenetre['bg']='black'

        self.End=Canvas(self.FINfenetre,height=1062,width=1534)
        self.End.pack(side = LEFT, padx = 10, pady = 10)

        self.image=PhotoImage(file="Tétriche.png", master = self.End)              # affichage de la fenetre de fin
        self.End.create_image(0,0,anchor=NW,image=self.image)

        self.Commandes_Triche=Canvas(self.FINfenetre,height=1200,width=90)
        self.Commandes_Triche.pack(side = RIGHT, padx = 10, pady = 10)
        self.Bouton_Triche()

        self.FINfenetre.mainloop()

    def Bouton_Triche (self):
        police = tkFont.Font(family='Helvetica', size=52, weight='bold')

        bouton_menu=Button(self.Commandes_Triche,command=self.fonct_menu, bg='black', font = police, text="Menu", fg='orange')
        bouton_menu.configure(height=5, width=15, relief = RIDGE, overrelief = SUNKEN)
        bouton_menu.pack(side=TOP, padx=0, pady=0)

        bouton_tricher=Button(self.Commandes_Triche,command=self.triche, bg='black', font = police, text="?", fg='yellow')
        bouton_tricher.configure(height=5, width=15, relief = FLAT, overrelief = RIDGE)
        bouton_tricher.pack(side=BOTTOM, padx=0, pady=0)

    def triche(self):
        self.FINfenetre.destroy()
        Panoramix=Triche()

    def fonct_menu(self):
        self.FINfenetre.destroy()
        Panoramix=Menu()

class Triche ():                                                # ultime page du jeu
    def __init__(self):
        self.TRICHEfenetre = Tk()
        self.TRICHEfenetre.title('Tétris FIN')
        self.TRICHEfenetre['bg']='black'

        self.Triche=Canvas(self.TRICHEfenetre,height=1062,width=1534)
        self.Triche.pack(side = LEFT, padx = 150, pady = 10)

        self.image=PhotoImage(file="TétricheFIN.png", master=self.Triche)
        self.Triche.create_image(0,0,anchor=NW,image=self.image)

        self.TRICHEfenetre.mainloop()

## Lancement du Jeu

Panoramix= Menu()                                                                       # pour le jeu on commencera par le menu:
