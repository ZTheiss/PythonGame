import pygame

startingBG = pygame.image.load('GeneralSprits/background.jpg')
charIdleModel = pygame.image.load('Sams/idle.png')
walkrightMovement = [pygame.image.load('Sams/r1.png'), pygame.image.load('Sams/r2.png'), pygame.image.load('Sams/r3.png'), 
pygame.image.load('Sams/r4.png'), pygame.image.load('Sams/r5.png')]

walkleftMovement = [pygame.image.load('Sams/l1.png'), pygame.image.load('Sams/l2.png'), pygame.image.load('Sams/l3.png'), 
    pygame.image.load('Sams/l4.png'), pygame.image.load('Sams/l5.png')]

walkupMovement = [pygame.image.load('Sams/u1.png'), pygame.image.load('Sams/u2.png'), pygame.image.load('Sams/u3.png'), 
    pygame.image.load('Sams/u4.png'), pygame.image.load('Sams/u5.png')]

walkdownMovement = [pygame.image.load('Sams/idle.png'), pygame.image.load('Sams/d1.png'), pygame.image.load('Sams/d2.png'), pygame.image.load('Sams/d3.png'), 
    pygame.image.load('Sams/d4.png')]

for i in range(len(walkrightMovement)):
    walkrightMovement[i] = pygame.transform.scale(walkrightMovement[i], (64,64))
for i in range(len(walkleftMovement)):
    walkleftMovement[i] = pygame.transform.scale(walkleftMovement[i], (64,64))
for i in range(len(walkupMovement)):
    walkupMovement[i] = pygame.transform.scale(walkupMovement[i], (64,64))
for i in range(len(walkdownMovement)):
    walkdownMovement[i] = pygame.transform.scale(walkdownMovement[i], (64,64))



class Player(object):
    def __init__(self, xlocation, ylocation, playerWidth, playerHeight):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.playerWidth = playerWidth
        self.playerHeight = playerHeight
        self.walkSpeed = 5
        self.walkCount = 0
        self.leftMovement = False
        self.rightMovement = False
        self.upMovement = False
        self.downMovement = False
        self.standing = True
        self.hitbox = (self.xlocation + 16, self.ylocation + 15, 30, 40) #x,y,width,height
        self.hp = 10
        self.startingHP = 10
       

    def draw(self,wind):
        if self.walkCount + 1 >= 15: #9 sprits that display for 3 frames, index error if we go longer
            self.walkCount = 0

        if not(self.standing):
            if self.leftMovement:
                wind.blit(walkleftMovement[self.walkCount//3], (self.xlocation,self.ylocation))
                self.walkCount += 1
            elif self.rightMovement:
                wind.blit(walkrightMovement[self.walkCount//3], (self.xlocation,self.ylocation))
                self.walkCount += 1
            elif self.upMovement: #Sprits need to be changed to up movement
                wind.blit(walkupMovement[self.walkCount//3], (self.xlocation,self.ylocation))
                self.walkCount += 1
            elif self.downMovement: #Sprits need to be changed to up movement
                wind.blit(walkdownMovement[self.walkCount//3], (self.xlocation,self.ylocation))
                self.walkCount += 1
        else:
            if self.leftMovement:
                wind.blit(walkleftMovement[0], (self.xlocation, self.ylocation))
            elif self.rightMovement:
                wind.blit(walkrightMovement[0], (self.xlocation, self.ylocation))
            elif self.upMovement:
                wind.blit(walkupMovement[0], (self.xlocation, self.ylocation))
            else:
                wind.blit(walkdownMovement[0], (self.xlocation, self.ylocation))
        pygame.draw.rect(wind, (255,0,0), (self.hitbox[0] - 10, self.hitbox[1] - 15, 50, 10))
        pygame.draw.rect(wind, (0,255,0), (self.hitbox[0] - 10, self.hitbox[1] - 15, 50 - (5*(self.startingHP-self.hp)), 10))
        self.hitbox = (self.xlocation + 16, self.ylocation + 15, 30, 40)
        pygame.draw.rect(wind, (255,0,0), self.hitbox,2) #REMOVE BOX
            