import pygame

#controllers

controllers = {
    'LEFT':  pygame.K_LEFT,
    'RIGHT': pygame.K_RIGHT,
    'UP':    pygame.K_UP,
    'DOWN':  pygame.K_DOWN
}

forbidden_turns = {
    pygame.K_LEFT: pygame.K_RIGHT,
    pygame.K_RIGHT: pygame.K_LEFT,
    pygame.K_UP: pygame.K_DOWN,
    pygame.K_DOWN: pygame.K_UP
}