import random
import pygame
from Player import *
from Projectile import *

pygame.init()
#For Debugging
wind = pygame.display.set_mode((640,480))
#wind = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screenw, screenh = pygame.display.get_surface().get_size()
pygame.display.set_caption("WolfPack")
startingBG = pygame.image.load('GeneralSprits/background.jpg')

clockFPS = pygame.time.Clock()


#Changing the GameWindow
def redrawGameWindow():
    wind.blit(startingBG, (0,0))
    playerChar.draw(wind)
    pygame.display.update()


#Main Loop

playerChar = Player(300,410,64,64)


run = True
while run:
    clockFPS.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerChar.xlocation > playerChar.velocity:
        playerChar.xlocation -= playerChar.velocity
        playerChar.leftMovement = True #Movement is currently left, use left sprits
        playerChar.rightMovement = False
        playerChar.upMovement = False
        playerChar.downMovement = False
        playerChar.standing = False

    elif keys[pygame.K_RIGHT] and playerChar.xlocation < screenw - playerChar.playerWidth - playerChar.velocity:
        playerChar.xlocation += playerChar.velocity
        playerChar.leftMovement = False
        playerChar.rightMovement = True #Movement is currently right, use right sprits
        playerChar.upMovement = False
        playerChar.downMovement = False
        playerChar.standing = False

    elif keys[pygame.K_UP] and playerChar.ylocation > playerChar.velocity:
        playerChar.ylocation -= playerChar.velocity
        playerChar.leftMovement = False
        playerChar.rightMovement = False
        playerChar.upMovement = True #Movement is currently up, use up sprits
        playerChar.downMovement = False
        playerChar.standing = False

    elif keys[pygame.K_DOWN] and playerChar.ylocation < screenh - playerChar.playerHeight - playerChar.velocity:
        playerChar.ylocation += playerChar.velocity
        playerChar.leftMovement = False
        playerChar.rightMovement = False
        playerChar.upMovement = False
        playerChar.downMovement = True #Movement is currently down, use down sprits
        playerChar.standing = False

    else:
        playerChar.standing = True
        playerChar.walkCount = 0

    redrawGameWindow()
    

pygame.quit()
