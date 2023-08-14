# CS 172
# Filename: paddle.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: The Paddle class represents a paddle
# Date: 8/6/2023

from drawable import Drawable

import pygame

class Paddle(Drawable):
    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get_rect())
        
    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2, \
                           screenHeight - 20 - (self.__height), \
                           self.__width, self.__height)
    
    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width
        
    # Shorten the paddle by 1. If the width of the paddle below 50, keeps it constant
    def shorten_paddle(self):
        self.setWidth(self.getWidth() - 1)
        if self.getWidth() < 50:
            self.setWidth(50)
    
    # Wider the paddle by 1. If the width of the paddle higher than 700, keeps it constant
    def longer_paddle(self):
        self.setWidth(self.getWidth() + 1)
        if self.getWidth() > 700:
            self.setWidth(700)        
    