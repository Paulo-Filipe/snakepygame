import pygame
import sys
from pygame.locals import *


def draw_snake_tale(display, color, x, y, tile_size):
    return pygame.draw.rect(display, color, (x, y, tile_size, tile_size))
