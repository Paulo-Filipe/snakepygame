import pygame, sys 
from game import assets


# Setup a pixel display with caption
display_size = 600
DISPLAY = pygame.display.set_mode((display_size, display_size))
DISPLAY.fill(assets.colors['GREEN'])
pygame.display.set_caption("Snake")

# Assign FPS a value
FPS = 1
Clock = pygame.time.Clock()
FramePerSec= Clock.tick(FPS)