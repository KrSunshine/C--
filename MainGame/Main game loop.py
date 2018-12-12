import pygame 
import os
import time
from pygame.math import Vector2
import players
import random
import pygame, sys
from pygame.locals import *
global HEIGHT
HEIGHT = 675
global WIDTH
WIDTH = 1200
global ENDZONE
ENDZONE = 15
global BORDER
BORDER = 30
VELOCITY = 15
IsaacScore = 0
ThorstenScore = 0

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init
pygame.init()

#import images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'TSArt')

screen = pygame.display.set_mode((WIDTH,HEIGHT))
title = pygame.image.load("TSArt/title.png")
player_button = pygame.image.load("TSArt/play.png")
player_button2 = pygame.image.load("TSArt/play2.png")
help_button = pygame.image.load("TSArt/help.png")
help_button2 = pygame.image.load("TSArt/help1.png")
help_menu = pygame.image.load("TSArt/help menu.png")
left_menu = pygame.image.load("TSArt/left.png")
right_menu = pygame.image.load("TSArt/right.png")
background = pygame.image.load("TSArt/airadventurelevel1.png")
click_sound = pygame.mixer.Sound("TSArt/click.wav")
click_sound.set_volume(0.5)
Background1 = pygame.image.load("TSArt/airadventurelevel1.png")
Background2 = pygame.image.load("TSArt/airadventurelevel2.png")
Background3 = pygame.image.load("TSArt/airadventurelevel3.png")
Background4 = pygame.image.load("TSArt/airadventurelevel4.png")
#Background1 = pygame.image.load(os.path.join(img_folder, 'airadventurelevel1.png')).convert()
#Background2 = pygame.image.load(os.path.join(img_folder, 'airadventurelevel2.png')).convert()
#Background3 = pygame.image.load(os.path.join(img_folder, 'airadventurelevel3.png')).convert()
#Background4 = pygame.image.load(os.path.join(img_folder, 'airadventurelevel4.png')).convert()

pygame.mixer.music.load("Deja Vu.mp3")
pygame.mixer.music.play(-1)

r = random.randint(1,4)

def random(random):
    if random == 1:
        return Background1
    elif random == 2:
        return Background2
    elif random == 3:
        return Background3
    elif random == 4:
        return Background4
Background = random(r)

Background = pygame.transform.scale(Background, (WIDTH,HEIGHT)) 
    
sfx_throw = pygame.mixer.Sound("sfx_throw2.wav")
targethit = pygame.mixer.Sound("targethit.wav")


class Bullet(pygame.sprite.Sprite):
    def __init__(self, velocity, pos):
        pygame.sprite.Sprite.__init__(self)
        self.z = 32
        self.image = pygame.image.load(os.path.join(img_folder, 'sprite_1.png')).convert()
        self.image = pygame.transform.scale(self.image, (self.z, self.z))
        self.image.set_colorkey(pygame.Color("White"))
        #pygame.draw.circle(self.image, (0,255,0), (int(self.z/2), int(self.z/2)), int(self.z/2))
        self.rect = self.image.get_rect() #put object into a rectangle. Tt is needed to interact with other object
        self.rect.center = (self.z, self.z) #Set position accrding to the center of the bullet
        
        #init values
        self.pos = pos 
        self.velocity = velocity
        

    def update(self):
        self.pos -= self.velocity #Velocity tells where bullet go. It is set in the "aim" function
        self.rect.center = self.pos #move the bullet according to the velocity
        if self.rect.center[1]<=self.z or self.rect.center[1]>=HEIGHT - self.z: #Bouncing
            self.velocity = Vector2((self.velocity[0], -self.velocity[1]))
        if self.rect.center[0] <=0:
            pygame.sprite.Sprite.kill(self) # if we don't kill them, they will return from the other side after a while

class Border1(pygame.sprite.Sprite):
    def __init__(self): 
       pygame.sprite.Sprite.__init__(self)
       #self.image = pygame.Surface((WIDTH, BORDER))
       #self.image.fill((255, 255, 0))
       self.image = pygame.image.load(os.path.join(img_folder, 'Topborder.png')).convert()
       self.image = pygame.transform.scale(self.image, (WIDTH, BORDER))
       self.image.set_colorkey(pygame.Color("Grey"))
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
       
