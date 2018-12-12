import pygame 
import os
from pygame.math import Vector2
import players
global HEIGHT
HEIGHT = 675
global WIDTH
WIDTH = 1200
global ENDZONE
ENDZONE = 15
global BORDER
BORDER = 30
VELOCITY = 15
LIVES = 30
LIVESX = 30

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

#import images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'TSArt')

screen = pygame.display.set_mode((WIDTH,HEIGHT))

Background = pygame.image.load(os.path.join(img_folder, 'airadventurelevel3.png')).convert()
Background = pygame.transform.scale(Background, (WIDTH,HEIGHT))            

sfx_throw = pygame.mixer.Sound("sfx_throw2.wav")
targethit = pygame.mixer.Sound("targethit.wav")

class Bullet(pygame.sprite.Sprite):
    def __init__(self, velocity, pos):
        pygame.sprite.Sprite.__init__(self)
        self.z = 32
        #self.image = pygame.Surface((self.z, self.z)) #Shape of bullet
        #self.image.fill((0, 0, 0))            #Bullet colour
        self.image = pygame.image.load(os.path.join(img_folder, 'sprite_1.png')).convert()
        self.image = pygame.transform.scale(self.image, (self.z, self.z))
        self.image.set_colorkey(pygame.Color("White"))
        #pygame.draw.circle(self.image, (0,255,0), (int(self.z/2), int(self.z/2)), int(self.z/2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.z, self.z) #Set position accrding to the center of the bullet
        
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

class Border1(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.Surface((WIDTH, BORDER))
       #self.image.fill((255, 255, 0))
       self.image = pygame.image.load(os.path.join(img_folder, 'applerow.png')).convert()
       self.image = pygame.transform.scale(self.image, (WIDTH, BORDER))
       self.image.set_colorkey(pygame.Color("White"))
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = 0
              
class Border2(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.Surface((WIDTH, BORDER))
       #self.image.fill((255, 255, 0))
       self.image = pygame.image.load(os.path.join(img_folder, 'ground.png')).convert()
       self.image = pygame.transform.scale(self.image, (WIDTH, BORDER))
       self.image.set_colorkey(pygame.Color("Black"))
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = HEIGHT-BORDER
       
class Endzone1(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.Surface((ENDZONE, HEIGHT-2*BORDER))
       #self.image.fill((0, 255, 0))
       self.image = pygame.image.load(os.path.join(img_folder, 'lightsaber.png')).convert()
       self.image = pygame.transform.scale(self.image, (ENDZONE, HEIGHT-2*BORDER))
       self.image.set_colorkey(pygame.Color("White"))
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = BORDER

class Endzone2(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((ENDZONE, HEIGHT-2*BORDER))
       self.image.fill((0, 255, 0))
       self.image.set_colorkey(pygame.Color("Green"))
       self.rect = self.image.get_rect()
       self.rect.x = WIDTH-ENDZONE
       self.rect.y = BORDER
       
def main ():
      
    pygame.init()
    pygame.display.set_caption("Thor(sten) vs Isaac Newton") #name of the window
    
    all_bullets = pygame.sprite.Group() 
    
    player2_group = pygame.sprite.Group()
    player2 = players.Player2(WIDTH - 41, HEIGHT//2,pygame.image.load(os.path.join(img_folder, 'Isaac.png')).convert()) #starting position of player 2
    player2_group.add(player2)
    
    player1_group = pygame.sprite.Group()
    player1 = players.Player1(150,HEIGHT//2, pygame.image.load(os.path.join(img_folder, 'Thorstenflip.png')).convert()) #starting position of player 1
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
    #divider = Divider()
    #boundary_group.add(divider)
     
    FPS = 40
    clock = pygame.time.Clock()
    counter = 5-(pygame.time.get_ticks()//1000)
    print(clock)
    
    def Timeshow(text): 
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),25) #default font size 25
        surf = myFont.render(text, False, pygame.Color("Black"), pygame.Color("Yellow")) #font and background color
        screen.blit(surf,((WIDTH//2)-50,0)) #where to put the text on
    
    def Lifeshow(text):
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),25)
        surf =  myFont.render(text,False,pygame.Color("Black"), pygame.Color("Yellow"))
        screen.blit(surf,(0,0))
    
    def aim():
        end_x = pygame.mouse.get_pos()[0]
        end_y = pygame.mouse.get_pos()[1]
        end = Vector2((end_x, end_y))
        Bullet.start = Vector2((WIDTH - 100 - ENDZONE- ((BORDER+WIDTH)//240) - players.Player2.WIDTH//2, player2.y))
        Bullet.velocity = (Bullet.start-end).normalize()*16   
        
    def collide():
            for bullet in all_bullets:
                if bullet.rect.colliderect(player1.rect):
                    targethit.play()
                    pygame.sprite.Sprite.kill(bullet)
                    if time_left>0:   
                        global LIVES
                        LIVES -=1
                if bullet.rect.colliderect(player2.rect):
                    targethit.play()
                    pygame.sprite.Sprite.kill(bullet)
                    global LIVESX
                    LIVESX -=1
    round_time = 30
    break_time = 6
    counter = round_time-(pygame.time.get_ticks()//1000)
    last_shot = 0
    SHOT_DELAY = 500
    i=0                
    
    while True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            break 
        time_left = counter-(pygame.time.get_ticks()//1000)
        if time_left <= 0:
            if i <1:
                pygame.sprite.Sprite.kill(player2)
                pygame.sprite.Sprite.kill(player1)                
                if time_left <= -break_time:
                   
                    player1 = players.Player2(WIDTH - 41, HEIGHT//2,pygame.image.load(os.path.join(img_folder, 'Thorsten.png')).convert()) #starting position of player 2
                    player2_group.add(player1)
                    player2 = players.Player1(150,HEIGHT//2, pygame.image.load(os.path.join(img_folder, 'Isaacflip.png')).convert()) #starting position of player 1
                    player1_group.add(player2)
                    
                    counter+=round_time+break_time
                    i+=1
                    continue
            else:
                break 
                
        if LIVES < 1:
            break
        if time_left > 0 :
            if e.type == pygame.MOUSEBUTTONDOWN :
                now = pygame.time.get_ticks()
                if now - last_shot >= SHOT_DELAY:
                    sfx_throw.play()
                    all_bullets.add(Bullet(Bullet.velocity, Bullet.start))
                    last_shot = now
        collide()
        all_bullets.update()
        player2_group.update()
        player1_group.update()
        boundary_group.update()
        #calculate destination and velocity
        aim()    
        # Draw / render
        clock.tick(FPS)
        
        screen.fill([255, 255, 255])
        screen.blit(Background, [0, 0])
        
        all_bullets.draw(screen)
        player2_group.draw(screen)
        player1_group.draw(screen)
        boundary_group.draw(screen)
            
        #Timeshow("Time: {}".format(seconds)) #show timer
        Timeshow("Time: {}".format(time_left))
        Lifeshow("Lives: {}  LIVESX: {}".format(LIVES, LIVESX))
         
        pygame.display.flip()
if __name__ == '__main__':
    main()
    pygame.quit() #to be able to press exit
    os._exit(0)