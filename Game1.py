import random
import pygame
import copy
from Player import *
from Projectile import *
from Enemy import *


windowX = 640 #screen.get_width()
windowY = 480 #screen.get_height()

pygame.init()
#For Debugging
wind = pygame.display.set_mode((windowX,windowY))
#wind = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screenw, screenh = pygame.display.get_surface().get_size()
pygame.display.set_caption("WolfPack")
startingBG = pygame.image.load('GeneralSprits/background.jpg')

clockFPS = pygame.time.Clock()

#Audio
arrowSound = pygame.mixer.Sound('Sounds/arrow.wav')
hitSound = pygame.mixer.Sound('Sounds/arrow.wav')
#music = pygame.mixer.music.load('Sounds/music.mp3')
#pygame.mixer.music.play(-1)

#score = 0

#Changing the GameWindow
def redrawGameWindow():
    wind.blit(startingBG, (0,0))
    #text = font.render('Score: ' + str(score), 1, (0,0,0)) #text, 1, Color
    #wind.blit(text, (390, 10)) #Put score on screen (top right)
    playerChar.draw(wind)
    if enemyExists == True:
        tempEnemy.draw(wind)
    for arrow in arrows:
        arrow.draw(wind)
    pygame.display.update()


#Main Loop
facing = 0
enemyExists = True
#font = pygame.font.SysFont('comicsans', 30, True, False) #Font, size, Bold, Italics Top right text that updates with the score
playerChar = Player(300,410,64,64)
tempEnemy = Enemy(100, 250, 64, 64, 450, 410)
arrowTimer = 0
arrows = []

run = True
while run:
    clockFPS.tick(30)

    """ if enemyExists:
        if playerChar.hitbox[1] < tempEnemy.hitbox[1] + tempEnemy.hitbox[3] and playerChar.hitbox[1] > tempEnemy.hitbox[1]:
            if playerChar.hitbox[0] < tempEnemy.hitbox[0] + tempEnemy.hitbox[2] and playerChar.hitbox[0] > tempEnemy.hitbox[0]:
                playerChar.hit(wind)
                #score += 1 """


    if enemyExists:
        if playerChar.is_collided_with(tempEnemy):
            playerChar.hit(wind)

    if enemyExists:

        if tempEnemy.visible == False:
            del tempEnemy
            enemyExists = False

    if arrowTimer > 0:
        arrowTimer += 1
    if arrowTimer > 3:
        arrowTimer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break
    i= 0
    for arrow in arrows: #Bug was checking facing, not arrow.facing
        i+=1
        if enemyExists:
            if arrow.rect.y < tempEnemy.hitbox[1] + tempEnemy.hitbox[3] and arrow.rect.y > tempEnemy.hitbox[1]:
                if arrow.rect.x < tempEnemy.hitbox[0] + tempEnemy.hitbox[2] and arrow.rect.x > tempEnemy.hitbox[0]:
                    tempEnemy.hit()
                    #score += 1
                    arrows.pop(arrows.index(arrow))
        if arrow.facing == 1 or arrow.facing == -1: #Left Right
            if arrow.rect.x < windowX and arrow.rect.x > 0:
                arrow.rect.x += arrow.velocity
            else:
                arrows.pop(arrows.index(arrow))
        elif arrow.facing == -2 or arrow.facing == 2:
            if arrow.rect.y < windowY and arrow.rect.y > 0:
                arrow.rect.y += arrow.velocity
            else:
                arrows.pop(arrows.index(arrow))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and arrowTimer == 0:
        if len(arrows) < 5:
            arrowSound.play()
            if playerChar.leftMovement:
                facing = -1
                arrows.append(copy.copy(Projectile(round(playerChar.rect.x+playerChar.playerWidth//2),
                round(playerChar.rect.y+playerChar.playerHeight//2),facing)))

            elif playerChar.rightMovement:
                facing = 1
                arrows.append(copy.copy(Projectile(round(playerChar.rect.x+playerChar.playerWidth//2),
                round(playerChar.rect.y+playerChar.playerHeight//2),facing)))

            elif playerChar.upMovement:
                facing = -2
                arrows.append(copy.copy(Projectile(round(playerChar.rect.x+playerChar.playerWidth//2),
                round(playerChar.rect.y+playerChar.playerHeight//2),facing)))

            elif playerChar.downMovement:
                facing = 2
                arrows.append(copy.copy(Projectile(round(playerChar.rect.x+playerChar.playerWidth//2),
                round(playerChar.rect.y+playerChar.playerHeight//2),facing)))
        arrowTimer = 1

    if keys[pygame.K_LEFT] and playerChar.rect.x > playerChar.walkSpeed:
        playerChar.rect.x -= playerChar.walkSpeed
        playerChar.leftMovement = True #Movement is currently left, use left sprits
        playerChar.rightMovement = False
        playerChar.upMovement = False
        playerChar.downMovement = False
        playerChar.standing = False

    elif keys[pygame.K_RIGHT] and playerChar.rect.x < screenw - playerChar.playerWidth - playerChar.walkSpeed:
        playerChar.rect.x += playerChar.walkSpeed
        playerChar.leftMovement = False
        playerChar.rightMovement = True #Movement is currently right, use right sprits
        playerChar.upMovement = False
        playerChar.downMovement = False
        playerChar.standing = False

    elif keys[pygame.K_UP] and playerChar.rect.y > playerChar.walkSpeed:
        playerChar.rect.y -= playerChar.walkSpeed
        playerChar.leftMovement = False
        playerChar.rightMovement = False
        playerChar.upMovement = True #Movement is currently up, use up sprits
        playerChar.downMovement = False
        playerChar.standing = False

    elif keys[pygame.K_DOWN] and playerChar.rect.y < screenh - playerChar.playerHeight - playerChar.walkSpeed:
        playerChar.rect.y += playerChar.walkSpeed
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
