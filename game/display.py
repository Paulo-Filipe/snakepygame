import pygame, sys 
from game import assets


# Setup a display with caption
display_size = 600
score_size = 60
DISPLAY = pygame.display.set_mode((display_size + 2 * score_size, display_size + 2 * score_size))
DISPLAY.fill(assets.colors['GREEN'])
pygame.display.set_caption("Snake")

# Draw stage boundaries
def stage():
    top_left_corner = (score_size,score_size)
    bottom_left_corner = (score_size, score_size + display_size)
    top_right_corner = (score_size + display_size, score_size)
    bottom_right_corner = (score_size + display_size, score_size + display_size)

    return (
    pygame.draw.line(DISPLAY,assets.colors['GREEN'],top_left_corner,top_right_corner),
    pygame.draw.line(DISPLAY,assets.colors['GREEN'],bottom_left_corner,bottom_right_corner),
    pygame.draw.line(DISPLAY,assets.colors['GREEN'],top_left_corner, bottom_left_corner),
    pygame.draw.line(DISPLAY,assets.colors['GREEN'],top_right_corner, bottom_right_corner),
    )

# Assign FPS a value
FPS = 60
Clock = pygame.time.Clock()
FramePerSec= Clock.tick(FPS)


#fontes
selected_font = 'ubuntu'
if not selected_font in pygame.font.get_fonts():
    selected_font = None

def callText(txt, posx= (display_size + score_size + 20) // 2, posy= (display_size + score_size + 20) // 2 ):
    font = pygame.font.SysFont('ubuntu', 32)
    message = font.render(txt, True, assets.colors['GREEN'], assets.colors['BLACK'])
    message_rect = message.get_rect()
    message_rect.center = (posx, posy)
    return DISPLAY.blit(message, message_rect)