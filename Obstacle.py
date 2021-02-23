import pygame
import cmath 
class Obstacle():
    RADIUS = 5
    def __init__(self,pos=complex(0,0),surf=None):
        self.pos = pos
        self.surf = surf
    def render(self):
        pygame.draw.circle(self.surf,(255,255,255),(self.pos.real,self.pos.imag),self.RADIUS)