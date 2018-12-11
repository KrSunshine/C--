# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:08:41 2018

@author: pAngEr
"""

import pygame, sys
from pygame.locals import *
pygame. init()

size = width, height = 1200, 650
screen = pygame.display.set_mode(size) #surface set
pygame.display.set_caption("Thos vs Isaac")

clock = pygame.time.Clock()
running = True
while running :
    end_x = pygame.mouse.get_pos()[0]
    end_y = pygame.mouse.get_pos()[1]
        
    font = pygame.font.Font(None, 140)
    Title_text = font.render("Thor vs Isaac", 1, (255,255,255))
    screen.blit(Title_text,(300,150))
    
    #image
    player_button = pygame.image.load("start.png")
    player_button2 = pygame.image.load("start2.png")
#    start = start.png, ()
    screen.blit(player_button,(535,370))
    if (535 < end_x < 655) and (370 <= end_y <= 419):
        screen.blit(player_button2,(535,370))
        pygame.time.delay(300)
        if pygame.mouse.get_pressed()[0]:
#            main() #one player class
    
    players_button = pygame.image.load("start.png")
    player_button2 = pygame.image.load("start2.png")
#    start = start.png, ()
    screen.blit(players_button,(535,430))
    if (535 < end_x < 655) and (430 <= end_y <= 479):
        screen.blit(player_button2,(535,430))
        pygame.time.delay(300)
        if pygame.mouse.get_pressed()[0]:
#            main() #two playeres class
    
    help_button = pygame.image.load("start.png")
    help_button2 = pygame.image.load("start2.png")
    help_menu = pygame.image.load("help.png")
#    start = start.png, ()
    screen.blit(help_button,(535,490))
    if (535 < end_x < 655) and (490 <= end_y <= 539):
        screen.blit(player_button2,(535,490))
        pygame.time.delay(300)
#        if pygame.mouse.get_pressed()[0]:
#            screen.blit(help_menu,(200,125))
        if pygame.mouse.get_pressed()[0]:
            screen.blit(help_menu,(200,125))
        if  (200 < end_x < 1000) and (125 <= end_y <= 525):
            pass
        else: 
           if pygame.mouse.get_pressed()[0]:
#              pygame.transform.smoothscale(help_menu,(2,1),DestSurface = None)
              
    
    pygame.display.flip()
    pygame.display.update()     
    event = pygame.event.poll()
        
    
    if event.type == QUIT:
       pygame.quit()
       sys.exit()

#def help_screen:
    
    
#def main_menu(screen):
#    font = pygame.font.Font(None, 40)
#    text = font.render("Thor vs Isaac", 1, (255,255,255))
#    screen.blit(text,(280,100))
#    
#    pygame.display.flip()
#    pygame.display.update()
#    while True:
#        for event in pygame.event.get():
#           if event.type == pygame.QUIT:
#               pygame.quit()
#               sys.exit()
#image
#player_button = pygame.image.load("")

#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            sys.exit()
            
#def main_menu(screen):
#    font = pygame.font.Font(None, 40)
#    text = font.render("Thor vs Isaac", 1, (255,255,255))
#    screen.blit(text,(280,100))
#    
#    pygame.display.flip()
#    pygame.display.update()