# imports
import time
import pygame
import sys
import assets.languages.langs as langs


# configuration
pygame.init()
ICON = pygame.image.load('./assets/imgs/icon.png')
pygame.display.set_icon(ICON)
pygame.display.set_caption("Generator Panel")
fps = 60
fpsClock = pygame.time.Clock()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height))
font_conthrax64 = pygame.font.Font('./assets/fonts/conthrax-sb.ttf', 64)
font_conthrax48 = pygame.font.Font('./assets/fonts/conthrax-sb.ttf', 48)
def font_mindustry(fontsize):
    return pygame.font.Font('./assets/fonts/mindustry.ttf', int(128/fontsize))
title2_pic = pygame.image.load('./assets/imgs/title_2.png')
title2_size_width, title2_size_height = title2_pic.get_size()
sound_title_1 = pygame.mixer.Sound('./assets/sounds/title_1.wav')
sound_title_2 = pygame.mixer.Sound('./assets/sounds/title_2.wav')
sound_swap = pygame.mixer.Sound('./assets/sounds/swap.wav')
sound_click = pygame.mixer.Sound('./assets/sounds/click.wav')
sound_clickBURGER = pygame.mixer.Sound('./assets/sounds/click_burger.wav')
sound_clickBRUH = pygame.mixer.Sound('./assets/sounds/click_bruh.wav')


# variables
total_time = 0
logo1_line_alpha = 255
logo2_alpha = 255
lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
langseleted1 = False
langseleted2 = False
button_cooldown = False
underline1 = 1
lang0W, lang0H = font_mindustry(3.5).render("######", True, (255,255,255)).get_size()

# functions
def renderlogo1(line_text, font, offset): # render logo1line
    logo1_line = font.render(line_text, True, (255, 255, 255))
    logo1_line.set_alpha(logo1_line_alpha)
    logo1_box = logo1_line.get_rect()
    logo1_box.center = (width/2, (height/2)+offset)
    return logo1_line, logo1_box
def renderlangs(text, color, offset): # render langs button and outline
    lang = font_mindustry(3.5).render(text, True, color)
    lang_box = lang.get_rect()
    lang_box.center = (width/2, height*(offset/10))
    langW, langH = lang.get_size()
    langoutline = pygame.Rect(0, 0 , langW+lang0W*0.2, lang0H*1.4)
    langoutline.center = (width/2, height*(offset/10))
    pygame.draw.rect(screen, (color), langoutline,  3, 4)
    screen.blit(lang, lang_box)
    return lang, langoutline
def langpressed(lang, langsec, langcolor, offset): # when langs button pressed
    global button_cooldown, Hlocation, langW, langH, langseleted2, lang1_Bcolor, lang2_Bcolor, lang3_Bcolor, lang4_Bcolor, lang5_Bcolor, lang6_Bcolor
    if not button_cooldown:
        button_cooldown = True
        lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
        langs.selected_language = langsec
        langW, langH = lang.get_size()
        Hlocation = height*(offset/10)
        langseleted2 = True
        if lang == lang5: sound_clickBURGER.play()
        elif lang == lang6: sound_clickBRUH.play()
        else: sound_click.play()
        time.sleep(0.1)
        button_cooldown = False



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
        pygame.draw.rect(screen, (255, 214, 99), ((width-(width/1.75))/2, (height/7)+(height/15), width/1.75, height/200)) # underline
        langcon = font_mindustry(3).render(langs.selected_language.text_langContinue[0], True, (255, 214, 99))
        langconW, langconH = langcon.get_size()
        langconOL = pygame.Rect(0, 0, langconW+lang0W/4, lang0H+lang0H/2)
        langconOL.center = ((width-(langconW+width*0.03)+langconW/2), (height*(9/10)+langconH/2))
        if langseleted2: # show continue button and highlight
            screen.blit(langcon, (width-(langconW+width*0.03), height*(9/10)))
            pygame.draw.rect(screen, (255, 214, 99), langconOL, 3, 4) 
            langselUL2 = pygame.Rect(0, 0, lang0H/3, lang0H*1.4)
            langselUL2.center = ((width/2)-(langW+lang0W*0.4)/2, Hlocation)
            pygame.draw.rect(screen, (255, 214, 99), langselUL2) 
        
        lang1, lang1_box = renderlangs("中文(台灣正體)", lang1_Bcolor, 3)
        lang2, lang2_box = renderlangs("中文(中国简体)", lang2_Bcolor, 4)
        lang3, lang3_box = renderlangs("English", lang3_Bcolor, 5)
        lang4, lang4_box = renderlangs("Deutsch", lang4_Bcolor, 6)
        lang5, lang5_box = renderlangs("Burgerishkiy", lang5_Bcolor, 7)
        lang6, lang6_box = renderlangs("Bruhwtf", lang6_Bcolor, 8)
        
        if lang1_box.collidepoint(mouse_pos): langpressed(lang1, langs.zhTW, lang1_Bcolor, 3); lang1_Bcolor = 255, 214, 99
        elif lang2_box.collidepoint(mouse_pos): langpressed(lang2, langs.zhCN, lang2_Bcolor, 4); lang2_Bcolor = 255, 214, 99
        elif lang3_box.collidepoint(mouse_pos): langpressed(lang3, langs.EN, lang3_Bcolor, 5); lang3_Bcolor = 255, 214, 99
        elif lang4_box.collidepoint(mouse_pos): langpressed(lang4, langs.DE, lang4_Bcolor, 6); lang4_Bcolor = 255, 214, 99
        elif lang5_box.collidepoint(mouse_pos): langpressed(lang5, langs.BURGER, lang5_Bcolor, 7); lang5_Bcolor = 255, 214, 99
        elif lang6_box.collidepoint(mouse_pos): langpressed(lang6, langs.BRUH, lang6_Bcolor, 8); lang6_Bcolor = 255, 214, 99
        elif langconOL.collidepoint(mouse_pos):   langseleted1 = True; sound_clickBURGER.stop(), sound_clickBRUH.stop(), sound_click.stop(), sound_swap.play()

    
    total_time += 1     # time +1
    pygame.display.flip()   # update frame
    fpsClock.tick(fps)