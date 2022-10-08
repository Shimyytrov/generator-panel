# 導入 imports
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

# Game loop.
while  True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        else:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Main Loop Code belongs here

    pygame.display.flip()
    fpsClock.tick(fps)