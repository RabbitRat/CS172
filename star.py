# CS 172
# Filename: star.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: The Star class represents a star
# Date: 8/6/2023

from drawable import Drawable
import pygame
import math

# The star is an object to earn points

class Star(Drawable):
    def __init__(self, x=0, y=0, radius=0, color=(0,0,0), speed=1):
        super().__init__(x,y)
        self.__radius = radius
        self.__color = color
        self.__speed = speed
                
    # It is quite different to draw a perfect star. I create a list of points to represent
    # the vertices of the star, using trigonometry
    def draw(self, surface):
        points = []
        for i in range(5):
            # loop through 5 time (= create 5 vertices of a star)
            angle = 2 * math.pi * i / 5 # find angle of current vertex
            x1 = self.getLoc()[0] + self.__radius * math.cos(angle) # calculate x of outer point of the vertex
            y1 = self.getLoc()[1] + self.__radius * math.sin(angle) # calculate y of outer point
            x2 = self.getLoc()[0] + self.__radius * 0.5 * math.cos(angle + math.pi / 5) # calculate x of inner point
            y2 = self.getLoc()[1] + self.__radius * 0.5 * math.sin(angle + math.pi / 5) # calculate y of innter point
            points.append((x1, y1)) # append outer points to the points list
            points.append((x2, y2)) # append inner points to the points list
        pygame.draw.polygon(surface, self.__color, points)
            
    def move(self, p):
        newX, newY = self.getLoc()
        self.setLoc((newX, newY + p/100))

    # Top left corner of the rectangle is taking from subtracting the radius from the x and y
    # of location. Width and Height are 2 times radius. It is a square!
    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius)