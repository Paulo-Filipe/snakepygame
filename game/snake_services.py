import pygame, sys

def draw_snake_tile(display, color, x, y, tile_size):
    return pygame.draw.rect(display, color, (x, y, tile_size, tile_size))


def create_snake(tile, snake_size, direction, x, y):
    snake_body = []
    for i in range(snake_size):
        snake_body.append((x + i * tile, y, direction))
    return snake_body
