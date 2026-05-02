import pygame
import random
import sys
import time

# Initialisation de tous les modules Pygame
pygame.init()

# ─── DIMENSIONS DE LA FENÊTRE ───────────────────────────────────────────────
largeur, hauteur = 600, 400      # Taille de la fenêtre en pixels
taille_case = 20                  # Taille d'une case de la grille (serpent, pomme, obstacles)
ecran = pygame.display.set_mode((largeur, hauteur))  # Création de la fenêtre
pygame.display.set_caption("Snake - Niveaux, Obstacles & Invincibilité")  # Titre de la fenêtre

# ─── COULEURS (format RGB) ───────────────────────────────────────────────────
VERT  = (0, 255, 0)      # Corps du serpent
ROUGE = (255, 0, 0)      # Pomme et texte game over
NOIR  = (0, 0, 0)        # Fond de l'écran
BLANC = (255, 255, 255)  # Texte et yeux du serpent
GRIS  = (100, 100, 100)  # Obstacles
JAUNE = (255, 215, 0)    # Étoile d'invincibilité

# ─── POLICE ET HORLOGE ──────────────────────────────────────────────────────
font  = pygame.font.SysFont(None, 30)  # Police système taille 30 pour les textes
clock = pygame.time.Clock()             # Horloge pour contrôler la vitesse du jeu


# ─── FONCTION : Afficher du texte à l'écran ─────────────────────────────────
def afficher_texte(texte, x, y, couleur=BLANC):
    txt = font.render(texte, True, couleur)  # Génère une surface image du texte
    ecran.blit(txt, (x, y))                  # Dessine cette surface aux coordonnées (x, y)


# ─── FONCTION : Dessiner le serpent case par case ───────────────────────────
def dessiner_serpent(serpent):
    for i, bloc in enumerate(serpent):
        x, y = bloc  # Coordonnées de chaque segment
        if i == 0:
            # Tête du serpent : coin arrondi + 2 yeux blancs
            pygame.draw.rect(ecran, (0, 200, 0), (x, y, taille_case, taille_case), border_radius=8)
            pygame.draw.circle(ecran, BLANC, (x + 5,  y + 5), 3)   # Oeil gauche
            pygame.draw.circle(ecran, BLANC, (x + 15, y + 5), 3)   # Oeil droit
        else:
            # Corps du serpent : dégradé de vert selon la position du segment
            vert_variable = 100 + (i * 10 % 155)  # La valeur de vert augmente vers la queue
            pygame.draw.rect(ecran, (0, vert_variable, 0), (x, y, taille_case, taille_case), border_radius=6)


# ─── FONCTION : Dessiner les obstacles ──────────────────────────────────────
def dessiner_obstacles(obstacles):
    for obs in obstacles:
        # Chaque obstacle est un carré gris avec coins arrondis
        pygame.draw.rect(ecran, GRIS, (*obs, taille_case, taille_case), border_radius=4)


# ─── FONCTION : Générer une pomme à une position aléatoire ──────────────────
def nouvelle_pomme():
    return (
        random.randrange(0, largeur, taille_case),  # Position X aléatoire alignée sur la grille
        random.randrange(0, hauteur, taille_case)   # Position Y aléatoire alignée sur la grille
    )


# ─── FONCTION : Générer les obstacles selon le niveau actuel ────────────────
def generer_obstacles(niveau):
    obstacles = []
    if niveau >= 2:
        # Niveau 2 : mur vertical de 5 cases en x=200
        for i in range(5):
            obstacles.append((200, 60 + i * taille_case))
    if niveau >= 3:
        # Niveau 3 : mur vertical de 5 cases en x=300
        for i in range(5):
            obstacles.append((300, 100 + i * taille_case))
    if niveau >= 4:
        # Niveau 4 : mur horizontal de 8 cases en y=200
        for i in range(8):
            obstacles.append((100 + i * taille_case, 200))
    if niveau >= 5:
        # Niveau 5 : mur vertical de 6 cases en x=400
        for i in range(6):
            obstacles.append((400, 50 + i * taille_case))
    return obstacles