'''class Endzone1(pygame.sprite.Sprite):
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
       self.rect.y = BORDER'''
       
def menu ():
      
    pygame.init()
    pygame.display.set_caption("Thor(sten) vs Isaac Newton") #name of the window
    #random()
    global intro
    intro = True
    
    while intro :
        end_x = pygame.mouse.get_pos()[0]
        end_y = pygame.mouse.get_pos()[1]
        screen.fill((204,204,204)) 
        screen.blit(background,(0,0))
        screen.blit(title,(260,70))
        screen.blit(help_button,(555,460))
        screen.blit(player_button,(555,400))
        screen.blit(left_menu,(60,230))
        screen.blit(right_menu,(930,230))

        
        if (555 < end_x < 675) and (400 <= end_y <= 439):
            screen.blit(player_button2,(555,400))
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.stop()
                intro = False
                
                

        
        if (555 < end_x < 675) and (460 <= end_y <= 509):
            screen.blit(help_button2,(555,460))

            if pygame.mouse.get_pressed()[0]:
#                click_sound.paly()
                screen.blit(help_menu,(280,220))
                pygame.time.delay(200)

            else:
                pass
                  
        
        
        pygame.display.flip()
        pygame.display.update()     
        event = pygame.event.poll()
        
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
           
def main():
    all_bullets = pygame.sprite.Group()  #create a sprite group
    
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
    '''endzone1 = Endzone1()
    boundary_group.add(endzone1)
    endzone2 = Endzone2()
    boundary_group.add(endzone2)
    divider = Divider()
    boundary_group.add(divider)'''
     
    FPS = 40
    clock = pygame.time.Clock()
    
    '''def music():
        if intro == False:
            pygame.mixer.music.load("Running in the 90s.mp3")
            pygame.mixer.music.play(-1)'''
                
    def Timeshow(text): 
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),40) #default font size 25
        surf = myFont.render(text, False, pygame.Color("White")) #font and background color
        screen.blit(surf,((WIDTH//2)-50,0)) #where to put the text on
    
    def Lifeshow1(text):
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),40)
        surf =  myFont.render(text,False,pygame.Color("White"))
        screen.blit(surf,(5,0))
        
    def Lifeshow2(text):
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),40)
        surf =  myFont.render(text,False,pygame.Color("White"))
        screen.blit(surf,(953,0))
        
    def VictoryText(text):
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),70)
        surf =  myFont.render(text,False,pygame.Color("Black"))
        screen.blit(surf,(50,30))
        
    def thorstenscore(text):
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),50)
        surf =  myFont.render(text,False,pygame.Color("Black"))
        screen.blit(surf,(50,350))
    
    def isaacscore(text):
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),50)
        surf =  myFont.render(text,False,pygame.Color("Black"))
        screen.blit(surf,(50,450))
        
    def GoBack(text): #press space to go back text
        pygame.font.init()
        myFont = pygame.font.SysFont(pygame.font.get_default_font(),25)
        surf =  myFont.render(text,False,pygame.Color("Black"))
        screen.blit(surf,(WIDTH-350,HEIGHT-BORDER))
    
    
    def aim(): #set the direction of the bullet
        end_x = pygame.mouse.get_pos()[0]
        end_y = pygame.mouse.get_pos()[1]
        end = Vector2((end_x, end_y))
        Bullet.start = Vector2((WIDTH - 100 - ENDZONE- ((BORDER+WIDTH)//240) - players.Player2.WIDTH//2, player2.y))
        Bullet.velocity = (Bullet.start-end).normalize()*(VELOCITY+2) #count one step of the bullet  
        
    def collide(): #check if bullets hit the player
        for bullet in all_bullets:
            if time_left <= 0:
                pygame.sprite.Sprite.kill(bullet)
            elif bullet.rect.colliderect(player1.rect):
                 targethit.play()
                 pygame.sprite.Sprite.kill(bullet)
                 if time_left>0:   
                     global IsaacScore
                     IsaacScore +=1
            elif bullet.rect.colliderect(player2.rect):
                 targethit.play()
                 pygame.sprite.Sprite.kill(bullet)
                 global ThorstenScore
                 ThorstenScore +=1
                 
    round_time = 5 #set the time of each round
    break_time = 2 #set the time between rounds
    t0 = time.time() #start measure time from the moment of leaving the menu
    last_shot = 0 #to set a fire rate
    SHOT_DELAY = 500
    i=0  #change rounds  
    def results(): #display victory images
        if ThorstenScore < IsaacScore:
                print("Isaac wins!")
                IWin = pygame.image.load(os.path.join(img_folder, 'IsaacWin.png')).convert()
                IWin = pygame.transform.scale(IWin, (WIDTH, HEIGHT))
                screen.blit(IWin, [0, 0])
                VictoryText("Isaac WINS: I had the highground, Thor(sten)!")
                GoBack("Press SPACE to go back to the main menu")
                thorstenscore("Thorsten's Power : {}".format(ThorstenScore))
                isaacscore("Isaac's Energy : {}".format(IsaacScore))
                
        elif ThorstenScore > IsaacScore:
                print("Thorsten wins!")
                TWin = pygame.image.load(os.path.join(img_folder, 'ThorstenWin.png')).convert()
                TWin = pygame.transform.scale(TWin, (WIDTH, HEIGHT))
                screen.blit(TWin, [0, 0])
                VictoryText("Thor WINS: You never had a chance, Isaac!")
                GoBack("Press SPACE to go back to the main menu")
                thorstenscore("Thorsten's Power : {}".format(ThorstenScore))
                isaacscore("Isaac's Energy : {}".format(IsaacScore))
        else: 
                Draw = pygame.image.load(os.path.join(img_folder, 'Draw.png')).convert()
                Draw = pygame.transform.scale(Draw, (WIDTH, HEIGHT))
                screen.blit(Draw, [0, 0])
                VictoryText("DRAW: We were equally professional this time")
                GoBack("Press SPACE to go back to the main menu")
              
    gameExit = False
    while not gameExit:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        global time_left
        time_left = round_time - int(time.time()- t0)
        if time_left <= 0:
            
            if i <1:
                pygame.sprite.Sprite.kill(player2)#kill player2
                pygame.sprite.Sprite.kill(player1)#kill player1
                
                if time_left <= -break_time:
                    #create players in new locations
                    player1 = players.Player2(WIDTH - 41, HEIGHT//2,pygame.image.load(os.path.join(img_folder, 'Thorsten.png')).convert()) #starting position of player 2
                    player2_group.add(player1)
                    player2 = players.Player1(150,HEIGHT//2, pygame.image.load(os.path.join(img_folder, 'Isaacflip.png')).convert()) #starting position of player 1
                    player1_group.add(player2)
                    round_time+=round_time+break_time
                    
                    i+=1
                    False
            else:
                i +=1 
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    gameExit = True
                    menu()
                    main()
                    
                
        #if Thorstenlife < 1 or Isaaclife <1:
         #   break
        if time_left > 0 :
            if e.type == pygame.MOUSEBUTTONDOWN :
                now = pygame.time.get_ticks()
                if now - last_shot >= SHOT_DELAY: #fire rate
                    sfx_throw.play()
                    all_bullets.add(Bullet(Bullet.velocity, Bullet.start))
                    last_shot = now
        collide() #check if bullet hit a player
        all_bullets.update() #update positions of all bullets
        player2_group.update()
        player1_group.update()
        boundary_group.update()
        #calculate destination and velocity
        aim() #set the direction of the bullet    
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
        Lifeshow1("Thorsten's Power: {}".format(ThorstenScore))
        Lifeshow2("Isaac's Energy : {}".format(IsaacScore))
        if  i <1 and -break_time <= time_left <= 0:
            print(i)
            TTurn = pygame.image.load(os.path.join(img_folder, 'ThorstenTurn.png')).convert()
            TTurn = pygame.transform.scale(TTurn, (WIDTH, HEIGHT))
            screen.blit(TTurn, [0, 0])
            
        if i >2:
            results()
        pygame.display.flip()
if __name__ == '__main__':
    menu()
    main()
    pygame.quit() #to be able to press exit
    os._exit(0)