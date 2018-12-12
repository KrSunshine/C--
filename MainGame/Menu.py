import pygame 
import os


def menu ():
    pygame.init()
    pygame.display.set_caption("Thor(sten) vs Isaac Newton") #name of the window  
    start = True
    while start == True:
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break
            

    
  