import pygame
from main.main import player, drawWindow
from main.image_init import image

pygame.init()

screen_width = 1920
screen_height = 1080

win = pygame.display.set_mode([screen_width, screen_height],pygame.FULLSCREEN)
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
        run = false

    color3 = 255
    color1 = 255
    color2 = 255

    if pygame.mouse.get_pos()[0] >= 40 and pygame.mouse.get_pos()[1] >= 540 and pygame.mouse.get_pos()[0] <= 260 and pygame.mouse.get_pos()[1] <= 580:
        color3 = 135
    if pygame.mouse.get_pressed()[0]:
        color3 = 50
        color1 = 10
        color2 = 200

    pygame.draw.rect(win, (color1, color2, color3), (40, 540, 220, 40))
    win.blit(image.backgroundmenu, (300, 0))
    pygame.display.update()

pygame.quit()
