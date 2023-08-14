Drexel University
CS 172 - Homework 4
Name: Tram Phan
Drexel ID: 14413801
Purpose: Pingpong Game using the Pygame library

Wellcome to the Ball Game!

---Game Instructions---
Description: You need to use the paddle to control a ball and hit falling objects while avoiding certain triangles. The triangle will randomly appear in the screen. There are 2 types of triangles RED and GREEN that have different effects on the paddle. There are two falling objects: STAR and VIRUS. You can earn points by hitting the STAR and lose points when hitting the VIRUS. The objects will fall randomly from the top of the screen. 

To avoid too many objects falling at a time, I write some codes to make sure only one star fall at a time. Also, there are only 1 triangle appears on the screen. It will be visible for 2 seconds. Every 6 seconds, it will be reappear. 

You can win the game by getting 20 points. You will lose the game if the ball reach the bottom of the screen and if your point is below 5. When you win or lose, the game will be paused, a message will appear. The score will be counted and display at the left top corner. When you are 18 points, a brief message will notify you that you are on the brink of winning the game.

To make the game more appealing, I add backgrounds and music. Everytime you open the game, it will display a random background in the list of three. The music will be played forever. There is also a funny sound when you hit the STAR or the VIRUS

#HACK TIP: You can press spacebar to make all the Triangle invisible for an easy win game!


Game Element:
yellow star: 2 points
purple virus: -1 point
red triangle: shorten the paddle 
green triangle: wider the paddle

How to Win:
Get 20 points to win the game

How to Lose:
The ball hit the bottom of the screen
Points are below 5

