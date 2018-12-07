import pygame 
import os
from pygame.math import Vector2

global HEIGHT
HEIGHT = 650
global WIDTH
WIDTH = 1200
global ENDZONE
ENDZONE = 15
global BORDER
BORDER = 30
VELOCITY = 15
LIVES = 3

screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Player1(pygame.sprite.Sprite):#shooter moves across a defined area in 2 dimensions

   WIDTH = 45
   HEIGHT = 60
    
   def __init__(self,x,y): #x and y are positions
       pygame.sprite.Sprite.__init__(self)
       self.x = x
       self.y = y
       self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
       self.image.fill((0, 255, 0))
       self.rect = self.image.get_rect()
       self.rect.center = (self.x, self.y)
       print(self.x)
       print(self.y)
              
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
           if self.x >= WIDTH//2- self.WIDTH:
              self.x = WIDTH//2- self.WIDTH
       elif keys[pygame.K_a]:
           self.x -=VELOCITY
           self.rect.center = (self.x, self.rect.center[1])
           if self.x <= ENDZONE + self.WIDTH -5:
              self.x = ENDZONE + self.WIDTH - 5

class Player2(pygame.sprite.Sprite): #shooter only moves up and down on y coordinate

   WIDTH = 45
   HEIGHT = 60
    
   def __init__(self,x,y): #x and y are positions
       pygame.sprite.Sprite.__init__(self)
       self.x = x
       self.y = y
       self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
       self.image.fill((0, 255, 0))
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
        if self.rect.colliderect(player1.rect):
            pygame.sprite.Sprite.kill(self)

    def aim(self):
        end_x = pygame.mouse.get_pos()[0]
        end_y = pygame.mouse.get_pos()[1]
        end = Vector2((end_x, end_y))
        self.start = Vector2((WIDTH - ENDZONE- ((BORDER+WIDTH)//240) - Player2.WIDTH//2, player2.y))
        self.velocity = (self.start-end).normalize()*16
        return self.velocity
        
class Border1(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((WIDTH, BORDER))
       self.image.fill((255, 255, 0))
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = 0
              
class Border2(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((WIDTH, BORDER))
       self.image.fill((255, 255, 0))
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = HEIGHT-BORDER
       
class Endzone1(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((ENDZONE, WIDTH-2*ENDZONE))
       self.image.fill((0, 255, 0))
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = BORDER

class Endzone2(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((ENDZONE, WIDTH-2*ENDZONE))
       self.image.fill((0, 255, 0))
       self.rect = self.image.get_rect()
       self.rect.x = WIDTH-ENDZONE
       self.rect.y = BORDER

class Divider(pygame.sprite.Sprite):
    WIDTH = 5
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((self.WIDTH, HEIGHT-(2*BORDER)))
       self.image.fill((255, 255, 255))
       self.rect = self.image.get_rect()
       self.rect.x = WIDTH//2-self.WIDTH//2
       self.rect.y = BORDER
       
pygame.init()
pygame.display.set_caption("Thor(sten) vs Isaac Newton") #name of the window

all_bullets = pygame.sprite.Group() 

player2_group = pygame.sprite.Group()
player2 = Player2(WIDTH - 41, HEIGHT//2) #starting position of player 2
player2_group.add(player2)

player1_group = pygame.sprite.Group()
player1 = Player1(40,HEIGHT//2) #starting position of player 1
player1_group.add(player1)

boundary_group = pygame.sprite.Group()
border1 = Border1()
boundary_group.add(border1)
border2 = Border2()
boundary_group.add(border2)
endzone1 = Endzone1()
boundary_group.add(endzone1)
endzone2 = Endzone2()
boundary_group.add(endzone2)
divider = Divider()
boundary_group.add(divider)


FPS = 40
clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break 
    elif e.type == pygame.MOUSEBUTTONDOWN :
        all_bullets.add(Bullet(Bullet.velocity, Bullet.start))

    all_bullets.update()
    player2_group.update()
    player1_group.update()
    boundary_group.update()
     
    #calculate destination and velocity
    Bullet.aim(Bullet)    
    # Draw / render
    clock.tick(FPS)
    
    screen.fill(pygame.Color("black")) #don't put after any draw function
    
    all_bullets.draw(screen)
    player2_group.draw(screen)
    player1_group.draw(screen)
    boundary_group.draw(screen)
     
    pygame.display.flip()
pygame.quit() #to be able to press exit
os._exit(0)