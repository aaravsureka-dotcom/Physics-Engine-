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
    def __init__(self,vector):
        super().__init__()
        self.radius = 10
        self.vector = vector
        self.velocity = 0
    def draw(self):
        pygame.draw.circle(screen, (255,0,0), (self.vector.x,self.vector.y),self.radius)
    def update(self,velocity):
        self.velocity += velocity
        print(self.velocity)

        self.vector.y += self.velocity









firstone = Particle(Vector2d(300,0))
secondone = Particle(Vector2d(400,300))





SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    if firstone.vector.y < 600:
        firstone.draw()
        firstone.update(velocity=0.16333333333)
    else:
        firstone.draw()


    pygame.display.flip()


    clock.tick(60)