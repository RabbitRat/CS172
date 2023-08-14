# CS 172
# Filename: triangle.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: The Triangle class represents a triangle
# Date: 8/6/2023

from drawable import Drawable
import pygame
import random

# The triangle is an object to create effects on the paddle
# I use pygame.org to find how to draw a triangle using the polygon command
# They provide the vertices for perfect triangles, so I decide to keep it vertices.
# This draws a triangle using the polygon command
#   pygame.draw.polygon(screen, "black", [[100, 100], [0, 200], [200, 200]], 5)

class Triangle(Drawable):
    __width = 800
    __height = 600

    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        super().__init__(x1,y1)
        self.__x2, self.__y2 = x2, y2
        self.__x3, self.__y3 = x3, y3
        self.__color = color
        self.show_triangle_time = pygame.time.get_ticks()
        
        
    def draw(self, surface):
        pygame.draw.polygon(surface, self.__color,  [[self.getLoc()[0], self.getLoc()[1]], [self.__x2, self.__y2], [self.__x3, self.__y3]])
            
        
    def get_rect(self):
        centerX, centerY = self.getLoc()
        # calculate half of the rect's width by finding the absolute different
        # between one of the vertices and object's center x. Do the same for half height
        halfWidth = abs(self.__x2 - centerX)
        halfHeight = abs(self.__y2 - centerY)
        topLeft_X = centerX - halfWidth
        topLeft_Y = centerY - halfHeight
        fullWidth = 2 * halfWidth
        fullHeight = 2 * halfHeight
        return pygame.Rect(topLeft_X, topLeft_Y, fullWidth, fullHeight)

    
    def getColor(self):
        return self.__color
    
    
    ''' Purpose: Checks if the triangle is visible.
        The triangle is visible if the time since it was shown is less than or equal to
        the show_triangle_duration. If the time since it was shown is greater than the
        show_triangle_duration, the triangle is not visible.
        If the triangle is visible, the function updates the triangle's position and
        color. The position is updated by randomly moving the triangle a few pixels.
        The color is updated by randomly choosing a red or green color.
 
        Return value: True if the triangle is visible, False if it is not visible.
    '''  
    def is_triangle_visible(self):
        # Variables for states. Triangle will appear for 2 seconds, then disappear, it will reappear every 6 seconds
        show_triangle_duration = 2000
        hide_duration = 4000
        show_triangle_interval = 6000
        current_time = pygame.time.get_ticks()
        RED = (255,0,0)
        GREEN = (0,255,0)
        # Using only these vertices 
        triangle_vertices = [(50, 50), (0, 100), (100, 100)]
        
        # The time passed after the triangle's last visibility
        time_since_start = current_time - self.show_triangle_time

        if time_since_start <= show_triangle_duration: # if time within the duration 2s
            return True # return True to show it will be visible
        elif show_triangle_duration < time_since_start <= hide_duration: # if time since start within the hide duration
            return False # return False to show it will be hiddenn
        elif hide_duration < time_since_start <= show_triangle_interval: # if time since start within the interval
            # Update triangle position only
            x, y = random.randint(0, Triangle.__width - 50), random.randint(0, Triangle.__height // 2 - 30)
            
            # Change location but keep vertices 
            self.setLoc((triangle_vertices[0][0] + x, triangle_vertices[0][1] + y))
            self.__x2 = triangle_vertices[1][0] + x
            self.__y2 = triangle_vertices[1][1] + y
            self.__x3 = triangle_vertices[2][0] + x
            self.__y3 = triangle_vertices[2][1] + y
            
            # Random choose Red or Green Color
            self.__color = random.choice([RED, GREEN]) 
            self.show_triangle_time = current_time
            return True # it will be visible
        else:
            return False # it will be hidden
