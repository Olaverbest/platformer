import pygame, sys, random
from settings import *
from level import Level


# Setting up pygame
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

pygame_icon = pygame.image.load('imgs/tiles/grass.png')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('PLATFORMER')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('light blue')
    level.run()

    pygame.display.update()
    clock.tick(60)

# Stuff I have done! I can easily modify my level i can face both directions i have animations and gravity and collitions also i can't infininetly jump
# Stuff to do add multible levels, add more than one block, add enemies and ways to die, add scalling and fullscreen, add music, and tutorial, find good name and redo all the art,
# Make barney the eldrich dinosaur animation and improve the art lol or somthing
# ADD COOL INTRO FOR GAME
# Fix landing particle