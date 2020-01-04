import pygame

walkrightMovementEnemy = [pygame.image.load('EnemySprits/R1E.png'), pygame.image.load('EnemySprits/R2E.png'), pygame.image.load('EnemySprits/R3E.png'), 
pygame.image.load('EnemySprits/R4E.png'), pygame.image.load('EnemySprits/R5E.png'),pygame.image.load('EnemySprits/R4E.png'), 
pygame.image.load('EnemySprits/R6E.png'),pygame.image.load('EnemySprits/R7E.png'), pygame.image.load('EnemySprits/R8E.png'),
pygame.image.load('EnemySprits/R9E.png'),pygame.image.load('EnemySprits/R10E.png'), pygame.image.load('EnemySprits/R11E.png')]

walkleftMovementEnemy = [pygame.image.load('EnemySprits/L1E.png'), pygame.image.load('EnemySprits/L2E.png'), pygame.image.load('EnemySprits/L3E.png'), 
pygame.image.load('EnemySprits/L4E.png'), pygame.image.load('EnemySprits/L5E.png'),pygame.image.load('EnemySprits/L4E.png'), 
pygame.image.load('EnemySprits/L6E.png'),pygame.image.load('EnemySprits/L7E.png'), pygame.image.load('EnemySprits/L8E.png'),
pygame.image.load('EnemySprits/L9E.png'),pygame.image.load('EnemySprits/L10E.png'), pygame.image.load('EnemySprits/L11E.png')]

class Enemy(object):

    def __init__(self, xlocation, ylocation, widthEnemy, heightEnemy, xend, yend): 
        self.rect = pygame.image.load("EnemySprits/R1E.png").get_rect()
        self.rect.x = xlocation #Left Right
        self.rect.y = ylocation #Up Down
        self.rect.width = 28
        self.rect.height = 60
        self.widthEnemy = widthEnemy
        self.heightEnemy = heightEnemy
        self.xend = xend
        self.yend = yend
        self.path = [self.rect.x, self.xend, self.rect.y, self.yend]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.rect.x + 20, self.rect.y, 28, 60) #x,y,width,height
        self.hp = 10
        self.startingHP = 10
        self.visible = True
        

    def draw(self, wind):
        self.move()
        if self.hp > 0:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.vel > 0:
                wind.blit(walkrightMovementEnemy[self.walkCount//3], (self.rect.x, self.rect.y))
                self.walkCount += 1
            else:
                wind.blit(walkleftMovementEnemy[self.walkCount//3], (self.rect.x, self.rect.y))
                self.walkCount += 1
            self.hitbox = (self.rect.x + 20, self.rect.y, 28, 60) #x,y,width,height
            #pygame.draw.rect(wind, (255,0,0), self.hitbox,2) #REMOVE BOX
        else:
            self.visible = False


    def move(self):
        if self.vel > 0: #moving Right
            if self.rect.x + self.vel < self.path[1]: #Second element
                self.rect.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.rect.x - self.vel > self.path[0]:
                self.rect.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    
    def hit(self):
        if self.hp > 0:
            self.hp -= 1
        else:
            self.visible = False
        #print('hit')