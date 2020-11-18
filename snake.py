import pygame, sys
from pygame.locals import *
from drawsnake import *

# Initialize program
pygame.init()

# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
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


#describing snake
tile_size = 20
initial_snake_size = 6
initial_position_x = display_size / 2
initial_position_y = display_size / 2
 
# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    for i in range(initial_snake_size):
        draw_snake_tile(DISPLAY, RED, initial_position_x+i*tile_size, initial_position_y, tile_size)
    pygame.display.update()
   
    FramePerSec.tick(FPS)