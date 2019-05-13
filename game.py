import pygame
from main.image_init import image
from levels.scene1 import start
from main.main import screen

pygame.init()

pygame.display.set_caption("Cherviak")
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if pygame.mouse.get_pos()[0] >= 57 and pygame.mouse.get_pos()[1] >= 540 and pygame.mouse.get_pos()[0] <= 243 and pygame.mouse.get_pos()[1] <= 616:
        screen.win.blit(image.play2, (57, 540))
    else:
        screen.win.blit(image.play1, (57, 540))
    if pygame.mouse.get_pressed() and pygame.mouse.get_pos()[0] >= 57 and pygame.mouse.get_pos()[1] >= 540 and pygame.mouse.get_pos()[0] <= 243 and pygame.mouse.get_pos()[1] <= 616:
        start()

    screen.win.blit(image.backgroundmenu, (300, 0))
    pygame.display.update()

pygame.quit()
