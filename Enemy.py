<<<<<<< HEAD
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
        self.xlocation = xlocation #Left Right
        self.ylocation = ylocation #Up Down
        self.widthEnemy = widthEnemy
        self.heightEnemy = heightEnemy
        self.xend = xend
        self.yend = yend
        self.path = [self.xlocation, self.xend, self.ylocation, self.yend]
        self.walkCount = 0
        self.vel = 3

    def draw(self, wind):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            wind.blit(walkrightMovementEnemy[self.walkCount//3], (self.xlocation, self.ylocation))
            self.walkCount += 1
        else:
            wind.blit(walkleftMovementEnemy[self.walkCount//3], (self.xlocation, self.ylocation))
            self.walkCount += 1
        pass

    def move(self):
        if self.vel > 0: #moving Right
            if self.xlocation + self.vel < self.path[1]: #Second element
                self.xlocation += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.xlocation - self.vel > self.path[0]:
                self.xlocation += self.vel
            else:
                self.vel = self.vel * -1
=======
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
        self.xlocation = xlocation #Left Right
        self.ylocation = ylocation #Up Down
        self.widthEnemy = widthEnemy
        self.heightEnemy = heightEnemy
        self.xend = xend
        self.yend = yend
        self.path = [self.xlocation, self.xend, self.ylocation, self.yend]
        self.walkCount = 0
        self.vel = 3

    def draw(self, wind):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            wind.blit(walkrightMovementEnemy[self.walkCount//3], (self.xlocation, self.ylocation))
            self.walkCount += 1
        else:
            wind.blit(walkleftMovementEnemy[self.walkCount//3], (self.xlocation, self.ylocation))
            self.walkCount += 1
        pass

    def move(self):
        if self.vel > 0: #moving Right
            if self.xlocation + self.vel < self.path[1]: #Second element
                self.xlocation += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.xlocation - self.vel > self.path[0]:
                self.xlocation += self.vel
            else:
                self.vel = self.vel * -1
>>>>>>> df53555c5f8e04a975181d0b78dc4fce128fc651
                self.walkCount = 0