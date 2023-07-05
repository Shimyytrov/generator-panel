import pygame
import sys
from random import randint
pygame.init()
screen_info = pygame.display.Info() # get screen info
width, height = screen_info.current_w, screen_info.current_h    # get screen (width, height)
screen = pygame.display.set_mode((width, height))   # full screen
screen.fill((0, 255, 0))
running = True
while running:
    pygame.display.flip()   # update frame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: # quit
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            screen.fill((r, g, b))