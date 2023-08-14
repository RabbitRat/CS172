# CS 172
# Filename: virus.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: The Virus class represents a virus
# Date: 8/6/2023

from drawable import Drawable
import pygame

# I want to create an object that player can lose points. I use the code in Lab5
# to draw snowflake. I change the color to purple to make it looks like virus.
# I also increase the size to 25 to make it easy to see

class Virus(Drawable):
    def __init__(self, x, y=0, size=25):
        super().__init__(x,y)
        
        
    def draw(self, surface):
        x,y = self.getLoc()
        # line 1
        pygame.draw.line(surface, (128,0,128), (x - 5, y), (x + 5, y)) 
        # line 2
        pygame.draw.line(surface, (128,0,128), (x, y - 5), (x, y + 5))
        # line 3
        pygame.draw.line(surface, (128,0,128), (x - 5, y - 5), (x + 5, y + 5))
        # line 4
        pygame.draw.line(surface, (128,0,128), (x - 5, y + 5), (x + 5, y - 5))
        
    
                
    def move(self, p):
        newX, newY = self.getLoc()
        self.setLoc((newX, newY + p/100))

    
    # Draw rectangle outside of the VIRUS object
    def get_rect(self):
        location = self.getLoc()
        return pygame.Rect(location[0] - 25/ 2, location[1] - 25 / 2, 25, 25)