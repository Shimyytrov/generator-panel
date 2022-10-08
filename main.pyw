# 導入 imports
from telnetlib import theNULL
import pygame
import sys

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))
font_conthrax60 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 60)
font_conthrax48 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 48)


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
        logo1_line1 = font_conthrax60.render('PRODUCE BY', True, (255, 255, 255))
        logo1_line2 = font_conthrax48.render('Shimyytrov Studio', True, (255, 255, 255))
        logo_box1 = logo1_line1.get_rect()
        logo_box1.center = (width/2, height/2)
        screen.blit(logo1_line1, logo_box1)
    #time +1
    total_time += 1

    # Main Loop Code belongs here

    pygame.display.flip()
    fpsClock.tick(fps)