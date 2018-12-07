# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:45:40 2018

@author: UoN Loan Laptop
"""
import pygame 
#import math 
from pygame.math import Vector2

pygame.display.set_caption("Thor(sten) vs 'Isaac Newton'")

global HEIGHT
HEIGHT = 650
global WIDTH
WIDTH = 1200
ENDZONE = 10
BORDER = 20
VELOCITY = 14

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Player1(pygame.sprite.Sprite):

   WIDTH = 45
   HEIGHT = 60
    
   def __init__(self): #x and y are positions
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((self.WIDTH,self.HEIGHT))
       self.image.fill(pygame.Color("White"))
       self.rect = self.image.get_rect()
       self.rect.x = ENDZONE + (WIDTH//240)
       self.rect.y = HEIGHT//2 - 2*BORDER
       
  ''' def show(self, colour):
       global screen
       pygame.draw.rect(screen, colour, pygame.Rect((self.x + ENDZONE + (WIDTH//240)), self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))'''
   
   def keypress(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_s]:
          self.rect.y += VELOCITY
          if not (self.rect.y <= (HEIGHT -self.HEIGHT//2 - BORDER)):
              self.rect.y = HEIGHT - self.HEIGHT//2 - BORDER
       elif keys[pygame.K_w]:
           self.rect.y -= VELOCITY
           if not (self.y >= 0 + self.HEIGHT//2 + BORDER):
               self.rect.y = 0 + self.HEIGHT//2 + BORDER
       elif keys[pygame.K_d]:
           self.rect.x += VELOCITY
           if not (self.rect.x <= (WIDTH//2)- self.WIDTH-2*ENDZONE):
              self.rect.x = (WIDTH//2 - self.WIDTH-2*ENDZONE)
       elif keys[pygame.K_a]:
           player1.moveLeft = 1
           self.rect.x -= VELOCITY
           if not (self.rect.x >= (WIDTH//500) ):
              self.rect.x = ((WIDTH//500))
              
   def update(self):
       return self.keypress()


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
       pygame.draw.rect(screen, colour, pygame.Rect(WIDTH-(WIDTH//240)-ENDZONE-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))
       
   def keypress(self):
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
       
   def update(self):
       return self.keypress()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, velocity, pos):
        self.z = 32
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.z, self.z)) #Shape of bullet
        self.image.fill((0, 0, 0))            #Bullet colour
        pygame.draw.circle(self.image, (0,255,0), (int(self.z/2), int(self.z/2)), int(self.z/2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 10, HEIGHT / 2) #Set position accrding to the center of the bullet
        
        #init values
        self.pos = pos 
        self.velocity = velocity
        

    def update(self):
        self.pos -= self.velocity
        self.rect.center = self.pos
        if self.rect.center[1]<=self.z or self.rect.center[1]>=HEIGHT - self.z: #Bouncing
            self.velocity = Vector2((self.velocity[0], -self.velocity[1]))
        if self.rect.center[0] <=0:
            pygame.sprite.Sprite.kill(self) # if we don't kill them, they will return from the other side after a while


            


pygame.init()
pygame.display.set_caption("Thor(sten) vs Isaac Newton") #name of the window

velocity = (0,0) #bullet velocity at the beginning
#start = (HEIGHT / 2, WIDTH - ENDZONE- ((BORDER+WIDTH)//240) - Player2.WIDTH//2) #start at the same place as player2
all_bullets = pygame.sprite.Group() 

all_sprites = pygame.sprite.Group()
player1 = Player1()
all_sprites.add(player1)

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
    start = Vector2((WIDTH - ENDZONE- ((BORDER+WIDTH)//240) - Player2.WIDTH//2, player2.y))
    velocity = (start-end).normalize()*16
    
    # Draw / render
    
    
    clock.tick(FPS)
    all_sprites.update()
    player1.update()
    player2.update()
    
    screen.fill(pygame.Color("black")) #don't put after any draw function
    
    all_bullets.draw(screen)
    all_sprites.draw(screen)

    pygame.draw.rect(screen, pygame.Color("yellow"), pygame.Rect(0,0,WIDTH,BORDER))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(0,BORDER,ENDZONE,HEIGHT-(2*BORDER)))
    pygame.draw.rect(screen, pygame.Color("yellow"), pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))
    pygame.draw.rect(screen, pygame.Color("red"), pygame.Rect(WIDTH-ENDZONE, BORDER, ENDZONE, HEIGHT-(2*BORDER)))
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(WIDTH//2,BORDER,2,HEIGHT-(2*BORDER)))
    
    player1.show(pygame.Color("white"))
    player2.show(pygame.Color("white")) #show player2
    pygame.display.flip()
pygame.quit() #to be able to press exit
