import pygame
import sys
from assets import *


# Setup a pixel display with caption
display_size = 600
DISPLAY = pygame.display.set_mode((display_size, display_size))
DISPLAY.fill(colors['GREEN'])
pygame.display.set_caption("Snake")

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()