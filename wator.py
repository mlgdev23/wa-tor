from creature import Creature
from fish import Fish
from shark import Shark

import pygame, random, ipdb

BACKGROUND = (255, 255, 255)
OCEAN = (79, 66, 181)

OCEAN_CODE = 0
FISH_CODE = 1
SHARK_CODE = 2

# Constants

CELLSIZE = 8
MARGIN = 2
WIDTH = 100
HEIGHT = 75
WINDOW_X = 1000 
WINDOW_Y = 750    # 4:3 aspect ratio for 2D

NUM_FISH = 120 # these will eventually come from command line
NUM_SHARK = 40

class World():
    
    # populate ocean with fish and sharks
    def populate_ocean(self, ocean_grid, type):
        
        # Choose a random location on ocean_grid
        populated = False
        while not populated:
            row = random.randint(0, HEIGHT - 1)
            col = random.randint(0, WIDTH -1)
            
            # if location OCEAN_CODE, it is ok to populate
            if ocean_grid[row][col] == OCEAN_CODE:
                populated = True
                
        if type == "f":
            ocean_grid[row][col] = FISH_CODE
            Fish(row, col)
        elif type == "s":
            ocean_grid[row][col] = SHARK_CODE
            Shark(row, col)
                
    
    # update world - drawing function based on current grid contents
    
    # initialize world with 0's (ocean)
    def init_world_grid(self):
        world_grid = []
        
        for y in range(0, HEIGHT):
            world_grid.append([])
            for x in range(0, WIDTH):
                world_grid[y].append(OCEAN_CODE)
        return world_grid


def main():
    # initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("The World of Wa-Tor")
    
    # create World - the world_grid represents what's to be displayed on screen
    world = World()
    
    world_initialized = False
    
    # populate world with random creatures
    while not world_initialized:
        screen.fill(BACKGROUND)
        brand_new_world = world.init_world_grid()
        for _ in range(NUM_FISH):
            world.populate_ocean(brand_new_world, "f")
        for _ in range(NUM_SHARK):
            world.populate_ocean(brand_new_world, "s")
        world_initialized = True
    
    # simulation loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()
        
        
if __name__ == '__main__':
    main()

