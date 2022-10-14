# imports
from math import sin
import time
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
def font_mindustry(fontsize):
    return pygame.font.Font('assets/fonts/mindustry.ttf', int(128/fontsize))
title2_pic = pygame.image.load('assets/imgs/title_2.png')
title2_size_width, title2_size_height = title2_pic.get_size()
sound_title_1 = pygame.mixer.Sound('assets/sounds/title_1.wav')
sound_title_2 = pygame.mixer.Sound('assets/sounds/title_2.wav')
sound_swap = pygame.mixer.Sound('assets/sounds/swap.wav')
sound_click = pygame.mixer.Sound('assets/sounds/click.wav')
sound_clickBURGER = pygame.mixer.Sound('assets/sounds/click_burger.wav')
sound_clickBRUH = pygame.mixer.Sound('assets/sounds/click_bruh.wav')


# variables
total_time = 0
logo1_line_alpha = 255
logo2_alpha = 255
lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
langseleted1 = False
langseleted2 = False
button_cooldown = False
underline1 = 1

# functions
def renderlogo1(line_text, font, offset): # render logo1line
    logo1_line = font.render(line_text, True, (255, 255, 255))
    logo1_line.set_alpha(logo1_line_alpha)
    logo1_box = logo1_line.get_rect()
    logo1_box.center = (width/2, (height/2)+offset)
    return logo1_line, logo1_box
def udl1Ani(): # underline1 animation
    if 450 <= total_time <= 509 and not langseleted1:
        y=round(pow(((sin(((total_time-450)/6)/3.1416))*10), 1.42), 3)
        global underline1
        print(y)
        underline1 = underline1 + (underline1*y)/underline1
    

