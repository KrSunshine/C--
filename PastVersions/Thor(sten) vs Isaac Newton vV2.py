#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:26:43 2018

@author: KenarKrSunshine
"""

import pygame 
import os

pygame.display.set_caption("Thor(sten) vs 'Isaac Newton'")

HEIGHT = 650
WIDTH = 1200
BORDER = 10
VELOCITY = 14

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Player1:

   WIDTH = 45
   HEIGHT = 60
    
   def __init__(self,x,y): #x and y are positions
       self.x = x
       self.y = y
       self.moveUp = 0
       self.moveDown = 0
       self.moveRight = 0
       self.moveLeft = 0
       
   def show(self, colour):
       global screen
       pygame.draw.rect(screen, colour, pygame.Rect((BORDER+WIDTH//240), self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))
       
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_s]:
          player1.moveDown = 1
          self.y += (self.moveDown - self.moveUp) + VELOCITY
          if not (self.y <= (HEIGHT -self.HEIGHT//2 - BORDER)):
              self.y = HEIGHT - self.HEIGHT//2 - BORDER
       elif keys[pygame.K_w]:
           player1.moveUP = 1
           self.y -= (self.moveDown - self.moveUp) + VELOCITY
           if not (self.y >= 0 + self.HEIGHT//2 + BORDER):
               self.y = 0 + self.HEIGHT//2 + BORDER
       elif keys[pygame.K_d]:
           player1.moveRight = 1
           self.x += (self.moveRight - self.moveLeft)+ VELOCITY
       elif keys[pygame.K_a]:
           player1.moveLeft = 1
           self.x -= (self.moveRight - self.moveLeft)+ VELOCITY


class Player2: #shooter only moves up and down on y coordinate

   WIDTH = 45
   HEIGHT = 60
    
   def __init__(self,x,y): #x and y are positions
       self.x = x
       self.y = y
       self.moveUp = 0
       self.moveDown = 0
       
   def show(self, colour):
       global screen
       pygame.draw.rect(screen, colour, pygame.Rect(WIDTH-(BORDER+WIDTH//240)-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))
       
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_DOWN]:
          player2.moveDown = 1
          self.y += (self.moveDown - self.moveUp) + VELOCITY
          if not (self.y <= (HEIGHT -self.HEIGHT//2 - BORDER)):
              self.y = HEIGHT - self.HEIGHT//2 - BORDER
       elif keys[pygame.K_UP]:
           player2.moveUP = 1
           self.y -= (self.moveDown - self.moveUp) + VELOCITY
           if not (self.y >= 0 + self.HEIGHT//2 + BORDER):
               self.y = 0 + self.HEIGHT//2 + BORDER
       #self.x = self.x + (self.moveR - self.moveL)+ VELOCITY

pygame.init()

player1 = Player1(0,HEIGHT//2)
player2 = Player2(0,HEIGHT//2)

FPS = 40
clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break    
    clock.tick(FPS)
    player1.update()
    player2.update()
    screen.fill(pygame.Color("black")) #don't put after any draw function
    
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(0,0,WIDTH,BORDER))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(0,BORDER,BORDER,HEIGHT-(2*BORDER)))
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(WIDTH-BORDER, BORDER, BORDER, HEIGHT-(2*BORDER)))

    player1.show(pygame.Color("white"))
    player2.show(pygame.Color("white")) #show player2
    pygame.display.flip()
pygame.quit() #to be able to press exit
os._exit(0) #MAC
