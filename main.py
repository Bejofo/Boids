import time
import sys
import pygame
from pygame.locals import *
from BoidAgent import BoidAgent
from Obstacle import Obstacle

if __name__ == "__main__":
    pygame.init()
    global DISPLAYSURF
    global WIDTH 
    global HEIGHT
    WIDTH = 500
    HEIGHT = 400
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Drawing')
    boids = [
        BoidAgent(complex(60,60),complex(0,4),DISPLAYSURF),
        BoidAgent(complex(120,60),complex(1,-2),DISPLAYSURF),
        BoidAgent(complex(60,120),complex(1,-2),DISPLAYSURF),
        BoidAgent(complex(200,200),4*complex(-1,-2),DISPLAYSURF)
    ]

    obstacles = [
        Obstacle(complex(350,300),DISPLAYSURF)
    ]
    # for x in range(0,400,10):
    #     obstacles.append(Obstacle(complex(0,x),DISPLAYSURF))
    #     obstacles.append(Obstacle(complex(400,x),DISPLAYSURF))
    #     obstacles.append(Obstacle(complex(x,0),DISPLAYSURF))
    #     obstacles.append(Obstacle(complex(x,400),DISPLAYSURF))

    def move_everything(vec):
        for b in boids:
            b.pos+= vec
        for o in obstacles:
            o.pos+=vec

    while True:
        keys=pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            move_everything( complex(2,0))
        if keys[K_RIGHT] or keys[K_d]:
            move_everything( complex(-2,0))
        if keys[K_UP] or keys[K_w]:
            move_everything(  complex(0,2))
        if keys[K_DOWN] or keys[K_s]:
            move_everything(  complex(0,-2))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                boids.append(BoidAgent(complex(*pos),surf=DISPLAYSURF))
            if event.type == pygame.KEYDOWN:
                if event.key == K_x: # x key
                    BoidAgent.DRAW_CIRCLE = not BoidAgent.DRAW_CIRCLE
        DISPLAYSURF.fill((0,0,0))
        time.sleep(0.005)
        for x in boids:
            x.sense(boids,obstacles)
            x.decide()
            x.act(0.01)
            x.render()
        for o in obstacles:
            o.render()
        pygame.display.update()