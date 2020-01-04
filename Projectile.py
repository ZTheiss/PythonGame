
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
        self.rect = arrowLeft.get_rect()
        self.rect.x = xlocation
        self.rect.y = ylocation
        self.facing = facing

        if facing == 2: #Down
            self.rect.x -= 9
            self.rect.y += 20
            self.velocity = 10 * facing
        if facing == -2: #Up
            self.rect.x -= 7.5
            self.rect.y -= 20
            self.velocity = 10 * facing
        elif facing == -1: #Left
            self.rect.x -= 30
            self.velocity = 20 * facing #facing for direction U=-2,R=1,D=2,L=-1
        elif facing == 1: #Right
            self.rect.x += 8 
            self.velocity = 20 * facing #facing for direction U=-2,R=1,D=2,L=-1
    
    def draw(self, wind):
        if self.facing == 1:
            wind.blit(arrowRight, (self.rect.x,self.rect.y))
        elif self.facing == -1:
            wind.blit(arrowLeft, (self.rect.x,self.rect.y))
        elif self.facing == 2:
            wind.blit(arrowDown, (self.rect.x,self.rect.y))
        elif self.facing == -2:
            wind.blit(arrowUp, (self.rect.x,self.rect.y))
