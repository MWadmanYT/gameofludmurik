import pygame
from main.main import player, drawWindow, playerGoing
from main.image_init import image

def start():
    run = True

    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        playerGoing()
        drawWindow()

    pygame.quit()
