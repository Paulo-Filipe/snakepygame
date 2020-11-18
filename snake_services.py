import pygame
import sys
from controls import *

tile_size = 20

# describing directions
snake_directions = {
    controllers['LEFT']:  (-tile_size, 0),
    controllers['RIGHT']: (tile_size, 0),
    controllers['UP']:    (0, -tile_size),
    controllers['DOWN']:  (0, tile_size)
}

def draw_snake_tile(display, color, x, y, tile_size):
    return pygame.draw.rect(display, color, (x, y, tile_size, tile_size))


def create_snake(tile, snake_size, direction, x, y):
    snake_body = []
    for i in range(snake_size):
        snake_body.append((x + i * tile, y, direction))
    return snake_body