# ─── FONCTION PRINCIPALE : Boucle de jeu ────────────────────────────────────
def game():
    # Initialisation des variables de jeu
    serpent            = [(100, 100)]      # Liste de tuples (x, y) — la tête est en index 0
    direction          = (taille_case, 0)  # Direction initiale : vers la droite
    pomme              = nouvelle_pomme()  # Position initiale de la pomme
    etoile             = None              # L'étoile n'apparaît pas au départ
    score              = 0
    niveau             = 1
    score_par_niveau   = 5                 # Nombre de pommes à manger pour passer au niveau suivant
    obstacles          = generer_obstacles(niveau)
    invincible         = False             # Mode invincibilité désactivé au départ
    invincible_start_time = 0              # Timestamp du début de l'invincibilité
    game_over          = False

    # ─── BOUCLE PRINCIPALE ──────────────────────────────────────────────────
    while True:

        # ── Gestion des événements (clavier, fermeture fenêtre) ─────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Changement de direction — on empêche le demi-tour immédiat
                if event.key == pygame.K_UP    and direction != (0, taille_case):
                    direction = (0, -taille_case)
                elif event.key == pygame.K_DOWN  and direction != (0, -taille_case):
                    direction = (0, taille_case)
                elif event.key == pygame.K_LEFT  and direction != (taille_case, 0):
                    direction = (-taille_case, 0)
                elif event.key == pygame.K_RIGHT and direction != (-taille_case, 0):
                    direction = (taille_case, 0)
                elif event.key == pygame.K_r and game_over:
                    return game()  # Redémarre le jeu si R est pressé après game over

        # Si game over, on arrête les mises à jour et on attend la touche R
        if game_over:
            continue

        # ── Déplacement : calcul de la nouvelle tête ────────────────────────
        tete = (serpent[0][0] + direction[0], serpent[0][1] + direction[1])
        serpent.insert(0, tete)  # Ajoute la nouvelle tête en début de liste

        # ── Collision avec la pomme ──────────────────────────────────────────
        if tete == pomme:
            pomme = nouvelle_pomme()  # Nouvelle pomme générée
            score += 1                # Le serpent grandit (on ne retire pas la queue)
        else:
            serpent.pop()             # Retire le dernier segment pour simuler le déplacement

        # ── Apparition aléatoire de l'étoile (1 chance sur 251 par frame) ───
        if etoile is None and random.randint(0, 250) == 1:
            etoile = nouvelle_pomme()

        # ── Ramassage de l'étoile → active l'invincibilité 5 secondes ───────
        if etoile and tete == etoile:
            etoile = None
            invincible = True
            invincible_start_time = time.time()

        # ── Fin de l'invincibilité après 5 secondes ──────────────────────────
        if invincible and time.time() - invincible_start_time >= 5:
            invincible = False

        # ── Passage au niveau supérieur ──────────────────────────────────────
        if score >= niveau * score_par_niveau:
            if niveau < 5:
                niveau += 1
                obstacles = generer_obstacles(niveau)  # Nouveaux obstacles pour le niveau
            else:
                # Niveau 5 terminé → victoire
                ecran.fill(NOIR)
                afficher_texte("Félicitations, tu as gagné !", 150, 180, ROUGE)
                pygame.display.flip()
                pygame.time.delay(3000)  # Pause 3 secondes avant de quitter
                return

        # ── Détection des collisions mortelles (sauf si invincible) ─────────
        if (
            (tete[0] < 0 or tete[0] >= largeur or tete[1] < 0 or tete[1] >= hauteur) or
            # Collision avec les bords de la fenêtre
            (tete in serpent[1:]) or
            # Collision avec son propre corps
            (tete in obstacles)
            # Collision avec un obstacle
        ):
            if not invincible:
                game_over = True  # Déclenche le game over uniquement si pas invincible

        # ── Affichage ────────────────────────────────────────────────────────
        ecran.fill(NOIR)                    # Efface l'écran à chaque frame
        dessiner_serpent(serpent)           # Redessine le serpent
        dessiner_obstacles(obstacles)       # Redessine les obstacles

        # Pomme rouge
        pygame.draw.rect(ecran, ROUGE, (*pomme, taille_case, taille_case), border_radius=6)

        # Étoile jaune (si présente)
        if etoile:
            pygame.draw.rect(ecran, JAUNE, (*etoile, taille_case, taille_case), border_radius=8)

        # Affichage du score et du niveau
        afficher_texte(f"Score : {score}",  10,  10)
        afficher_texte(f"Niveau : {niveau}", 500, 10)

        # Indicateur d'invincibilité
        if invincible:
            afficher_texte("INVINCIBLE", 230, 10, JAUNE)

        # Écran game over
        if game_over:
            afficher_texte("GAME OVER",                   240, 160, ROUGE)
            afficher_texte("Appuie sur R pour rejouer",   190, 200, BLANC)

        pygame.display.flip()  # Met à jour l'affichage (envoie le buffer à l'écran)

        # ── Vitesse du jeu selon le niveau (augmente à chaque niveau) ────────
        vitesse = 2 + (niveau - 1) * 2  # Niveau 1=2fps, Niveau 2=4fps, ... Niveau 5=10fps
        clock.tick(vitesse)


# ─── LANCEMENT DU JEU ───────────────────────────────────────────────────────
game()