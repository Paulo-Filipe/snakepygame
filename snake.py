import pygame
import sys
from pygame.locals import *
from drawsnake import *

# Initialize program
pygame.init()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a pixel display with caption
display_size = 600
DISPLAY = pygame.display.set_mode((display_size, display_size))
DISPLAY.fill(GREEN)
pygame.display.set_caption("Snake")

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()


# describing snake
tile_size = 20
snake_size = 6
direction = 'LEFT'
position_x = display_size / 2
position_y = display_size / 2

snake_body = []
for i in range(snake_size):
    snake_body.append( (position_x + i * tile_size, position_y, direction) )

# describing directions
snake_directions = {
    'LEFT':  (-tile_size, 0),
    'RIGHT': (tile_size, 0),
    'UP':    (0, -tile_size),
    'DOWN':  (0, tile_size)
}

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for i in range(snake_size):
        (x, y, direction) = snake_body[i]
        draw_snake_tile(DISPLAY, RED, x, y, tile_size)
    pygame.display.update()

    FramePerSec.tick(FPS)
