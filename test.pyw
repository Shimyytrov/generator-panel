import pygame
import sys
from random import randint
pygame.init()
screen_info = pygame.display.Info() # get screen info
width, height = screen_info.current_w, screen_info.current_h    # get screen (width, height)
screen = pygame.display.set_mode((width, height))   # full screen
screen.fill((0, 255, 0))
fps = 60    # fps
fps_clock = pygame.time.Clock() # clock
r, g, b = 0, 255, 128
running = True
r_max = False
g_max = True
b_max = False
while running:
    pygame.display.flip()   # update frame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: # quit
            pygame.quit()
            sys.exit()
    if 0 <= r < 255 and not r_max:
        r += 1
    elif r == 255 and not r_max:
        r_max = True
    elif 0 < r <= 255 and r_max:
        r -= 1
    elif r == 0 and r_max:
        r_max = False
    if 0 <= g < 255 and not g_max:
        g += 1
    elif g == 255 and not g_max:
        g_max = True
    elif 0 < g <= 255 and g_max:
        g -= 1
    elif g == 0 and g_max:
        g_max = False
    if 0 <= b < 255 and not b_max:
        b += 2
    elif b == 255 and not b_max:
        b_max = True
    elif 0 < b <= 255 and b_max:
        b -= 1
    elif b == 0 and b_max:
        b_max = False
    
    if b > 255:
        b = 255
    screen.fill((r, g, b))
    fps_clock.tick(fps)