import tkinter as tk # Importe la bibliothèque Tkinter pour créer l'interface graphique
from tkinter import messagebox # Importe le module messagebox pour afficher des pop-ups d'information

# --- Classe principale du jeu ---
class QuizGame:
    def __init__(self, master):
        # Initialisation du jeu
        self.master = master # 'master' représente la fenêtre principale Tkinter
        master.title("Jeu Vrai ou Faux") # Définit le titre de la fenêtre
        master.geometry("500x300") # Définit la taille initiale de la fenêtre (largeur x hauteur)

        self.score = 0 # Initialise le score du joueur à 0
        self.question_index = 0 # Garde une trace de la question actuelle (commence à la première, index 0)
        self.player_name = "" # Variable pour stocker le nom du joueur

        # Liste des questions et de leurs réponses correctes
        # Chaque élément est un tuple: (texte de la question, réponse correcte Vrai/Faux)
        self.questions = [
            ("Paris est la capitale de la France.", True),
            ("Le soleil tourne autour de la Terre.", False),
            ("Un octogone a 8 côtés.", True),
            ("L'eau bout à 0 degré Celsius.", False),
            ("Les poissons dorment les yeux ouverts.", True),
            ("L'Everest est la plus haute montagne du monde.", True),
            ("Les fourmis ont six pattes.", True),
            ("La Grande Muraille de Chine est visible depuis l'espace à l'œil nu.", False),
            ("Le sang des insectes est vert.", False),
            ("Les pingouins ne peuvent pas voler.", True),
            ("Le chocolat est toxique pour les chiens.", True),
            ("L'Australie est un continent.", True),
            ("Les chauves-souris sont aveugles.", False),
            ("Les serpents sont des reptiles.", True),
            ("Un triangle a toujours 3 angles égaux.", False),
            ("La lune est une étoile.", False),
            ("Les abeilles meurent après avoir piqué.", True),
            ("La tour Eiffel se trouve à Londres.", False),
            ("Les girafes peuvent nettoyer leurs oreilles avec leur langue.", True),
            ("Les requins sont des mammifères.", False),
            ("Les roses sont toujours rouges.", False),
            ("La tomate est un fruit.", True),
            ("Le Nil est le fleuve le plus long du monde.", True),
            ("Les chats n'aiment pas l'eau.", False),
            ("Le Sahara est le plus grand désert chaud du monde.", True)
        ]

        self.create_widgets() # Appelle la méthode pour créer tous les éléments de l'interface

    # --- Création des éléments de l'interface graphique ---
    def create_widgets(self):
        # Cadre pour demander le nom du joueur (visible au début)
        self.name_frame = tk.Frame(self.master) # Crée un cadre dans la fenêtre principale
        self.name_frame.pack(pady=20) # Place le cadre et ajoute un peu d'espace vertical

        self.name_label = tk.Label(self.name_frame, text="Quel est votre nom ?", font=("Arial", 14))
        self.name_label.pack() # Crée et place une étiquette pour demander le nom

        self.name_entry = tk.Entry(self.name_frame, width=30, font=("Arial", 12))
        self.name_entry.pack(pady=10) # Crée et place un champ de saisie pour le nom

        self.start_button = tk.Button(self.name_frame, text="Commencer le jeu", command=self.start_game, font=("Arial", 12))
        self.start_button.pack() # Crée et place un bouton pour démarrer le jeu.
                                 # 'command=self.start_game' fait en sorte que la méthode start_game est appelée au clic.

        # Cadre pour les questions et le score (initialement caché)
        self.quiz_frame = tk.Frame(self.master) # Crée un autre cadre

        self.score_label = tk.Label(self.quiz_frame, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=10) # Crée et place une étiquette pour afficher le score

        self.question_label = tk.Label(self.quiz_frame, text="", wraplength=450, font=("Arial", 16))
        self.question_label.pack(pady=20) # Crée et place une étiquette pour afficher la question.
                                          # 'wraplength' assure que le texte s'enroule si trop long.

        self.true_button = tk.Button(self.quiz_frame, text="Vrai", command=lambda: self.check_answer(True), font=("Arial", 12), width=10)
        self.true_button.pack(side=tk.LEFT, padx=50, pady=10) # Crée et place le bouton "Vrai".
                                                             # 'lambda' est utilisé pour passer 'True' à check_answer.

        self.false_button = tk.Button(self.quiz_frame, text="Faux", command=lambda: self.check_answer(False), font=("Arial", 12), width=10)
        self.false_button.pack(side=tk.RIGHT, padx=50, pady=10) # Crée et place le bouton "Faux".
                                                               # 'lambda' est utilisé pour passer 'False' à check_answer.

    # --- Démarrer le jeu ---
    def start_game(self):
        self.player_name = self.name_entry.get().strip() # Récupère le texte du champ de saisie du nom et supprime les espaces inutiles
        if not self.player_name: # Vérifie si le nom est vide
            messagebox.showwarning("Nom manquant", "Veuillez entrer votre nom pour commencer le jeu.")
            return # Arrête la fonction si le nom est vide

        self.name_frame.pack_forget() # Cache le cadre où on demande le nom (il n'est plus nécessaire)
        self.quiz_frame.pack(pady=20) # Affiche le cadre du quiz
        self.next_question() # Appelle la méthode pour afficher la première question

    # --- Afficher la question suivante ---
    def next_question(self):
        if self.question_index < len(self.questions): # Vérifie s'il reste des questions
            question_text, _ = self.questions[self.question_index] # Récupère le texte de la question actuelle (le '_' ignore la réponse)
            self.question_label.config(text=question_text) # Met à jour l'étiquette de la question
            self.score_label.config(text=f"Score: {self.score}") # Met à jour l'affichage du score
        else:
            self.show_results() # Si toutes les questions ont été posées, affiche les résultats

    # --- Vérifier la réponse de l'utilisateur ---
    def check_answer(self, user_answer):
        _, correct_answer = self.questions[self.question_index] # Récupère la réponse correcte pour la question actuelle (le '_' ignore le texte)
        if user_answer == correct_answer: # Compare la réponse de l'utilisateur avec la bonne réponse
            self.score += 1 # Incrémente le score si la réponse est correcte
            # messagebox.showinfo("Résultat", "Bonne réponse !") # Affiche un message de succès
        # else:
            # messagebox.showinfo("Résultat", "Mauvaise réponse.") # Affiche un message d'erreur

        self.question_index += 1 # Passe à la question suivante
        self.next_question() # Appelle la méthode pour afficher la question suivante (ou les résultats si c'est la fin)

    # --- Afficher les résultats finaux ---
    def show_results(self):
        messagebox.showinfo("Fin du jeu",
                            f"Félicitations {self.player_name} !\n" # Affiche un message de félicitations avec le nom du joueur
                            f"Votre score final est de {self.score} sur {len(self.questions)} questions.") # Affiche le score final
        self.master.destroy() # Ferme la fenêtre du jeu après l'affichage des résultats

# --- Démarrage de l'application Tkinter ---
root = tk.Tk() # Crée la fenêtre racine (principale) de l'application Tkinter
game = QuizGame(root) # Crée une instance de notre jeu QuizGame, en lui passant la fenêtre racine
root.mainloop() # Lance la boucle principale de Tkinter. C'est elle qui gère les événements (clics, saisies...)
                 # et maintient la fenêtre ouverte jusqu'à ce qu'elle soit fermée par l'utilisateur ou le programme.