
import pygame

class Projectile(object):
    def __init__ (self,xlocation,ylocation,radius,color,facing):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.radius = radius
        self.color = color
        self.facing = facing

        if facing == 2 or facing == -2:
            self.velocity = 40 * facing
        else:
            self.velocity = 80 * facing #facing for direction U=-2,R=1,D=2,L=-1
    
    def draw(self, wind):
        pygame.draw.circle(wind, self.color, (self.xlocation, self.ylocation), self.radius)