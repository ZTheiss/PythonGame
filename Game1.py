import pygame
import random

pygame.init()

wind = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


pygame.display.set_caption("First Game")

x = 50
y = 50
width = 60
height = 70
velocity = 15

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        break
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    wind.fill((0,0,0))
    pygame.draw.rect(wind, (255, 0, 0), (x,y,width,height))
    pygame.display.update()
    

pygame.quit()


