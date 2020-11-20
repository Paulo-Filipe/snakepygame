import pygame
import sys
import random
from game import assets, controls, display, snake_services


# Initialize program
pygame.init()

# describing snake
tile_size = 20
snake_size = 5
snake_color = assets.colors['WHITE']
direction = controls.controllers['LEFT']
position_x = display.display_size / 2
position_y = display.display_size / 2

snake = snake_services.create_snake(
    tile_size, snake_size, direction, position_x, position_y)

# describing the background
background_color = assets.colors['BLACK']

# describing directions
snake_directions = {
    controls.controllers['LEFT']:  (-tile_size, 0),
    controls.controllers['RIGHT']: (tile_size, 0),
    controls.controllers['UP']:    (0, -tile_size),
    controls.controllers['DOWN']:  (0, tile_size)
}
# defines the limits where the snake will be drawn.
legal_display_range = display.display_size

# points controller
points = 0
frame_counter = 0
food_spawn_interval = 20
food_pos = (None, None)

# Beginning Main Game Loop
while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key in controls.controllers.values() and controls.forbidden_turns[direction] != event.key:
            direction = event.key
            (x, y, old_direction) = snake[0]
            snake[0] = (x, y, direction)  # change the direction of the head.

    # reset the screen
    display.DISPLAY.fill(background_color)

    # Check for colisions between head and body.
    if snake_services.check_collision(snake):
        pygame.quit()
        sys.exit()

    # Check for incrising the snake size - collision with food - spawn food.
    if frame_counter < food_spawn_interval:
        if food_pos != (None, None):
            (x_food_pos, y_food_pos) = food_pos
            snake_services.draw_snake_tile(display.DISPLAY, snake_color, x_food_pos, y_food_pos, tile_size)

        frame_counter += 1

    else:
        frame_counter = 0
        if food_pos == (None, None):
            (x_rand, y_rand) = snake_services.spawn_food(tile_size, snake, food_pos)
            food_pos = (x_rand, y_rand)
            snake_services.draw_snake_tile(display.DISPLAY, snake_color, x_rand, y_rand, tile_size)

    if food_pos != (None, None) and snake_services.isInSnake(snake, food_pos):
        snake_services.add_tile(snake, snake_directions)
        snake_size += 1
        food_pos = (None, None)


    #start computing movement
    for i in range(snake_size-1, -1, -1):
        (x, y, direction) = snake[i]
        (move_x, move_y) = snake_directions[direction]
        new_pos_x = (x + move_x) % legal_display_range
        new_pos_y = (y + move_y) % legal_display_range

        # draw on new position.
        snake_services.draw_snake_tile(
            display.DISPLAY, snake_color, new_pos_x, new_pos_y, tile_size)

        if i == 0:  # change all directions, except for the head. update all positions.
            snake[i] = (new_pos_x, new_pos_y, direction)
        else:
            (next_x, next_y, next_direction) = snake[i-1]
            snake[i] = (new_pos_x, new_pos_y, next_direction)

    pygame.display.update()

    display.FramePerSec
