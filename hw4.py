# CS 172
# Filename: hw4.py
# Name: Tram Phan
# Drexel ID: 14413801
# Purpose: using the Pygame graphics API to create a fun, interac+ve 2D game
# Date: 8/6/2023


import pygame
from ball import Ball
from paddle import Paddle
from text import Text
from star import Star
from triangle import Triangle
from virus import Virus
import random
import pygame.mixer

width = 800
height = 600

pygame.init()
surface = pygame.display.set_mode((800,600))
WHITE = (255,255,255)
DREXEL_YELLOW = (255, 199, 0)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

myBall = Ball(400, 300, 25, WHITE)
myPaddle = Paddle(200,25, WHITE)
myScoreBoard = Text("Score: 0", 10, 10)
myEndBoard = Text("", width // 5, height // 3, size=50)

# triangle
myTriangle = Triangle(50, 50, 0, 100, 100, 100, random.choice([RED, GREEN]))

# List for holding falling objects
falling_stars = []
falling_virus = []

# Points counter
numHits = 0

# Control rate of spawning falling objects
spawn_timer = 0

# Background
background1 = pygame.image.load('1.png')
background2 = pygame.image.load('2.png')
background3 = pygame.image.load('3.png')

# Store background images in a list
background_list = [background1, background2, background3]
selected_background = random.choice(background_list)

# pause
Pause = False

# Win/Lose
win_score = 20
lose_score = -5

# Music Win/Lose
win_sound = pygame.mixer.Sound('Win.mp3')
lose_sound = pygame.mixer.Sound('Lose.mp3')

# Earn/Lose point sound
ting_sound = pygame.mixer.Sound('Ting.mp3')
whoops_sound = pygame.mixer.Sound('Whoops.mp3')

#Background Music
background_music = pygame.mixer.Sound('Background.mp3')
background_music.set_volume(0.3)
background_music.play(-1)

running = True

while running:
    surface.fill((WHITE))
    if Pause:
        # Display message for Win/Lose state
        myEndBoard.draw(surface) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    else:
        # Background Image
        surface.blit(selected_background,(0, 0))
        pygame.display.set_caption("It's Game Time!")
        myBall.draw(surface)
        myPaddle.draw(surface)
        myScoreBoard.draw(surface)
        
        # Triangle visibility logic
        if myTriangle.is_triangle_visible():
            myTriangle.draw(surface)
        
        if myBall.intersects(myPaddle):
            myBall.setYSpeed(myBall.getYSpeed()*-1)
        
        # If the ball hits the triangle and the triangle is visible
        if myBall.intersects(myTriangle) and myTriangle.is_triangle_visible():
            # If it hits the RED triangle, shorten the paddle
            if myTriangle.getColor() == RED:
                myPaddle.shorten_paddle()
            # If it hits the GREEN triangle, wider the paddle
            elif myTriangle.getColor() == GREEN:
                myPaddle.longer_paddle()
       
        myBall.move()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and \
                      event.__dict__['key'] == pygame.K_SPACE:
                # Space to hidden triangles
                myTriangle.setVisible(not myTriangle.isVisible()) 
        
        if Pause == False:
            # Falling objects: STAR and VIRUS randomly fall from the top of the screen
            # if the ball hits a star or virus, the star and virus is removed and the
            # score is increased or decreased
            # spawn_timer control new stars and viruses are spawned.
            # Only one stars falls at a time
            if spawn_timer == 0 and len(falling_stars) < 2:
                falling_stars.append(Star(random.randint(0, width), 0, 15, DREXEL_YELLOW))
                falling_virus.append(Virus(random.randint(0, width), 0, 25))
                spawn_timer = 60 # a new star or virus will be spawned every 60 frames
            spawn_timer = max(0, spawn_timer - 1) # prevent timer going below 0
            
            # Remove object lists
            stars_to_remove =[]
            virus_to_remove = []
            
            for star in falling_stars:
                # Star falls down at random location from the top
                x1, y1 = star.getLoc()
                star.setLoc((x1, y1 + random.randint(1,5)))
                if y1 >= height:
                    star.setLoc((random.randint(0, width), 0))
                star.draw(surface)
                star.move(1)
                
                # Add objects to remove list after touching
                if myBall.intersects(star):
                    stars_to_remove.append(star)
            
            # Remove objects, update score, play sound        
            for star in stars_to_remove:
                falling_stars.remove(star)
                numHits += 2
                myScoreBoard.setMessage('Score: ' + str(numHits))
                ting_sound.play()
            
            
            for virus in falling_virus:
                # Viruses falls down at random location from the top
                x2,y2 = virus.getLoc()
                virus.setLoc((x2, y2 + random.randint(1,5)))
                if y2 >= height:
                    virus.setLoc((random.randint(0, width), 0))
                virus.draw(surface)
                virus.move(1)
                
                # Add objects to remove list after touching
                if myBall.intersects(virus):
                    virus_to_remove.append(virus)
            
            # Remove objects, update score, play sound   
            for virus in virus_to_remove:
                falling_virus.remove(virus)
                numHits -= 1
                myScoreBoard.setMessage('Score: ' + str(numHits))
                whoops_sound.play()
                
            # Check the score for special messages
            if numHits >= 18:
                myScoreBoard.setMessage("Score: " + str(numHits) + " - You're almost there!")
            
            # Check win condition
            if numHits >= win_score:
                myEndBoard.setMessage('You Win! Congratulation!')
                pygame.display.set_caption("Congratulation!")
                Pause = True
                win_sound.play()
                background_music.stop()
                
            # Check lose condition
            if numHits <= lose_score or myBall.getLoc()[1] + myBall.getRadius() >= height:
                myEndBoard.setMessage('You Lose! Try Again.')
                pygame.display.set_caption("Game Over!")
                Pause = True
                lose_sound.play()
                background_music.stop()

    pygame.display.update()
        
pygame.quit()     
exit()