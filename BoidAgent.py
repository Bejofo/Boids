import cmath
import math
import random
import pygame

def normalize(vec):
    if abs(vec) == 0:
        return vec
    return vec/abs(vec)

class BoidAgent():
    BOID_SIZE = 7
    SENSE_RADIUS = 90
    WEIGHTS = (1.1,1,1.1,0.1)
    INERTIA =0.6
    DRAW_CIRCLE = True
    # seperation, aligment ,coehsinon,randomness
    def __init__(self,pos=complex(0,0),vel=complex(10,0),surf=None):
        self.pos = pos
        self.vel = vel
        self.accel = complex(0,0)
        self.neighbors = []
        self.obstacles = [] 
        self.surf = surf
    
    def sense(self,n,o):
        self.neighbors = []
        self.obstacles =[]
        for x in n:
            if x != self and abs(x.pos-self.pos) < self.SENSE_RADIUS:
                self.neighbors.append(x)
        for x in o:
            if x != self and abs(x.pos-self.pos) < self.SENSE_RADIUS:
                self.obstacles.append(x)
    
    def decide(self):
        self.accel += self.separation() * self.WEIGHTS[0]
        self.accel += self.alignment() * self.WEIGHTS[1]
        self.accel += self.cohesion() * self.WEIGHTS[2]
        self.accel += cmath.rect(self.WEIGHTS[3], random.uniform(0, math.pi*2))

    def act(self,dt):
        self.vel+= self.accel*self.INERTIA
        if abs(self.vel) > 20:
            self.vel = normalize(self.vel)*20
        self.pos+=self.vel*dt
        self.accel = complex(0,0)

    def separation(self):
        if len(self.neighbors+self.obstacles) == 0:
            return complex(0,0)
        tempVec = complex(0,0)
        tempVec = sum([normalize(self.pos-n.pos)/abs(self.pos-n.pos)  for n in self.neighbors+self.obstacles])
        return normalize(tempVec)

    def alignment(self):
        if len(self.neighbors) == 0:
            return complex(0,0)
        tempVec = sum([n.vel for n in self.neighbors])
        tempVec = normalize(tempVec)
        return tempVec/ len(self.neighbors)

    def cohesion(self):
        if len(self.neighbors) == 0:
            return complex(0,0)
        meanPos = sum([n.pos for n in self.neighbors]) / len(self.neighbors)
        return normalize(meanPos-self.pos)

    def render(self):
        angle = cmath.phase(self.vel)
        points = []
        theta = 0
        for _ in range(3):
            cart = cmath.rect(self.BOID_SIZE,angle+theta)
            x,y = cart.real,cart.imag
            points.append((self.pos.real+x,self.pos.imag+y))
            theta+= (2*math.pi)/3
        pygame.draw.polygon(self.surf,(255,255,255),points)
        pygame.draw.circle(self.surf,(255,0,0),points[0],4)
        if self.DRAW_CIRCLE:
            pygame.draw.circle(self.surf,(0,255,0),points[0],self.SENSE_RADIUS,width=1)