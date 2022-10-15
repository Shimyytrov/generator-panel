# imports
import time
import pygame
import sys

# configuration
fla = 0
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))

pygame.mixer.music.load('./assets/tracks/normal.ogg')
pygame.mixer.music.play(loops=2, fade_ms=2000)
pygame.mixer.music.fadeout(time=2000)
pygame.mixer.music.unload('./assets/tracks/normal.ogg')

# game loop
while  True:
    screen.fill((0, 0, 0))
    # events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:  pygame.quit(), sys.exit() # quit
    
    fla += 1
    pygame.display.flip()   # update frame
    fpsClock.tick(fps)