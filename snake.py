import pygame
import sys
from pygame.locals import *
from drawsnake import *
from assets import *
from display import *

# Initialize program
pygame.init()

# describing snake
tile_size = 20
snake_size = 6
direction = pygame.K_LEFT
position_x = display_size / 2
position_y = display_size / 2

snake = create_snake(tile_size, snake_size, direction, position_x, position_y)

# describing directions
snake_directions = {
    pygame.K_LEFT:  (-tile_size, 0),
    pygame.K_RIGHT: (tile_size, 0),
    pygame.K_UP:    (0, -tile_size),
    pygame.K_DOWN:  (0, tile_size)
}

# Beginning Game Loop
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [ pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT ]:
                print(snake_directions[event.key])

    for i in range(snake_size-1, -1, -1):
        (x, y, direction) = snake[i]
        draw_snake_tile(DISPLAY, RED, x, y, tile_size)
    pygame.display.update()

    FramePerSec.tick(FPS)
