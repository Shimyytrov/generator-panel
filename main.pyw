# 導入 imports
from telnetlib import theNULL
import pygame
import sys

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
game_font = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 30)


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
    
    #check time for logo display
    if total_time <= 100:
        #display logo1
        logo1_line1 = game_font.render('PRODUCE BY', True, (255, 255, 255))
        logo1_line2 = game_font.render('Shimyytrov Studio', True, (255, 255, 255))
        logo_box1 = logo1_line1.get_rect()
        logo_box1.center = (width/2, height/2)
        screen.blit(logo1_line1, logo_box1)
    #time +1
    total_time += 1

    # Main Loop Code belongs here

    pygame.display.flip()
    fpsClock.tick(fps)