# Importation des bibliothèques nécessaires
import customtkinter as ctk

import random

# Configuration du thème de l'application
ctk.set_appearance_mode("dark")  # Mode sombre
ctk.set_default_color_theme("blue")  # Thème bleu

# Liste des questions avec réponses et choix
questions = [
    {"q": "Quel composant exécute les instructions ?", "r": "Processeur", "choix": ["RAM", "Processeur", "Carte mère", "Disque dur"]},
    {"q": "Quelle mémoire stocke les données utilisées ?", "r": "RAM", "choix": ["ROM", "Disque dur", "RAM", "Cache"]},
    {"q": "Quelle mémoire garde les données sans courant ?", "r": "ROM", "choix": ["RAM", "Processeur", "ROM", "Registre"]},
    {"q": "Quel composant relie tous les autres composants ?", "r": "Carte mère", "choix": ["Carte graphique", "Carte mère", "Processeur", "Alimentation"]},
    {"q": "Quel est le cycle de base d’un processeur ?", "r": "Fetch-Decode-Execute", "choix": ["Encode-Décode", "Lecture-Écriture", "Fetch-Decode-Execute", "Clock Cycle"]},
    {"q": "Quel composant connecte un disque dur à la carte mère ?", "r": "Connecteur SATA", "choix": ["USB", "Slot PCI", "Connecteur SATA", "HDMI"]},
    {"q": "Quel composant contient le BIOS ?", "r": "ROM", "choix": ["RAM", "ROM", "Processeur", "Cache"]},
    {"q": "Quel composant graphique affiche l’image à l’écran ?", "r": "Carte graphique", "choix": ["Carte mère", "Carte graphique", "RAM", "CPU"]},
    {"q": "Que signifie CPU ?", "r": "Central Processing Unit", "choix": ["Computer Program Unit", "Central Processing Unit", "Core Program Unit", "Control Process Unit"]},
    {"q": "Quel type de mémoire est la plus rapide ?", "r": "Registres", "choix": ["RAM", "Cache", "ROM", "Registres"]},
    {"q": "Quel bus transmet les données ?", "r": "Bus de données", "choix": ["Bus de contrôle", "Bus d’adresse", "Bus de données", "Bus USB"]},
    {"q": "Quelle unité mesure la fréquence d’un processeur ?", "r": "Hertz", "choix": ["Byte", "Volt", "Hertz", "Ampère"]},
    {"q": "Quel périphérique est une sortie ?", "r": "Écran", "choix": ["Clavier", "Souris", "Écran", "Micro"]},
    {"q": "Quel périphérique est une entrée ?", "r": "Clavier", "choix": ["Écran", "Clavier", "Imprimante", "Haut-parleur"]},
    {"q": "Quelle unité mesure la capacité d’un disque dur ?", "r": "Go", "choix": ["Hz", "Go", "Km", "Volt"]},
    {"q": "Quelle mémoire est volatile ?", "r": "RAM", "choix": ["ROM", "SSD", "RAM", "Clé USB"]},
    {"q": "Le binaire est composé de combien de chiffres ?", "r": "2", "choix": ["2", "8", "10", "16"]},
    {"q": "Quel système utilise les chiffres 0 à 9 ?", "r": "Décimal", "choix": ["Binaire", "Hexadécimal", "Octal", "Décimal"]},
    {"q": "Quel système utilise les chiffres de 0 à F ?", "r": "Hexadécimal", "choix": ["Octal", "Binaire", "Hexadécimal", "Décimal"]},
    {"q": "Combien de bits dans un octet ?", "r": "8", "choix": ["4", "6", "8", "10"]},
    {"q": "Quel composant contient les registres ?", "r": "Processeur", "choix": ["RAM", "Carte mère", "Processeur", "ROM"]},
    {"q": "Quel composant stocke les fichiers à long terme ?", "r": "Disque dur", "choix": ["RAM", "Disque dur", "Cache", "Registre"]},
    {"q": "Quel type de mémoire est le cache ?", "r": "Mémoire rapide", "choix": ["Mémoire lente", "Mémoire morte", "Mémoire rapide", "Mémoire secondaire"]},
    {"q": "Que signifie RAM ?", "r": "Random Access Memory", "choix": ["Read Access Memory", "Random Access Memory", "Rapid Access Memory", "Read Anytime Memory"]},
    {"q": "Que signifie ROM ?", "r": "Read Only Memory", "choix": ["Random Output Memory", "Read Only Memory", "Reset Only Memory", "Rapid Output Module"]},
    {"q": "Quelle est la première étape du cycle d’instruction ?", "r": "Fetch", "choix": ["Execute", "Decode", "Fetch", "Cycle"]},
    {"q": "Quel composant gère l’alimentation électrique ?", "r": "Bloc d’alimentation", "choix": ["CPU", "Carte mère", "Bloc d’alimentation", "RAM"]},
    {"q": "Un SSD est...", "r": "Un disque de stockage", "choix": ["Un logiciel", "Une carte réseau", "Un disque de stockage", "Une mémoire vive"]},
    {"q": "Lequel est un système d’exploitation ?", "r": "Linux", "choix": ["Python", "Linux", "Excel", "BIOS"]},
    
    {"q": "Que fait cet algorithme ?\n x = 2\ny = 3\nsi x < y alors afficher x sinon afficher y", "r": "Affiche 2", "choix": ["Affiche 2", "Affiche 3", "Erreur", "Affiche x+y"]},
    {"q": "Quel sera le résultat ?\n somme = 0\n pour i de 1 à 3 faire\n somme = somme + i\n afficher somme", "r": "6", "choix": ["3", "6", "1", "Erreur"]},
    {"q": "Que fait cet algorithme ?\n x = 4\n tant que x > 0 faire x = x - 1\n afficher x", "r": "Affiche 0", "choix": ["Affiche 4", "Affiche 1", "Affiche 0", "Affiche -1"]},
    {"q": "Quelle valeur finale aura x ?\n x = 1\n pour i de 1 à 3 faire x = x * 2", "r": "8", "choix": ["2", "4", "6", "8"]},
    {"q": "Comment s’appelle l’action de s’appeler soi-même dans un algorithme ?", "r": "La récursivité", "choix": ["La répétition", "La récursivité", "L’invocation", "La boucle"]},
    {"q": "Quelle est la sortie ?\n x = 10\n si x % 2 == 0 alors afficher 'pair' sinon afficher 'impair'", "r": "pair", "choix": ["pair", "impair", "Erreur", "10"]},
    {"q": "Que fait 'x = x // 2' ?", "r": "Divise x par 2 et garde la partie entière", "choix": ["Multiplie x par 2", "Divise x par 2 avec virgule", "Ajoute 2 à x", "Divise x par 2 et garde \n la partie entière"]},
    {"q": "À quoi sert un algorithme de tri ?", "r": "Classer des éléments dans un ordre défini", "choix": ["Créer des variables", "Effacer des données", "Trier des fonctions", "Classer des éléments dans\n un ordre défini"]},
    {"q": "Quelle structure est la plus adaptée pour exécuter des étapes différentes selon une condition ?", "r": "Conditionnelle (si/sinon)", "choix": ["Boucle", "Fonction", "Conditionnelle (si/sinon)", "Variable"]},
    {"q": "Quel est le rôle d’une fonction dans un algorithme ?", "r": "Exécuter une tâche spécifique et retourner un résultat", "choix": ["Créer des boucles", "Afficher des valeurs", "Gérer les erreurs", "Exécuter une tâche spécifique et\n retourner un résultat"]},
    
    {"q": "Combien de fois la boucle s’exécute-t-elle ?\n pour i de 0 à 4 faire ...", "r": "5 fois", "choix": ["4 fois", "5 fois", "Infini", "Erreur"]},
    {"q": "Que vaut x à la fin ?\n x = 0\n pour i de 1 à 3 faire x = x + i", "r": "6", "choix": ["3", "5", "6", "9"]},
    {"q": "Quel est le rôle de l’instruction 'return' dans une fonction ?", "r": "Renvoyer une valeur", "choix": ["Afficher du texte", "Créer une boucle", "Arrêter le programme", "Renvoyer une valeur"]},
    {"q": "À quoi sert une condition (if) ?", "r": "Exécuter des instructions seulement si une condition est vraie", "choix": ["Créer des variables", "Afficher des résultats", "Répéter un bloc", "Exécuter des instructions seulement\n si une condition est vraie"]},
    {"q": "Quel est le résultat de :\n x = 3\n y = 2\n si x > y alors afficher 'A'", "r": "A", "choix": ["A", "Erreur", "rien", "B"]},
    {"q": "Comment appelle-t-on une boucle qui ne s’arrête jamais ?", "r": "Boucle infinie", "choix": ["Boucle éternelle", "Boucle morte", "Boucle infinie", "Boucle fantôme"]},
    {"q": "Quelle opération donne le reste de la division ?", "r": "Modulo (%)", "choix": ["Division (/)", "Multiplication (*)", "Modulo (%)", "Soustraction (-)"]},
    {"q": "Quel est le rôle d’une variable ?", "r": "Stocker une valeur", "choix": ["Afficher une valeur", "Répéter une action", "Stocker une valeur", "Créer une boucle"]},
    {"q": "Que vaut 'x' après :\n x = 5\n x = x * 2 + 1", "r": "11", "choix": ["10", "11", "12", "Erreur"]},
    {"q": "Quelle est la bonne syntaxe d’une condition en Python ?", "r": "if x > 5:", "choix": ["si x > 5 alors", "if (x > 5)", "if x > 5:", "if x > 5 then"]},

    {"q": "L’adresse IP sert à...", "r": "Identifier un appareil", "choix": ["Envoyer des fichiers", "Ajouter de la RAM", "Identifier un appareil", "Ouvrir un port USB"]}
]


