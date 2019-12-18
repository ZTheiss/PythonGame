import pygame
import random

pygame.init()
#For Debugging
wind = pygame.display.set_mode((500,480))
#wind = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screenw, screenh = pygame.display.get_surface().get_size()

pygame.display.set_caption("WolfPack")

walkrightMovement = [pygame.image.load('PlayerSprits/R1.png'), pygame.image.load('PlayerSprits/R2.png'), pygame.image.load('PlayerSprits/R3.png'), 
    pygame.image.load('PlayerSprits/R4.png'), pygame.image.load('PlayerSprits/R5.png'), pygame.image.load('PlayerSprits/R6.png'), 
    pygame.image.load('PlayerSprits/R7.png'), pygame.image.load('PlayerSprits/R8.png'), pygame.image.load('PlayerSprits/R9.png')]

walkleftMovement = [pygame.image.load('PlayerSprits/L1.png'), pygame.image.load('PlayerSprits/L2.png'), pygame.image.load('PlayerSprits/L3.png'), 
    pygame.image.load('PlayerSprits/L4.png'), pygame.image.load('PlayerSprits/L5.png'), pygame.image.load('PlayerSprits/L6.png'), 
    pygame.image.load('PlayerSprits/L7.png'), pygame.image.load('PlayerSprits/L8.png'), pygame.image.load('PlayerSprits/L9.png')]

startingBG = pygame.image.load('GeneralSprits/bg.jpg')
charIdleModel = pygame.image.load('PlayerSprits/standing.png')

clockFPS = pygame.time.Clock()

xlocation = 50
ylocation = 400
playerWidth = 64
playerHeight = 64
velocity = 15
leftMovement = False
rightMovement = False
upMovement = False
downMovement = False
walkCount = 0

#Changing the GameWindow
def redrawGameWindow():
    global walkCount
    wind.blit(startingBG, (0,0))
    
    if walkCount + 1 >= 27: #9 sprits that display for 3 frames, index error if we go longer
        walkCount = 0
    if leftMovement:
        wind.blit(walkleftMovement[walkCount//3], (xlocation,ylocation))
        walkCount += 1
    elif rightMovement:
        wind.blit(walkrightMovement[walkCount//3], (xlocation,ylocation))
        walkCount += 1
    elif upMovement: #Sprits need to be changed to up movement
        wind.blit(walkleftMovement[walkCount//3], (xlocation,ylocation))
        walkCount += 1
    elif downMovement: #Sprits need to be changed to up movement
        wind.blit(walkrightMovement[walkCount//3], (xlocation,ylocation))
        walkCount += 1
    else:
        wind.blit(charIdleModel, (xlocation,ylocation))

    pygame.display.update()


#Main Loop
run = True
while run:
    clockFPS.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xlocation > velocity:
        xlocation -= velocity
        leftMovement = True #Movement is currently left, use left sprits
        rightMovement = False
        upMovement = False
        downMovement = False

    elif keys[pygame.K_RIGHT] and xlocation < screenw - playerWidth - velocity:
        xlocation += velocity
        leftMovement = False
        rightMovement = True #Movement is currently right, use right sprits
        upMovement = False
        downMovement = False

    elif keys[pygame.K_UP] and ylocation > velocity:
        ylocation -= velocity
        leftMovement = False
        rightMovement = False
        upMovement = True #Movement is currently up, use up sprits
        downMovement = False

    elif keys[pygame.K_DOWN] and ylocation < screenh - playerHeight -velocity:
        ylocation += velocity
        leftMovement = False
        rightMovement = False
        upMovement = False
        downMovement = True #Movement is currently down, use down sprits

    else:
        leftMovement = False
        rightMovement = False
        upMovement = False
        downMovement = False
        walkCount = 0

    redrawGameWindow()
    

pygame.quit()


