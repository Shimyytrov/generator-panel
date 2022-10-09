# imports
import pygame
import sys
import assets.languages.langs as langs

# configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))
font_conthrax64 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 64)
font_conthrax48 = pygame.font.Font('assets/fonts/conthrax-sb.ttf', 48)
font_en = pygame.font.Font('assets/fonts/mindustry.woff', 24)
font_de = pygame.font.Font('assets/fonts/mindustry.woff', 24)
font_cn = pygame.font.Font('assets/fonts/mindustry.woff', 24)
font_tw = pygame.font.Font('assets/fonts/mindustry.woff', 24)
font_en_Heading = pygame.font.Font('assets/fonts/mindustry.woff', 72)
font_de_Heading = pygame.font.Font('assets/fonts/mindustry.woff', 72)
font_cn_Heading = pygame.font.Font('assets/fonts/mindustry.woff', 72)
font_tw_Heading = pygame.font.Font('assets/fonts/mindustry.woff', 72)
title_1 = pygame.mixer.Sound('assets/sounds/title_1.wav')
title_2 = pygame.mixer.Sound('assets/sounds/title_2.wav')
title2_pic = pygame.image.load('assets/imgs/title_2.png')
title2_size_width, title2_size_height = title2_pic.get_size()

# variables
total_time = 0
logo1_line_alpha = 255
logo2_alpha = 255

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
        line1 = renderlogo1("PRODUCED BY", font_conthrax64, -30)
        line2 = renderlogo1("Shimyytrov Studio", font_conthrax48, +30)
        screen.blit(line1[0], line1[1])
        screen.blit(line2[0], line2[1])
    if 240 <= total_time <= 400:
        title2_pic_box = pygame.transform.scale(title2_pic, (title2_size_width/2, title2_size_height/2)).get_rect()
        title2_pic.set_alpha(logo2_alpha)
        if total_time >= 310:
            logo2_alpha -= 4
        title2_pic_box.center = (width/2, (height/2))
        screen.blit(pygame.transform.scale(title2_pic, (title2_size_width/2, title2_size_height/2)), (title2_pic_box))    
    if total_time == 240:
        title_2.play()

    # time +1
    total_time += 1
    # update frame
    pygame.display.flip()
    fpsClock.tick(fps)