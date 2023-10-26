from creature import Creature
from fish import Fish
from shark import Shark

import pygame, random

OCEAN = (79, 66, 181)

# Constants

CELLSIZE = 8
MARGIN = 2
WIDTH = 90
HEIGHT = 60
WINDOW_X = 900
WINDOW_Y = 600

class World():
    # "spawn" creatures
    
    # update world - drawing function based on current grid contents
    
    # initialize world with 0's (ocean)
    pass


def main():
    # initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("The World of Wa-Tor")
    
    # create World
    # populate with random
    
    # simulation loop
    running = True
    while running:
        screen.fill(OCEAN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()
        
        
if __name__ == '__main__':
    main()

