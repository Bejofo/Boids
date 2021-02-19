import cmath
import math
import random
import pygame

def normalize(vec):
    if abs(vec) == 0:
        return vec
    return vec/abs(vec)

class BoidAgent():
    def __init__(self,pos=complex(0,0),vel=complex(0,0),surf=None):
        self.pos = pos
        self.vel = vel
        self.neighbors = []
        self.weights = (25,0.4,1.3)
        self.surf = surf
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
        pygame.draw.polygon(self.surf,(255,255,255),points)
        pygame.draw.circle(self.surf,(255,0,0),points[0],4)