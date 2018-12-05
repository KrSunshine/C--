# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 19:33:44 2018

@author: UoN Loan Laptop
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:27:22 2018
@author: User
"""

import pygame 
#import math 
from pygame.math import Vector2

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
       print(self.y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, velocity, pos):
        z = 32
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((z, z)) #Shape of bullet
        self.image.fill((0, 0, 0))            #Bullet colour
        pygame.draw.circle(self.image, (0,0,255), (int(z/2), int(z/2)), int(z/2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 10, HEIGHT / 2) #Set position accrding to the center of the bullet
        
        #init values
        self.pos = pos 
        self.velocity = velocity
        

    def update(self):
        
       # newx= self.x+self.vx
        #newy= self.y+self.vy
        
        self.pos -= self.velocity
        self.rect.center = self.pos
        '''if newx < BORDER+Bullet.RADIUS:
            #pong.play()
            self.vx = -self.vx
        elif newy < BORDER+Bullet.RADIUS or newy > HEIGHT-BORDER-Bullet.RADIUS:
            #pong.play()
            self.vy = -self.vy'''


pygame.init()
pygame.display.set_caption("Thor(sten) vs Isaac Newton") #name of the window

velocity = (0,0) #bullet velocity at the beginning
start = (HEIGHT / 2, WIDTH - 10) #start at the same place as player2
all_bullets = pygame.sprite.Group() 

player1 = Player1(0,HEIGHT//2)
player2 = Player2(0,HEIGHT//2)

FPS = 40
clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break 
    elif e.type == pygame.MOUSEBUTTONDOWN :
        all_bullets.add(Bullet(velocity, start))


    all_bullets.update()
    
    #calculate destination and velocity
    end_x = pygame.mouse.get_pos()[0]
    end_y = pygame.mouse.get_pos()[1]
    end = Vector2((end_x, end_y))
    start = Vector2((WIDTH - 10, player2.y))
    velocity = (start-end).normalize()*16
    
    # Draw / render
    
    
    clock.tick(FPS)
    player1.update()
    player2.update()
    
    screen.fill(pygame.Color("black")) #don't put after any draw function
    
    all_bullets.draw(screen)
    
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(0,0,WIDTH,BORDER))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(0,BORDER,BORDER,HEIGHT-(2*BORDER)))
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(WIDTH-BORDER, BORDER, BORDER, HEIGHT-(2*BORDER)))

    player1.show(pygame.Color("white"))
    player2.show(pygame.Color("white")) #show player2
    pygame.display.flip()
pygame.quit() #to be able to press exit