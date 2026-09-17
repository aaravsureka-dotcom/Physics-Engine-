import math
import random
import sqlite3
import math
import pygame


class Vector2d:
   def __init__(self,x,y):
       self.x = x
       self.y = y
       self.vector = [self.x,self.y]
   def __repr__(self):
       return f"{self.vector}"
   def __add__(self,othervector):
       addvalue = [x + y for x,y in zip(self.vector,othervector.vector)]
       finalvalue = Vector2d(addvalue[0],addvalue[1])
       return finalvalue
   def __sub__(self,othervector):
       subval = [x - y for x,y in zip(self.vector,othervector.vector)]
       return Vector2d(subval[0],subval[1])
   def lenght(self):
       return math.sqrt(self.x**2 + self.y**2)
   def distance_to(self,other):
       diff = self - other
       return diff.lenght()

class Particle(pygame.sprite.Sprite):
    def __init__(self, vector):
        super().__init__()

        self.pos = vector
        self.radius = 0
        self.yvelocity = 0
        self.xvelocity = 0
        self.elacity = -0.88

    def draw(self,radius):
        self.radius = radius
        pygame.draw.circle(screen, (255, 0, 0), (self.pos.x, self.pos.y), self.radius)
    def update(self,gravity_change,xchange):

        self.yvelocity += gravity_change
        self.xvelocity += xchange

        self.pos.y += self.yvelocity
        self.pos.x += self.xvelocity
        if self.pos.y > (600 - self.radius):
            self.yvelocity *= self.elacity
    def collison(self,othervector):
        pass






ball_list = []


firstone = Particle(vector=Vector2d(300,0))


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
velo = 0.1633
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    firstone.draw(radius=12)
    firstone.update(gravity_change=velo,xchange=0)

    pygame.display.flip()


    clock.tick(60)