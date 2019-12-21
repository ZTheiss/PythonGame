import random
import pygame
import copy
from Player import *
from Projectile import *


windowX = 640
windowY = 480
pygame.init()
#For Debugging
wind = pygame.display.set_mode((windowX,windowY))
#wind = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screenw, screenh = pygame.display.get_surface().get_size()
pygame.display.set_caption("WolfPack")
startingBG = pygame.image.load('GeneralSprits/background.jpg')

clockFPS = pygame.time.Clock()


#Changing the GameWindow
def redrawGameWindow():
    wind.blit(startingBG, (0,0))
    playerChar.draw(wind)
    for arrow in arrows:
        arrow.draw(wind)
    pygame.display.update()

#Main Loop
facing = 0

playerChar = Player(300,410,64,64)
arrows = []

run = True
while run:
    clockFPS.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break
    i= 0
    for arrow in arrows: #Bug was checking facing, not arrow.facing
        i+=1
        if arrow.facing == 1 or arrow.facing == -1:
            if arrow.xlocation < windowX and arrow.xlocation > 0:
                arrow.xlocation += arrow.velocity
            else:
                arrows.pop(arrows.index(arrow))
        elif arrow.facing == -2 or arrow.facing == 2:
            if arrow.ylocation < windowY and arrow.ylocation > 0:
                arrow.ylocation += arrow.velocity
            else:
                arrows.pop(arrows.index(arrow))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(arrows) < 5:
            if playerChar.leftMovement:
                facing = -1
                arrows.append(copy.copy(Projectile(round(playerChar.xlocation+playerChar.playerWidth//2),
                round(playerChar.ylocation+playerChar.playerHeight//2),facing)))

            elif playerChar.rightMovement:
                facing = 1
                arrows.append(copy.copy(Projectile(round(playerChar.xlocation+playerChar.playerWidth//2),
                round(playerChar.ylocation+playerChar.playerHeight//2),facing)))

            elif playerChar.upMovement:
                facing = -2
                arrows.append(copy.copy(Projectile(round(playerChar.xlocation+playerChar.playerWidth//2),
                round(playerChar.ylocation+playerChar.playerHeight//2),facing)))

            elif playerChar.downMovement:
                facing = 2
                arrows.append(copy.copy(Projectile(round(playerChar.xlocation+playerChar.playerWidth//2),
                round(playerChar.ylocation+playerChar.playerHeight//2),facing)))


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
