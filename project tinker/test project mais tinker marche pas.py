import tkinter as tk
import random

# Initialiser la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Jeu du pendu")
label = tk.Label(fenetre, text="Bienvenue dans le jeu du pendu", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget
fenetre.geometry(500*500)
fenetre.mainloop()

# Définir la liste de mots pour le jeu
liste_mots = ["correction", "opportuniste", "ascenseur", "evrest", "situation", "saturation", "programmeur","aviateur","musicien"]

# Choisir un mot aléatoire de la liste
mot_a_deviner = random.choice(liste_mots)

# Initialiser les variables du jeu
lettres_trouvees = []
lettres_manquees = []
nb_essais = 9

# Fonction pour afficher le mot caché avec les lettres déjà trouvées



def appui_a(event):
    print("Tu as appuyé sur la touche b")

def relache_a(event):
    print("Tu as relâché la touche b")
    
def affichage(event):
    print("toto")

fenetre.bind("<KeyPress-b>", appui_a)
fenetre.bind("<KeyRelease-b>", relache_a)
fenetre.bind("<Button-1>", affichage)


#truc dans el cour mais pas sur d'avoir compris