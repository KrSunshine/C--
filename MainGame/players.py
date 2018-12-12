import pygame 
import os

HEIGHT = 675
WIDTH = 1200
ENDZONE = 15
BORDER = 30
VELOCITY = 15

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'TSArt')



class Player1(pygame.sprite.Sprite):#shooter moves across a defined area in 2 dimensions

   WIDTH = 75
   HEIGHT = 100
    
   def __init__(self,x,y,image): #x and y are positions
       pygame.sprite.Sprite.__init__(self)
       self.x = x
       self.y = y
       self.image =image 
       self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
       self.image.set_colorkey(pygame.Color("White"))
       self.rect = self.image.get_rect()
       self.rect.center = (self.x, self.y)

              
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_s]:
          self.y += VELOCITY
          self.rect.center = (self.rect.center[0], self.y)
          if self.y >= HEIGHT -self.HEIGHT - BORDER + 12 :
              self.y = HEIGHT - self.HEIGHT - BORDER + 12
       elif keys[pygame.K_w]:
           self.y -=VELOCITY
           self.rect.center = (self.rect.center[0], self.y)
           if self.y <= self.HEIGHT + BORDER - 12:
               self.y = self.HEIGHT + BORDER - 12
       elif keys[pygame.K_d]:
           self.x += VELOCITY
           self.rect.center = (self.x, self.rect.center[1])
           if self.x >= WIDTH - self.WIDTH -200:
              self.x = WIDTH - self.WIDTH -200
       elif keys[pygame.K_a]:
           self.x -=VELOCITY
           self.rect.center = (self.x, self.rect.center[1])
           if self.x <= ENDZONE + self.WIDTH - 17:
              self.x = ENDZONE + self.WIDTH - 17

class Player2(pygame.sprite.Sprite): #shooter only moves up and down on y coordinate

   WIDTH = 75
   HEIGHT = 100
    
   def __init__(self,x,y, image): #x and y are positions
       pygame.sprite.Sprite.__init__(self)
       self.x = x
       self.y = y
       self.image = image 
       self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
       self.image.set_colorkey(pygame.Color("White"))
       self.rect = self.image.get_rect()
       self.rect.center = (self.x, self.y)
          
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_DOWN]:
          self.y +=VELOCITY
          self.rect.center = (self.rect.center[0], self.y)
          if self.y >= HEIGHT -self.HEIGHT - BORDER + 12:
              self.y = HEIGHT -self.HEIGHT - BORDER + 12
       elif keys[pygame.K_UP]:
           self.y -= VELOCITY
           self.rect.center = (self.rect.center[0], self.y)
           if self.y <= self.HEIGHT + BORDER - 12:
               self.y = self.HEIGHT + BORDER - 12