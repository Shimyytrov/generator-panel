# imports
from telnetlib import theNULL
import pygame
import sys

# configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))
font_conthrax60 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 60)
font_conthrax42 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 42)
title_1 = pygame.mixer.Sound('assets/sounds/title_1.wav')
title_2 = pygame.mixer.Sound('assets/sounds/title_2.wav')

# variables
total_time = 0
logo1_line_alpha = 255

# function to render logo1
def renderlogo1(line_text, font, offset):
    logo1_line = font.render(line_text, True, (255, 255, 255))
    logo1_line.set_alpha(logo1_line_alpha)
    logo1_box = logo1_line.get_rect()
    logo1_box.center = (width/2, (height/2)+offset)
    return logo1_line, logo1_box

# game loop
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
    
    # check time for logo display
    if 30 <= total_time <= 200:
        #fade out control
        if total_time >= 120:
            logo1_line_alpha -= 4
        elif total_time == 30:
            title_1.play()
        # render lines
        line1 = renderlogo1("PRODUCED BY", font_conthrax60, -30)
        line2 = renderlogo1("Shimyytrov Studio", font_conthrax42, +30)
        screen.blit(line1[0], line1[1])
        screen.blit(line2[0], line2[1])
        
    # time +1
    total_time += 1
    # update frame
    pygame.display.flip()
    fpsClock.tick(fps)