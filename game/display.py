import pygame, sys 
from game import assets


# Setup a pixel display with caption
display_size = 600
score_size = 50
DISPLAY = pygame.display.set_mode((display_size, display_size))
DISPLAY.fill(assets.colors['GREEN'])
pygame.display.set_caption("Snake")

# Assign FPS a value
FPS = 60
Clock = pygame.time.Clock()
FramePerSec= Clock.tick(FPS)

def callText(txt):
    font = pygame.font.SysFont(None, 30)
    message = font.render(txt, True, assets.colors['GREEN'], assets.colors['BLACK'])
    message_rect = message.get_rect()
    message_rect.center = (display_size // 2, display_size // 2)
    return DISPLAY.blit(message, message_rect)