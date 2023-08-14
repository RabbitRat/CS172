# CS 172
# Filename: drawable.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: The Drawable class represents super class for drawable objects
# Date: 8/6/2023

from abc import ABC

class Drawable(ABC):
    def __init__(self, x=0, y=0):
        self.__visible = True
        self.__x = x
        self.__y = y
        
    def draw(self, surface):
        pass
    
    def get_rect(self):
        pass
    
    def getLoc(self):
        return (self.__x, self.__y)
    
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def isVisible(self):
        return self.__visible
    
    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False
            
    def intersects(self,other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and \
           (rect1.x + rect1.width > rect2.x) and \
           (rect1.y < rect2.y + rect2.height) and \
           (rect1.height + rect1.y > rect2.y):
            return True
        return False