# Mélanger les questions à chaque partie
random.shuffle(questions)
questions = questions[:10]  # Limiter à 10 questions

# Variables globales
index = 0               # Numéro de la question
score = 0               # Score du joueur
choix_melanges = []     # Choix de réponses mélangés
aides_utilisees = 0     # Nombre d’aides 50/50 utilisées
temps_restant = 20      # Temps par question
timer_id = None
voiture = 0

# Couleurs pour les boutons
couleurs = ["#483CB8", "#41ac50", "#CF670B", "#A74439"]

# Affichage de la question actuelle


def afficher():
    global choix_melanges, temps_restant, timer_id   

    if timer_id:
        timer_id = app.after_cancel(timer_id)
    # Redémarrer le temps à 20s
    temps_restant = 20
    timer_label.configure(text=f"Time: {temps_restant}s")  # Mise à jour immédiate

    # Récupérer la question et mélanger les choix
    q = questions[index]
    choix_melanges = q["choix"].copy()
    random.shuffle(choix_melanges)

    # Afficher la question
    label.configure(text=f"{index + 1}. {q['q']}")

    # Afficher les boutons de réponse avec nouveaux choix
    for i in range(4):
        boutons[i].configure(text=choix_melanges[i], state="normal")
    
    for i, b in enumerate(boutons):
        b.grid(row=i//2 + 1, column=i%2, padx=10, pady=10)

        bouton_aide.grid(row=3, column=0, columnspan=2, pady=10)
        timer_label.grid(row=0, column=3, padx=10)
        label_score.grid(row=0, column=2, sticky="e", padx=10)

    # Lancer le compte à rebours
    mise_a_jour_timer()

# Vérifier si la réponse choisie est correcte
def verifier(i):
    global index, score, timer_id

    # Arrêter le timer si réponse donnée
    if timer_id:
        app.after_cancel(timer_id)

    if choix_melanges[i] == questions[index]["r"]:
        score += 1  # Ajouter un point si bonne réponse
        label.configure(text=f"Bravo !!!! + 1 au SCORE")
    else:
        label.configure(text=f"Dommage ! - 1 au SCORE..... Non je blagle")

    # Vérification de la réponse


    # Mise à jour du score à l’écran
    label_score.configure(text=f"Score : {score}")

    # Passer à la question suivante ou terminer
    index += 1
    if index < len(questions):
        app.after(1500, afficher)
    else:
        app.after(1500, terminer)

# Aide 50/50 qui élimine 2 mauvaises réponses
def aide_50_50():
    global aides_utilisees

    # Vérifie si l’aide est disponible
    if aides_utilisees >= 3:
        return

    aides_utilisees += 1  # Incrémenter le nombre d’aides

    # Récupérer la bonne réponse
    bonne_reponse = questions[index]["r"]

    # Identifier les mauvaises réponses
    mauvaises = [i for i in range(4) if choix_melanges[i] != bonne_reponse]

    # Supprimer aléatoirement deux mauvaises
    a_supprimer = random.sample(mauvaises, 2)
    for i in a_supprimer:
        boutons[i].configure(text="", state="disabled")

    # Mettre à jour le texte du bouton d’aide
    bouton_aide.configure(text=f"Aide 50/50 ({3 - aides_utilisees})")

    # Désactiver le bouton s’il n’y a plus d’aide
    if aides_utilisees == 3:
        bouton_aide.configure(state="disabled")

# Gérer la fin du temps
def temps_ecoule():
    global index

    # Passer à la question suivante automatiquement
    index += 1
    if index < len(questions):
        afficher()
    else:
        terminer()

# Compte à rebours
def mise_a_jour_timer():
    global temps_restant, timer_id

    # Affiche le temps actuel
    timer_label.configure(text=f"Time: {temps_restant}s")

    if temps_restant > 0:
        temps_restant -= 1
        timer_id = app.after(1000, mise_a_jour_timer)
    else:
        temps_ecoule()  # Fin du temps

# Fin du quiz
def terminer():
    label.configure(text=f"Quiz terminé ! Score : {score}/{len(questions)}")
    for b in boutons:
        b.grid_forget()
    bouton_aide.grid_forget()
    timer_label.grid_forget()
    message = f"Quiz terminé ! Score : {score}/{len(questions)}\n"
    if score == len(questions):
        label.configure(text=f"Hmm !! Tu es GARÇON !!! ")
    elif score >= len(questions) // 2:
        label.configure(text=f"Faut étudier c'est rien faut pas pleurer ")
    else:
        label.configure(text=f"On ne pleure pas c'est interdit de pleurer \n si tu pleures c'est trop grave !! ")
    label_score.configure(text=f"Score : {score}")
    rejouer_btn.grid(row=4, column=0, columnspan=2, pady=10)
    
def afficher_message_drole():
    # Cacher les boutons et labels
    for b in boutons:
        b.grid_remove()
    bouton_aide.grid_remove()
    timer_label.grid_remove()
    label_score.grid_remove()

    # Choisir un message drôle
    messages_droles1 = [
        "Ahhii ! Tu es encore la !! ",
    ]
    messages_droles2 = [
        "Pardon on a compris oh !!",
    ]
    messages_droles3 = [
        "Regarde on va arreter le jeu si tu continu a jouer",
    ]
    if voiture == 1:
        message_choisi = random.choice(messages_droles1)
        label.configure(text=message_choisi)
    elif voiture == 2:
        message_choisi = random.choice(messages_droles2)
        label.configure(text=message_choisi)
    elif voiture == 3:
        message_choisi = random.choice(messages_droles3)
        label.configure(text=message_choisi)
    else:
        app.destroy()


    # Attendre 2 secondes, puis démarrer le quiz
    app.after(2000, afficher)
# Recommencer une nouvelle partie
def rejouer():
    global index, score, aides_utilisees, questions,voiture

    
    voiture += 1
       
    # Réinitialisation des variables
    index = 0
    score = 0
    aides_utilisees = 0

    # Mélanger de nouvelles questions
    random.shuffle(questions)
    questions = questions[:10]

    # Réactiver le bouton aide
    bouton_aide.configure(text="Aide 50/50 (3)", state="normal")

    # Réinitialiser les affichages
    label_score.configure(text="Score : 0")
    timer_label.configure(text="Time: 10s")
    rejouer_btn.grid_forget()
    bouton_aide.grid(row=3, column=0, columnspan=2, pady=10)
    timer_label.grid(row=0, column=3, padx=10)
    for i, b in enumerate(boutons):
        b.grid(row=i//2 + 1, column=i%2, padx=10, pady=10)

    
    if voiture > 0:
        afficher_message_drole()
    else:
        afficher()
    


    

# Interface principale
app = ctk.CTk()
app.geometry("900x530")
app.title("Mini Kahoot")

# Cadre central
frame_centre = ctk.CTkFrame(app, fg_color="transparent")
frame_centre.place(relx=0.5, rely=0.5, anchor="center")

# Label pour afficher la question
label = ctk.CTkLabel(frame_centre, text="", font=ctk.CTkFont(size=16, weight="bold"),fg_color="#454545", corner_radius=8, wraplength=800, justify="center")
label.grid(row=0, column=0, columnspan=2, pady=25)

# Score affiché
label_score = ctk.CTkLabel(frame_centre, text="Score : 0", font=ctk.CTkFont(size=16),fg_color="#473232", corner_radius=8, wraplength=800)
label_score.grid(row=0, column=2, sticky="e", padx=10)

# Minuteur affiché à droite du score
timer_label = ctk.CTkLabel(frame_centre, text="Time: 10s", font=ctk.CTkFont(size=14),fg_color="#432727", corner_radius=8, wraplength=800)
timer_label.grid(row=0, column=3, padx=10)

# Création des boutons de réponse
boutons = []
for i in range(4):
    b = ctk.CTkButton(frame_centre, text="", width=150, height=60,
                      fg_color=couleurs[i], command=lambda i=i: verifier(i)) 
    b.grid(row=i//2 + 1, column=i%2, padx=10, pady=10)
    boutons.append(b)

# Bouton d’aide 50/50
bouton_aide = ctk.CTkButton(frame_centre, text="Aide 50/50 (3)", width=150, command=aide_50_50)
bouton_aide.grid(row=3, column=0, columnspan=2, pady=10)

# Bouton Rejouer (affiché seulement à la fin)
rejouer_btn = ctk.CTkButton(frame_centre, text="Rejouer", width=150, command=rejouer)

# Démarrer le quiz dès l’ouverture
afficher()

# Lancer la fenêtre
app.mainloop()