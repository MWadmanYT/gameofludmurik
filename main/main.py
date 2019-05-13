import pygame
from main.image_init import image

class screen():
    screen_width = 1920
    screen_height = 1080
    win = pygame.display.set_mode([screen_width, screen_height],pygame.FULLSCREEN)

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.lastposition = 1
        self.animCount = 0
        self.up = False
        self.down = True

    def draw(self, win):
        if self.animCount + 1 >= 30:
            self.animCount = 0
        if self.left:
            win.blit(image.walkLeft, (self.x, self.y))
            self.animCount += 1
        elif self.right:
            win.blit(image.walkRight, (self.x, self.y))
            self.animCount += 1
        else:
            if self.lastposition == 1:
                win.blit(image.idleLeft, (self.x, self.y))
            if self.lastposition == 2:
                win.blit(image.idleRight, (self.x, self.y))

player = player(0, 0, 196, 118)


def drawWindow():
    screen.win.blit(image.background, (0, 0))
    player.draw(screen.win)
    pygame.display.update()

def playerGoing():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x >= 0:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.lastposition = 1
    if keys[pygame.K_RIGHT] and player.x <= screen.screen_width - player.width:
        player.x += player.speed
        player.left = False
        player.right = True
        player.lastposition = 2
    else:
        player.left = False
        player.right = False
    if keys[pygame.K_UP] and y >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y <= screen.screen_height - player.height:
        y += speed
