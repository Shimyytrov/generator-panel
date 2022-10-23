# imports
import time
import pygame
import sys
import assets.languages.langs as langs

# configuration
fla = 0
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))
sound_endingBOOM = pygame.mixer.Sound('./assets/sounds/endingBOOM.wav')

time.sleep(1)
sound_endingBOOM.play()
time.sleep(2.1)
pygame.mixer.music.load('./assets/tracks/game_over.ogg')
pygame.mixer.music.play()

# game loop
while  True:
    screen.fill((0, 0, 0))
    # events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:  pygame.quit(), sys.exit() # quit
    
    fla += 1
    pygame.display.flip()   # update frame
    fpsClock.tick(fps)