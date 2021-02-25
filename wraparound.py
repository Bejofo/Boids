import time
import sys
import pygame
from pygame.locals import *
from BoidAgent import BoidAgent
from Obstacle import Obstacle
import cmath 

if __name__ == "__main__":
    pygame.init()
    global DISPLAYSURF
    global WIDTH 
    global HEIGHT
    WIDTH = 500
    HEIGHT = 400
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Drawing')
    boids = [
        BoidAgent(complex(60,60),complex(0,4),DISPLAYSURF),
        BoidAgent(complex(120,60),complex(1,-2),DISPLAYSURF),
        BoidAgent(complex(60,120),complex(1,-2),DISPLAYSURF),
        BoidAgent(complex(200,200),4*complex(-1,-2),DISPLAYSURF)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                boids.append(BoidAgent(complex(*pos),surf=DISPLAYSURF))
        DISPLAYSURF.fill((0,0,0))
        time.sleep(0.005)
        for x in boids:
            x.sense(boids,[])
            x.decide()
            x.act(0.01)
            xPos,yPos = x.pos.real,x.pos.imag
            x.pos = complex(xPos%WIDTH,yPos%HEIGHT)
            x.render()
        pygame.display.update()