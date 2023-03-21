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
nb_essais = 9

def penduTick(self, event = None) : #Le code sur lequel Aaron ta aidé éssai de comprendre quand meme

        if self.essaies > 0 and not self.win: #Si on a encore des essaies et qu'on n'a pas encore gagné
            
            #On récupère ce que le joueur à entrée
            self.congratsLabel.configure(text = "")
            guess = self.guessEntry.get()
            self.guessEntry.delete(0, len(guess))
            if len(guess) != 1 :
                guess = ""
                self.congratsLabel.configure(text = "Input only 1 character")
            for c in guess.lower() : #On vérifie si la lettre correspond à une lettre du mot (les lettres qui correspondent ne font pas perdre d'essaies)
                #On peut rentré plusieurs lettres d'un coup: si le joueur rentre "abcdefg", sa va regarder pour toutes ces lettre si elle est dans le mot.
                #On perd aussi plus d'essaies si on met plein de lettres qui ne sont pas dans le mot.
                if c in self.motC.lower() :
                    if c not in self.lettresTrouves : #Si la lettre est dans le mot, 
                        self.lettresTrouves.append(c)
                else :
                    try :
                        int(c)
                    except :
                        self.essaies -= 1 #Mauvaise lettre ? Un essaie en moins et on dessine le pendu un peu plus
                        self.drawNext()