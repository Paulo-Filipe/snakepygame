import pygame, sys, random
from game import display


def draw_snake_tile(display, color, x, y, tile_size):
    return pygame.draw.rect(display, color, (x, y, tile_size, tile_size))


def create_snake(tile, snake_size, direction, x, y):
    snake_body = []
    for i in range(snake_size):
        snake_body.append((x + i * tile, y, direction))
    return snake_body


def isInSnake(snake, food):
    (x_food, y_food) = food
    for tile in snake:
        (x_tile, y_tile, direction_tile) = tile
        if x_tile == x_food and y_tile == y_food:
            return True
    return False


def spawn_food(tile_size, snake, food):
    (x_food, y_food) = food
    while isInSnake(snake, (x_food, y_food)) or (x_food, y_food) == (None, None):
        x = random.randrange(0, display.display_size, tile_size)
        y = random.randrange(0, display.display_size, tile_size)
        (x_food, y_food) = (x, y)
    return (x_food, y_food)


def add_tile(snake, snake_directions):
    (last_x, last_y, last_direction) = snake[-1]

    (dir_x, dir_y) = snake_directions[last_direction]

    snake.append((last_x + (dir_x * -1), last_y + (dir_y * -1), last_direction))

def check_collision(snake):
    (x_0, y_0, direction_0) = snake[0]
    collision = False
    for i in range(3, len(snake)):
        (x_i, y_i, direction_i) = snake[i]
        if x_0 == x_i and y_0 == y_i:
            collision = True
            break
    return collision
