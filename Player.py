import pygame

startingBG = pygame.image.load('GeneralSprits/bg.jpg')
charIdleModel = pygame.image.load('PlayerSprits/standing.png')
walkrightMovement = [pygame.image.load('PlayerSprits/R1.png'), pygame.image.load('PlayerSprits/R2.png'), pygame.image.load('PlayerSprits/R3.png'), 
    pygame.image.load('PlayerSprits/R4.png'), pygame.image.load('PlayerSprits/R5.png'), pygame.image.load('PlayerSprits/R6.png'), 
    pygame.image.load('PlayerSprits/R7.png'), pygame.image.load('PlayerSprits/R8.png'), pygame.image.load('PlayerSprits/R9.png')]

walkleftMovement = [pygame.image.load('PlayerSprits/L1.png'), pygame.image.load('PlayerSprits/L2.png'), pygame.image.load('PlayerSprits/L3.png'), 
    pygame.image.load('PlayerSprits/L4.png'), pygame.image.load('PlayerSprits/L5.png'), pygame.image.load('PlayerSprits/L6.png'), 
    pygame.image.load('PlayerSprits/L7.png'), pygame.image.load('PlayerSprits/L8.png'), pygame.image.load('PlayerSprits/L9.png')]

class Player(object):
    def __init__(self, xlocation, ylocation, playerWidth, playerHeight):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.playerWidth = playerWidth
        self.playerHeight = playerHeight
        self.velocity = 10
        self.walkCount = 0
        self.leftMovement = False
        self.rightMovement = False
        self.upMovement = False
        self.downMovement = False

    def draw(self,wind):
        if self.walkCount + 1 >= 27: #9 sprits that display for 3 frames, index error if we go longer
            self.walkCount = 0
        if self.leftMovement:
            wind.blit(walkleftMovement[self.walkCount//3], (self.xlocation,self.ylocation))
            self.walkCount += 1
        elif self.rightMovement:
            wind.blit(walkrightMovement[self.walkCount//3], (self.xlocation,self.ylocation))
            self.walkCount += 1
        elif self.upMovement: #Sprits need to be changed to up movement
            wind.blit(walkleftMovement[self.walkCount//3], (self.xlocation,self.ylocation))
            self.walkCount += 1
        elif self.downMovement: #Sprits need to be changed to up movement
            wind.blit(walkrightMovement[self.walkCount//3], (self.xlocation,self.ylocation))
            self.walkCount += 1
        else:
            wind.blit(charIdleModel, (self.xlocation,self.ylocation))