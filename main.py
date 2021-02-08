import pygame
from Plateau import Plateau
from Joueur import Joueur



def grid(window,size,rows):
    distance_row = size //rows
    x=0
    y=0
    for l in range(rows):
        x+=distance_row
        y+=distance_row
        pygame.draw.line(window,(255,255,255),(x,0),(x,size))
        pygame.draw.line(window, (255, 255, 255), (0, y), (size, y))
    pygame.display.flip()




global size, rows


size = 600

plateau = Plateau(taille = 4 ,\
                  position_depart_joueur = (25,35),nombre_rewards=2)
rows = plateau.taille
player = plateau.player


window = pygame.display.set_mode((size,size))


pygame.display.set_caption("Petit jeu")







running = True

while running:

    grid(window, size, rows)
    window.fill((0, 0, 0))
    window.blit(player.image, player.rect)
    [window.blit(plateau.rewards[i].image_rew,plateau.rewards[i].rect_rew)  for i in range(plateau.nombre_rewards)]










    for event in pygame.event.get():



        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            print(player.poss_action())

            if event.key == pygame.K_RIGHT:
                player.action('droite',size)
            elif event.key == pygame.K_LEFT:
                player.action('gauche', size)
            elif event.key == pygame.K_DOWN:
                player.action('bas', size)
            elif event.key == pygame.K_UP:
                player.action('haut', size)





