import cmath
import math
import pygame, sys
from pygame.locals import *
import time 
import random

pygame.init()
global DISPLAYSURF
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

def normalize(vec):
    if abs(vec) == 0:
        return vec
    return vec/abs(vec)

class BoidAgent():
    def __init__(self,pos=complex(0,0),vel=complex(0,0)):
        self.pos = pos
        self.vel = vel
        self.neighbors = []
        self.weights = (25,0.4,1.3)
        # seperation, aligment ,coehsinon

    def sense(self,n):
        self.neighbors = []
        for x in n:
            if x != self and abs(x.pos-self.pos) < 100:
                self.neighbors.append(x)
    
    def decide(self):
        self.separation()
        self.alignment()
        self.cohesion()

    def act(self,dt):
        if abs(self.vel) == 0:
            return 
        self.pos+=normalize(self.vel)*dt*20

    def goto(self,target,strength):
        deltaPos = target-self.pos
        deltaPos = normalize(deltaPos)
        self.vel+= deltaPos*strength 

    def separation(self):
        tempVec = complex(0,0)
        if len(self.neighbors) == 0:
            return
        for n in self.neighbors:
            dist = abs(n.pos-self.pos)
            distanceScaling = 1/dist
            self.goto(n.pos,-self.weights[0]*distanceScaling)
    
    def alignment(self):
        if len(self.neighbors) == 0:
            return
        tempVec = sum([n.vel for n in self.neighbors])
        tempVec = normalize(tempVec)
        self.vel += self.weights[1]*tempVec/ len(self.neighbors)

    def cohesion(self):
        if len(self.neighbors) == 0:
            return
        meanPos = sum([n.pos for n in self.neighbors]) / len(self.neighbors)
        self.goto(meanPos,self.weights[2])

    def render(self):
        angle = cmath.phase(self.vel)
        points = []
        theta = 0
        for _ in range(3):
            cart = cmath.rect(7,angle+theta)
            x,y = cart.real,cart.imag
            points.append((self.pos.real+x,self.pos.imag+y))
            theta+= (2*math.pi)/3
        pygame.draw.polygon(DISPLAYSURF,(255,255,255),points)
        pygame.draw.circle(DISPLAYSURF,(255,0,0),points[0],4)



boids = []

# for _ in range(30):
#     boids.append(
#         BoidAgent(
#             complex(random.randint(0,200),random.randint(0,200)),
#             complex(random.randint(-6,6),random.randint(-6,6))
#             )
    # )
boids.append(
    BoidAgent(complex(60,60),complex(0,4))
)
boids.append(
    BoidAgent(complex(120,60),complex(1,-2))
)
boids.append(
    BoidAgent(complex(60,120),complex(1,-2))
)
boids.append(
    BoidAgent(complex(200,200),4*complex(-1,-2))
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
            boids.append(BoidAgent(complex(*pos)))

    DISPLAYSURF.fill((0,0,0))
    time.sleep(0.005)
    for x in boids:
        x.sense(boids)
        x.decide()
        x.act(0.01)
        x.render()
    pygame.display.update()