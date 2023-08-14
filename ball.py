# CS 172
# Filename: ball.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: The Ball class represents a ball
# Date: 8/6/2023

from drawable import Drawable
import pygame

class Ball(Drawable):
    def __init__(self, x=0, y=0, radius=0, color=(0,0,0)):
        super().__init__(x,y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 3
        self.__ySpeed = 3
        
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)
        
    def move(self):
        # Increase __x and __y by some amount
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)
        
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1
        if newY <= self.__radius or newY + self.__radius >= height:
            self.__ySpeed *= -1
            
    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius)
    
    def getYSpeed(self):
        return self.__ySpeed
    
    def setYSpeed(self, speed):
        self.__ySpeed = speed
        
    def getRadius(self):
        return self.__radius
        
