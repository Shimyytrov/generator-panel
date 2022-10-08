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
font_conthrax42 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 42)

pygame.mixer.init()
title_1 = pygame.mixer.Sound('assets/sounds/title_1.wav')
title_2 = pygame.mixer.Sound('assets/sounds/title_2.wav')


# Game loop.
total_time = 0
logo1_line1_alpha = 255
logo1_line1_alpha = 255
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
    if 30 <= total_time <= 200:
        #display logo1

        #fade out control
        if total_time >= 120:
            logo1_line1_alpha -= 2
            logo1_line1_alpha -= 2
        #render lines
        logo1_line1 = font_conthrax60.render('PRODUCE BY', True, (255, 255, 255))
        logo1_line2 = font_conthrax42.render('Shimyytrov Studio', True, (255, 255, 255))
        logo1_line1.set_alpha(logo1_line1_alpha)
        logo1_line2.set_alpha(logo1_line1_alpha)
        logo_box1 = logo1_line1.get_rect()
        logo_box1.center = (width/2, (height/2)-30)
        logo_box2 = logo1_line2.get_rect()
        logo_box2.center = (width/2, (height/2)+30)
        screen.blit(logo1_line1, logo_box1)
        screen.blit(logo1_line2, logo_box2)
        if total_time == 30:
            title_1.play()
        
    #time +1
    total_time += 1

    # Main Loop Code belongs here
    pygame.display.flip()
    fpsClock.tick(fps)