import pygame
from main.image_init import image

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

def drawWindow(win, ownplayer):
    win.blit(image.background, (0, 0))
    ownplayer.draw(win)
    pygame.display.update()

def playerGoing():
    if keys[pygame.K_LEFT] and player.x >= 0:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.lastposition = 1
    if keys[pygame.K_RIGHT] and player.x <= screen_width - player.width:
        player.x += player.speed
        player.left = False
        player.right = True
        player.lastposition = 2
    else:
        player.left = False
        player.right = False

    if keys[pygame.K_UP] and y >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y <= screen_height - height:
        y += speed
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
