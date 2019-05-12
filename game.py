import pygame
from main.main import player, drawWindow

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.init()
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

screen_width = 1920
screen_height = 1080

win = pygame.display.set_mode([screen_width, screen_height],pygame.FULLSCREEN)
pygame.display.set_caption("Червячок")
clock = pygame.time.Clock()

run = True
player = player(0, 415, 137, 85)

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_LEFT] and player.x >= 0:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.lastposition = 1
    elif keys[pygame.K_RIGHT] and player.x <= screen_width - player.width:
        player.x += player.speed
        player.left = False
        player.right = True
        player.lastposition = 2
    else:
        player.left = False
        player.right = False

    if not(player.isJump):
        #if keys[pygame.K_UP] and y >= 0:
        #    y -= speed
        #if keys[pygame.K_DOWN] and y <= screen_height - height:
        #    y += speed
        if keys[pygame.K_SPACE]:
            player.isJump = True
    else:
        if player.jumpCount >= -10:
            if player.jumpCount < 0:
                player.y += (player.jumpCount ** 2) / 4
            else:
                player.y -= (player.jumpCount ** 2) / 4
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    drawWindow(win, player)
pygame.quit()
        
