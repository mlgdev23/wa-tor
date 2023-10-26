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


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("The World of Wa-Tor")
    
    running = True
    while running:
        screen.fill(OCEAN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()
        
        
if __name__ == '__main__':
    main()

