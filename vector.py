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