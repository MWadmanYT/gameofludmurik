import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

run = True

x = 100
y = 100
width = 20
height = 30
speed = 5

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LEFT] and x >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= 500 - width:
        x += speed
    if keys[pygame.K_UP] and y >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y <= 500:
        y += speed

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
