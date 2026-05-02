import pygame
import random
import sys
import time

pygame.init()

# Dimensions
largeur, hauteur = 600, 400
taille_case = 20
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake - Niveaux, Obstacles & Invincibilité")

# Couleurs
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (100, 100, 100)
JAUNE = (255, 215, 0)

# Font et horloge
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

def afficher_texte(texte, x, y, couleur=BLANC):
    txt = font.render(texte, True, couleur)
    ecran.blit(txt, (x, y))

def dessiner_serpent(serpent):
    for i, bloc in enumerate(serpent):
        x, y = bloc
        if i == 0:
            pygame.draw.rect(ecran, (0, 200, 0), (x, y, taille_case, taille_case), border_radius=8)
            pygame.draw.circle(ecran, BLANC, (x + 5, y + 5), 3)
            pygame.draw.circle(ecran, BLANC, (x + 15, y + 5), 3)
        else:
            vert_variable = 100 + (i * 10 % 155)
            pygame.draw.rect(ecran, (0, vert_variable, 0), (x, y, taille_case, taille_case), border_radius=6)

def dessiner_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(ecran, GRIS, (*obs, taille_case, taille_case), border_radius=4)

def nouvelle_pomme():
    return (
        random.randrange(0, largeur, taille_case),
        random.randrange(0, hauteur, taille_case)
    )

def generer_obstacles(niveau):
    obstacles = []
    if niveau >= 2:
        for i in range(5):
            obstacles.append((200, 60 + i * taille_case))
    if niveau >= 3:
        for i in range(5):
            obstacles.append((300, 100 + i * taille_case))
    if niveau >= 4:
        for i in range(8):
            obstacles.append((100 + i * taille_case, 200))
    if niveau >= 5:
        for i in range(6):
            obstacles.append((400, 50 + i * taille_case))
    return obstacles

def game():
    # Variables du jeu
    serpent = [(100, 100)]
    direction = (taille_case, 0)
    pomme = nouvelle_pomme()
    etoile = None
    score = 0
    niveau = 1
    score_par_niveau = 5
    obstacles = generer_obstacles(niveau)
    invincible = False
    invincible_start_time = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, taille_case):
                    direction = (0, -taille_case)
                elif event.key == pygame.K_DOWN and direction != (0, -taille_case):
                    direction = (0, taille_case)
                elif event.key == pygame.K_LEFT and direction != (taille_case, 0):
                    direction = (-taille_case, 0)
                elif event.key == pygame.K_RIGHT and direction != (-taille_case, 0):
                    direction = (taille_case, 0)
                elif event.key == pygame.K_r and game_over:
                    return game()  # Recommencer

        if game_over:
            continue

        # Déplacement du serpent
        tete = (serpent[0][0] + direction[0], serpent[0][1] + direction[1])
        serpent.insert(0, tete)

        # Collision avec la pomme
        if tete == pomme:
            pomme = nouvelle_pomme()
            score += 1
        else:
            serpent.pop()

        # Apparition aléatoire de l’étoile
        if etoile is None and random.randint(0, 250) == 1:
            etoile = nouvelle_pomme()

        # Ramassage étoile
        if etoile and tete == etoile:
            etoile = None
            invincible = True
            invincible_start_time = time.time()

        # Fin de l’invincibilité après 5s
        if invincible and time.time() - invincible_start_time >= 5:
            invincible = False

        # Changement de niveau
        if score >= niveau * score_par_niveau:
            if niveau < 5:
                niveau += 1
                obstacles = generer_obstacles(niveau)
            else:
                ecran.fill(NOIR)
                afficher_texte("Félicitations, tu as gagné !", 150, 180, ROUGE)
                pygame.display.flip()
                pygame.time.delay(3000)
                return

        # Collision (sauf si invincible)
        if (
            (tete[0] < 0 or tete[0] >= largeur or tete[1] < 0 or tete[1] >= hauteur) or
            (tete in serpent[1:]) or
            (tete in obstacles)
        ):
            if not invincible:
                game_over = True

        # Affichage
        ecran.fill(NOIR)
        dessiner_serpent(serpent)
        dessiner_obstacles(obstacles)
        pygame.draw.rect(ecran, ROUGE, (*pomme, taille_case, taille_case), border_radius=6)

        if etoile:
            pygame.draw.rect(ecran, JAUNE, (*etoile, taille_case, taille_case), border_radius=8)

        afficher_texte(f"Score : {score}", 10, 10)
        afficher_texte(f"Niveau : {niveau}", 500, 10)

        if invincible:
            afficher_texte("INVINCIBLE ⭐", 230, 10, JAUNE)

        if game_over:
            afficher_texte("GAME OVER", 240, 160, ROUGE)
            afficher_texte("Appuie sur R pour rejouer", 190, 200, BLANC)

        pygame.display.flip()

        # Vitesse selon le niveau
        vitesse = 2 + (niveau - 1) * 2
        clock.tick(vitesse)

# Lancer le jeu
game()