# game loop
while  True:
    mouse_pos = (-255, -255)
    screen.fill((0, 0, 0))

    # events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and total_time >= 450:  mouse_pos = event.pos
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:  pygame.quit(), sys.exit() # quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if 31 <= total_time <= 199:     total_time = 230
                if 241  <= total_time <= 399:   total_time = 400



    # logo display
    if total_time == 30:sound_title_1.play()
    if 30 <= total_time <= 200:     # logo 1
        if total_time >= 120:   logo1_line_alpha -= 4
        line1 = renderlogo1("PRODUCED BY", font_conthrax64, -30)
        line2 = renderlogo1("Shimyytrov Studio", font_conthrax48, +30)
        screen.blit(line1[0], line1[1])
        screen.blit(line2[0], line2[1])
    if total_time == 240:sound_title_2.play()
    if 240 <= total_time <= 400:    # logo 2
        if total_time >= 310:   logo2_alpha -= 4
        title2_pic.set_alpha(logo2_alpha)
        title2_pic_box = pygame.transform.scale(title2_pic, (title2_size_width/2, title2_size_height/2)).get_rect()
        title2_pic_box.center = (width/2, (height/2))
        screen.blit(pygame.transform.scale(title2_pic, (title2_size_width/2, title2_size_height/2)), (title2_pic_box))    



    # language select menu
    if total_time == 450: sound_swap.play()
    if total_time >= 450 and not langseleted1: # lang select
        langsel = font_mindustry(2).render(langs.selected_language.text_langSelect[0], True, (255, 255, 255))
        langsel_box = langsel.get_rect()
        langsel_box.center = (width/2, height/7)
        screen.blit(langsel, langsel_box)
        # underline
        udl1Ani()
        pygame.draw.rect(screen, (255, 214, 99), ((width-(width/1.75))/2, (height/7)+(height/15), underline1, height/150))


        langcon = font_mindustry(3).render(langs.selected_language.text_langContinue[0], True, (255, 214, 99))
        langcon_box = langcon.get_rect()
        langcon_box.center = (width*(9/10), height*(9/10))
        if langseleted2:
            screen.blit(langcon, langcon_box)
            langselUL2 = pygame.Surface((langH/3, langH))
            langselUL2.fill((255, 214, 99)) 
            screen.blit(langselUL2, ((width/2)-langW/2-langH/2 , Hlocation-langH/2))

        lang1 = font_mindustry(3.5).render("中文(台灣正體)", True, (lang1_Bcolor))
        lang1_box = lang1.get_rect()
        lang1_box.center = (width/2, height*(3/10))
        screen.blit(lang1, lang1_box)
        lang2 = font_mindustry(3.5).render("中文(中国简体)", True, (lang2_Bcolor))
        lang2_box = lang2.get_rect()
        lang2_box.center = (width/2, height*(4/10))
        screen.blit(lang2, lang2_box)
        lang3 = font_mindustry(3.5).render("English", True, (lang3_Bcolor))
        lang3_box = lang3.get_rect()
        lang3_box.center = (width/2, height*(5/10))
        screen.blit(lang3, lang3_box)
        lang4 = font_mindustry(3.5).render("Deutsch", True, (lang4_Bcolor))
        lang4_box = lang4.get_rect()
        lang4_box.center = (width/2, height*(6/10))
        screen.blit(lang4, lang4_box)
        lang5 = font_mindustry(3.5).render("Burgerishkiy", True, (lang5_Bcolor))
        lang5_box = lang5.get_rect()
        lang5_box.center = (width/2, height*(7/10))
        screen.blit(lang5, lang5_box)
        lang6 = font_mindustry(3.5).render("Bruhwtf", True, (lang6_Bcolor))
        lang6_box = lang6.get_rect()
        lang6_box.center = (width/2, height*(8/10))
        screen.blit(lang6, lang6_box)
        
        if lang1_box.collidepoint(mouse_pos):
            if not button_cooldown:
                button_cooldown = True
                langW, langH = lang1.get_size()
                sound_click.play()
                langs.selected_language = langs.zhTW
                lang1_Bcolor = 255, 214, 99
                lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
                Hlocation = height*(3/10)
                langseleted2 = True
                time.sleep(0.1)
                button_cooldown = False
        elif lang2_box.collidepoint(mouse_pos):
            if not button_cooldown:
                button_cooldown = True
                langW, langH = lang2.get_size()
                sound_click.play()
                langs.selected_language = langs.zhCN
                lang2_Bcolor = 255, 214, 99
                lang1_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
                Hlocation = height*(4/10)
                langseleted2 = True
                time.sleep(0.1)
                button_cooldown = False
        elif lang3_box.collidepoint(mouse_pos):
            if not button_cooldown:
                button_cooldown = True
                langW, langH = lang3.get_size()
                sound_click.play()
                langs.selected_language = langs.EN
                lang3_Bcolor = 255, 214, 99
                lang1_Bcolor = lang2_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
                Hlocation = height*(5/10)
                langseleted2 = True
                time.sleep(0.1)
                button_cooldown = False
        elif lang4_box.collidepoint(mouse_pos):
            if not button_cooldown:
                button_cooldown = True
                langW, langH = lang4.get_size()
                sound_click.play()
                langs.selected_language = langs.DE
                lang4_Bcolor = 255, 214, 99
                lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
                Hlocation = height*(6/10)
                langseleted2 = True
                time.sleep(0.1)
                button_cooldown = False
        elif lang5_box.collidepoint(mouse_pos):
            if not button_cooldown:
                button_cooldown = True
                langW, langH = lang5.get_size()
                sound_clickBURGER.play()
                langs.selected_language = langs.BURGER
                lang5_Bcolor = 255, 214, 99
                lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang6_Bcolor = 255, 255, 255
                Hlocation = height*(7/10)
                langseleted2 = True
                time.sleep(0.1)
                button_cooldown = False
        elif lang6_box.collidepoint(mouse_pos):
            if not button_cooldown:
                button_cooldown = True
                langW, langH = lang6.get_size()
                sound_clickBRUH.play()
                langs.selected_language = langs.BRUH
                lang6_Bcolor = 255, 214, 99
                lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = 255, 255, 255
                Hlocation = height*(8/10)
                langseleted2 = True
                time.sleep(0.1)
                button_cooldown = False
                
        if langcon_box.collidepoint(mouse_pos):
            langseleted1 = True

    # time +1
    total_time += 1
    # update frame
    pygame.display.flip()
    fpsClock.tick(fps)