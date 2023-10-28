from creature import Creature
from fish import Fish
from shark import Shark

import pygame, random, ipdb, sys

BACKGROUND = (128, 128, 128)
OCEAN_COLOR = (79, 66, 181)
FISH_COLOR = (255, 153, 153)

OCEAN_CODE = 0
FISH_CODE = 1
SHARK_CODE = 2


# Constants

CELLSIZE = 8
MARGIN = 2
WIDTH = 90
HEIGHT = 60
WINDOW_X = 900
WINDOW_Y = 600

NUM_FISH = 120  # these will eventually come from command line
NUM_SHARK = 40
NUM_CHRONONS = 1000
FRAMERATE = 20


class World:
    # populate ocean with fish and sharks
    def populate_ocean(self, ocean_grid, type):
        # Choose a random location on ocean_grid
        populated = False
        while not populated:
            row = random.randint(0, HEIGHT - 1)
            col = random.randint(0, WIDTH - 1)

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
    # eventually try colored rectangles with text
    def update_world(self, current_grid, screen):
        for row in range(0, HEIGHT):
            for col in range(0, WIDTH):
                if current_grid[row][col] == FISH_CODE:
                    color = FISH_COLOR
                else:
                    color = OCEAN_COLOR
                pygame.draw.rect(
                    screen,
                    color,
                    [
                        (MARGIN + CELLSIZE) * col + MARGIN,
                        (MARGIN + CELLSIZE) * row + MARGIN,
                        CELLSIZE,
                        CELLSIZE,
                    ],
                )

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
    clock = pygame.time.Clock()
    chronons = NUM_CHRONONS

    # populate world with random creatures
    world_initialized = False
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

        if chronons > 0:
            # DO: check the status of each creature - pass reference to present ocean_grid
            world.update_world(brand_new_world, screen)
            chronons -= 1

        pygame.display.flip()
        clock.tick(FRAMERATE)

    # ipdb.set_trace()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
