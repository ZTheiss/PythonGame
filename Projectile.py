
import pygame

class Projectile(object):
    def __init__ (self,xlocation,ylocation,radius,color,facing):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing #facing for direction U=0,R=1,D=2,L=3
    
    def draw(wind):
        pygame.draw.circle(win, self.color, (self.xlocation, self.ylocation), self.radius)