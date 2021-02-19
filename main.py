import time
import sys
import pygame
from pygame.locals import *
from BoidAgent import BoidAgent

if __name__ == "__main__":
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Drawing')
    boids = []
    boids.append(
        BoidAgent(complex(60,60),complex(0,4),DISPLAYSURF)
    )
    boids.append(
        BoidAgent(complex(120,60),complex(1,-2),DISPLAYSURF)
    )
    boids.append(
        BoidAgent(complex(60,120),complex(1,-2),DISPLAYSURF)
    )
    boids.append(
        BoidAgent(complex(200,200),4*complex(-1,-2),DISPLAYSURF)
    )


    while True:
        keys=pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            for b in boids:
                b.pos+= complex(2,0)
        if keys[K_RIGHT] or keys[K_d]:
            for b in boids:
                b.pos+= complex(-2,0)
        if keys[K_UP] or keys[K_w]:
            for b in boids:
                b.pos+= complex(0,2)
        if keys[K_DOWN] or keys[K_s]:
            for b in boids:
                b.pos+= complex(0,-2)
        
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
            x.sense(boids)
            x.decide()
            x.act(0.01)
            x.render()
        pygame.display.update()