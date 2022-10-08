# 導入 imports
from telnetlib import theNULL
import pygame
import sys
# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode(
    (width, height),
    pygame.FULLSCREEN
)
imp = pygame.image.load('assets//imgs//overview_1.png')
# Game loop.
total_time = 0
while  True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if total_time <= 100:
        screen.blit(imp, (0, 0))
    total_time += 1

    # Main Loop Code belongs here

    pygame.display.flip()
    fpsClock.tick(fps)