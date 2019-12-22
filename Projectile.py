
import pygame

arrowLeft = pygame.image.load('GeneralSprits/arrowLeft.png')
arrowLeft = pygame.transform.scale(arrowLeft, (16,16))

arrowRight = pygame.image.load('GeneralSprits/arrowRight.png')
arrowRight = pygame.transform.scale(arrowRight, (16,16))

arrowUp = pygame.image.load('GeneralSprits/arrowUp.png')
arrowUp = pygame.transform.scale(arrowUp, (16,16))

arrowDown = pygame.image.load('GeneralSprits/arrowDown.png')
arrowDown = pygame.transform.scale(arrowDown, (16,16))

class Projectile(object):
    def __init__ (self,xlocation,ylocation,facing):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.facing = facing

        if facing == 2: #Down
            self.ylocation += 20
            self.xlocation -= 9
            self.velocity = 10 * facing
        if facing == -2: #Up
            self.ylocation -= 20
            self.xlocation -= 7.5
            self.velocity = 10 * facing
        elif facing == -1: #Left
            self.xlocation -= 30 
            self.velocity = 20 * facing #facing for direction U=-2,R=1,D=2,L=-1
        elif facing == 1: #Right
            self.xlocation += 8  
            self.velocity = 20 * facing #facing for direction U=-2,R=1,D=2,L=-1
    
    def draw(self, wind):
        if self.facing == 1:
            wind.blit(arrowRight, (self.xlocation,self.ylocation))
        elif self.facing == -1:
            wind.blit(arrowLeft, (self.xlocation,self.ylocation))
        elif self.facing == 2:
            wind.blit(arrowDown, (self.xlocation,self.ylocation))
        elif self.facing == -2:
            wind.blit(arrowUp, (self.xlocation,self.ylocation))
