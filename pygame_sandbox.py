import pygame

pygame.init()

color = (255, 255, 255)
rect_color = (255, 0, 0)

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My Python Image")

image = pygame.image.load("assets/Screenshot 2023-10-24 at 1.23.08 PM.png")
exit = False

while not exit:
    canvas.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas, rect_color, pygame.Rect(30, 30, 60, 60))

    pygame.display.update()
