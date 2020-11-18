import pygame
import sys
from pygame.locals import *
from drawsnake import *
from assets import *
from display import *
from controllers import *

# Initialize program
pygame.init()

# describing snake
tile_size = 20
snake_size = 6
direction = controllers['LEFT']
position_x = display_size / 2
position_y = display_size / 2

snake = create_snake(tile_size, snake_size, direction, position_x, position_y)

# describing directions
snake_directions = {
    controllers['LEFT']:  (-tile_size, 0),
    controllers['RIGHT']: (tile_size, 0),
    controllers['UP']:    (0, -tile_size),
    controllers['DOWN']:  (0, tile_size)
}

# Beginning Game Loop
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in controllers.values():
                direction = event.key
                (x, y, old_direction) = snake[0]
                snake[0] = (x, y, direction)

    for i in range(snake_size-1, -1, -1):
        (x, y, direction) = snake[i]
        (move_x, move_y) = snake_directions[direction]
        draw_snake_tile(DISPLAY, RED, x+move_x, y+move_y, tile_size)
    pygame.display.update()

    FramePerSec.tick(FPS)
