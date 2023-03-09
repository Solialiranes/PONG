# Créé par solia, le 17/10/2020 en Python 3.7
import pygame
import time
pygame.init()

#Couleurs
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
blue = (255, 0, 0)
red = (0, 255, 0)
magenta = (102, 0, 161)

screen_size = (800, 600) #Taille fenêtre
player_width = 15 #Largeur joueur
player_height = 90 #Hauteur joueur

compteurG = 0 #Compteur de points gauche
compteurD = 0 #Compteur de points droite


#Pour la musique en fond
#musique = 'musique/Sweden_Minecraft_Remix.mp3
#pygame.mixer.init()
#pygame.mixer.music.load(musique)
#pygame.mixer.music.play(-1)


pygame.display.set_caption("Pong Tohalia") #Nom de la fenêtre
#Background
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load("backlilian.jpg")
clock = pygame.time.Clock()

#Coordonées et vélocité du joueur 1
player1_x_coor = 50 - player_width
player1_y_coor = 300 - 45
player1_y_speed = 0

#Coordonées et vélocité du joueur 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

#Coordonées de la balle
balle_x = 400
balle_y = 300
balle_speed_x = 5
balle_speed_y = 5


game_over = False

while not game_over:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
			# Joueur 1
            if event.key == pygame.K_w:
                player1_y_speed = -8
            if event.key == pygame.K_s:
                player1_y_speed = 8
			# Joueur 2
            if event.key == pygame.K_UP:
                player2_y_speed = -8
            if event.key == pygame.K_DOWN:
                player2_y_speed = 8

        if event.type == pygame.KEYUP:
			# Joueur 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
			# Joueur 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

        #Relancer le jeu avec ENTER
        if event.type == pygame.KEYDOWN :
          if event.key == pygame.K_RETURN :
            print("Redémarrage du jeu dans 3 secondes")
            balle_x = 400
            balle_y = 300
            balle_speed_x = -5
            balle_speed_y = -5
            compteurD = 0
            compteurG = 0
            time.sleep(3)


    if balle_y > 575 or balle_y < 30:
        balle_speed_y *= -1

    #Lorsque le ballon sors à droite
    if balle_x > 800:
        balle_x = 400
        balle_y = 300
        print("-----------------------------------------------------------")
        print("Balle sortie du terrain à droite, +1 point pour le joueur 1 !")
        compteurG = compteurG + 1
        print("Le joueur 1 a ",compteurG," points")
        print("-----------------------------------------------------------")
        #Si il quitte l'écran, change direction
        balle_speed_x *= -1
        balle_speed_y *= -1

	#Lorsque le ballon sort à gauche
    if balle_x < 0:
        balle_x = 400
        balle_y = 300
        print("-----------------------------------------------------------")
        print("Balle sortie du terrain à gauche, +1 point pour le joueur 2 !")
        compteurD = compteurD + 1
        print("Le joueur 2 a ",compteurD," points")
        print("-----------------------------------------------------------")
	   #Si il quitte l'écran, change direction
        balle_speed_x *= -1
        balle_speed_y *= -1

	#Modifie les coordonnées par rapport au mouvement des joueurs / balle
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
	#Mouvement de la balle
    balle_x += balle_speed_x
    balle_y += balle_speed_y


    if compteurD == 5 : #Si le joueur de droite gagne :
        balle_speed_x = 0
        balle_speed_y = 0
        screen.blit(TextwinD1, (175, 300))
        screen.blit(TextwinD2, (20, 400))

    if compteurG == 5 : #Si le joueur de gauche gagne :
        balle_speed_x = 0
        balle_speed_y = 0
        screen.blit(TextwinG1, (175, 300))
        screen.blit(TextwinD2, (20, 400))



	#Zone de jeu
    joueur1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    joueur2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
    balle = pygame.draw.circle(screen, white, (balle_x, balle_y), 10)

	#Collisions
    if balle.colliderect(joueur1) or balle.colliderect(joueur2):
        balle_speed_x *= -1

    #Lignes bordure terrain
    pygame.draw.line(screen, white,(000,000),(800,000),30)#Haut
    pygame.draw.line(screen, white,(000,600),(800,600),30)#Bas
    pygame.display.flip()

    #Crée les variables pour les scores SUR LE TERRAIN
    font = pygame.font.Font("police/Robot_Z.ttf", 50)

    #Variables textes sur le terrain
    TextcompteurD = font.render(str(compteurD), 1, white)
    TextcompteurG = font.render(str(compteurG), 1, white)

    TextwinG1 = font.render("Le joueur 1 a gagné ! ", 1, white)
    TextwinG2 = font.render("Appuyez sur entrée pour rejouer", 1, white)

    TextwinD1 = font.render("Le joueur 2 a gagné !", 1, white)
    TextwinD2 = font.render("Appuyez sur entrée pour rejouer", 1, white)


    #Affiche les scores sur le terrain
    screen.blit(TextcompteurD, (500, 40))
    screen.blit(TextcompteurG, (300, 40))

    #Pour les FPS
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
