import pygame
from main.image_init import image

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.lastposition = 1
        self.animCount = 0

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
