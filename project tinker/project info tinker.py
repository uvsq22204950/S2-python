import tkinter as tk
import random

# Initialiser la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu du pendu")
label = tk.Label(fenetre, text="Bienvenue dans le jeu du pendu", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget
fenetre.geometry(500*500) #test de grandeur fenetre mais cela ne marche pas
fenetre.mainloop()#lancé la boucle pour pouvoir avoir la fenfetre

# Définir la liste de mots pour le jeu
liste_mots = ["correction", "opportuniste", "ascenseur", "evrest", "situation", "saturation", "programmeur","aviateur","musicien"]

# Choisir un mot aléatoire de la liste
mot_a_deviner = random.choice(liste_mots)

# Initialiser les variables du jeu
lettres_trouvees = []
lettres_manquees = []
essaies = 9

def penduTick(trouvenomvariable, event = None) : #Le code sur lequel Aaron ta aidé éssai de comprendre quand meme

        if trouvenomvariable.essaies > 0 and not trouvenomvariable.win: #Si on a encore des essaies et qu'on n'a pas encore gagné
            
            #On récupère ce que le joueur à entrée
            trouvenomvariable.congratsLabel.configure(text = "")
            guess = trouvenomvariable.guessEntry.get()
            trouvenomvariable.guessEntry.delete(0, len(guess))
            if len(guess) != 1 :
                guess = ""
                trouvenomvariable.congratsLabel.configure(text = "Input only 1 character")
            for c in guess.lower() : #On vérifie si la lettre correspond à une lettre du mot (les lettres qui correspondent ne font pas perdre d'essaies)
                #On peut rentré plusieurs lettres d'un coup: si le joueur rentre "lfpoeqys", sa va regarder pour toutes ces lettre si elle est dans le mot.
                #On perd aussi plus d'essaies si on met plein de lettres qui ne sont pas dans le mot.
                if c in trouvenomvariable.motC.lower() :
                    if c not in trouvenomvariable.lettresTrouves : #Si la lettre est dans le mot, 
                        trouvenomvariable.lettresTrouves.append(c)
                else :
                    try :
                        int(c)
                    except :
                        trouvenomvariable.essaies -= 1 #Mauvaise lettre ? Un essaie en moins et on dessine le pendu un peu plus
                        trouvenomvariable.drawNext()