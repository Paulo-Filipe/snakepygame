import pygame
import sys
from pygame.locals import *


def draw_snake_tile(display, color, x, y, tile_size):
    return pygame.draw.rect(display, color, (x, y, tile_size, tile_size))


def create_snake(tile_size, snake_size, direction, x, y):
    snake_body = []
    for i in range(snake_size):
        snake_body.append((x + i * tile_size, y, direction))
    return snake_body
