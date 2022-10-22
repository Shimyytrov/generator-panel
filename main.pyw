#========== imports ==========#
import time
import pygame
import sys
import assets.languages.langs as langs
import random
import math

#========== configuration ==========#
pygame.init()
ICON = pygame.image.load('./assets/imgs/icon.png')  # load icon
pygame.display.set_icon(ICON)   # set icon
pygame.display.set_caption("Generator Panel")   # set caption
fps = 60    # fps
fps_clock = pygame.time.Clock() # clock
screen_info = pygame.display.Info() # get screen info
width, height = screen_info.current_w, screen_info.current_h    # get screen (width, height)
screen = pygame.display.set_mode((width, height))   # full screen
# load font
font_conthrax64 = pygame.font.Font('./assets/fonts/conthrax-sb.ttf', 64)
font_conthrax48 = pygame.font.Font('./assets/fonts/conthrax-sb.ttf', 48)
def font_mindustry(fontsize):   # load font custom size function
    return pygame.font.Font('./assets/fonts/mindustry.ttf', int(128/fontsize))
# load imgs
title2_pic = pygame.image.load('./assets/imgs/title_2.png').convert()
start_screen_bg = pygame.image.load('./assets/imgs/sprites/room1/startscreen.png').convert()
start_core = pygame.image.load('./assets/imgs/sprites/room1/core-blackout.png').convert_alpha()
title2_size_width, title2_size_height = title2_pic.get_size()
# load sfx
sound_title_1 = pygame.mixer.Sound('./assets/sounds/title_1.wav')
sound_title_2 = pygame.mixer.Sound('./assets/sounds/title_2.wav')
sound_swap = pygame.mixer.Sound('./assets/sounds/swap.wav')
sound_click = pygame.mixer.Sound('./assets/sounds/click.wav')
sound_clickBURGER = pygame.mixer.Sound('./assets/sounds/click_burger.wav')
sound_clickBRUH = pygame.mixer.Sound('./assets/sounds/click_bruh.wav')
sound_endingBOOM = pygame.mixer.Sound('./assets/sounds/endingBOOM.wav')
def play_track(file, loop, fade_ms):    # play track function
    pygame.mixer.music.load(f'./assets/tracks/{file}.ogg')
    pygame.mixer.music.play(loop, fade_ms)



#========== variables ==========#
total_time = 0  # track time
logo2_alpha = logo1_line_alpha = 255 # variables for logo fadout
lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255 # languages button color control
lang_selected2 = False # variables for detecting after language selected (done intro)
lang_selected1 = False # variables for detecting after language pressed (button pressed)
button_cooldown = False # variable for button cooldown
lang0W, lang0H = font_mindustry(3.5).render("######", True, (255,255,255)).get_size()   # default use font size (width, height)
title_delay = False # variable for controlling title delay
one_time_var = False    # variables for controlling one-time use function
game_start_alpha = 0    # variable for controlling start button aphla


#========== functions ============#
def one_time(i): # make things run only once
    global one_time_var
    if i == one_time_var:
        return False
    else:
        one_time_var = i
        return True
def render_logo1(line_text, font, offset): # render logo1line
    logo1_line = font.render(line_text, True, (255, 255, 255))
    logo1_line.set_alpha(logo1_line_alpha)
    logo1_rec = logo1_line.get_rect()
    logo1_rec.center = (width/2, (height/2)+offset)
    return logo1_line, logo1_rec
def render_langs(text, color, offset): # render langs button and outline
    lang = font_mindustry(3.5).render(text, True, color)
    lang_rec = lang.get_rect()
    lang_rec.center = (width/2, height*(offset/10))
    langW, langH = lang.get_size()
    lang_outline = pygame.Rect(0, 0 , langW+lang0W*0.2, lang0H*1.4)
    lang_outline.center = (width/2, height*(offset/10))
    pygame.draw.rect(screen, (color), lang_outline,  3, 4)
    screen.blit(lang, lang_rec)
    return lang, lang_outline
def lang_pressed(lang, langsec, langcolor, offset): # when langs button pressed
    global button_cooldown, Hlocation, langW, langH, lang_selected1, lang1_Bcolor, lang2_Bcolor, lang3_Bcolor, lang4_Bcolor, lang5_Bcolor, lang6_Bcolor
    if not button_cooldown:
        button_cooldown = True
        lang1_Bcolor = lang2_Bcolor = lang3_Bcolor = lang4_Bcolor = lang5_Bcolor = lang6_Bcolor = 255, 255, 255
        langs.selected_language = langsec
        langW, langH = lang.get_size()
        Hlocation = height*(offset/10)
        lang_selected1 = True
        if lang == lang5:
            sound_clickBURGER.play()
        elif lang == lang6:
            sound_clickBRUH.play()
        else:
            sound_click.play()
        time.sleep(0.1)
        button_cooldown = False
def render_game_title(): # render the game title with delays
    global title_delay, total_time
    title_delay = True
    if total_time == 0:
        total_time = 1
    if total_time >= 60:
        screen.blit(game_title1, game_title1_rec)
    if total_time == 60:
        sound_title_1.play()
    if total_time >= 120:
        screen.blit(game_title2, game_title2_rec)
    if total_time == 120:
        sound_endingBOOM.play()
    if total_time == 240:
        play_track("title", -1, 0)
    if total_time >= 300:
        global game_start_alpha
        game_start_alpha += 2
        game_start.set_alpha(game_start_alpha)
        screen.blit(game_start, game_start_rec)
    if total_time == 600:
        title_delay = False
def drawbloom(cirs, expand, dens, center, color):   # draw light bloom effect
    surf = pygame.Surface((((dens*(cirs-1))+expand)*2,((dens*(cirs-1))+expand)*2))
    surfW, surfH = surf.get_size()
    for i in range(cirs):
        i += 1
        pygame.draw.circle(surf, ((color[0]*i)/cirs, (color[1]*i)/cirs, (color[2]*i)/cirs), (surfW/2, surfH/2), (dens*(cirs-i))+expand)
    surf_rec = surf.get_rect()
    surf_rec.center = center
    screen.blit(surf, surf_rec, special_flags = pygame.BLEND_RGB_ADD)


#========== intro loop ==========#
while not lang_selected2:
    mouse_pos = (-255, -255)
    screen.fill((0, 0, 0))

    # events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and total_time >= 450:
            mouse_pos = event.pos
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: # quit
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # skipping logo
                if 31 <= total_time <= 199:
                    total_time = 230
                if 241  <= total_time <= 399:
                    total_time = 400



    # logo display
    if total_time == 30:
        sound_title_1.play()
    if 30 <= total_time <= 200:     # logo 1
        if total_time >= 120:
            logo1_line_alpha -= 4
        line1 = render_logo1("PRODUCED BY", font_conthrax64, -30)
        line2 = render_logo1("Shimyytrov Studio", font_conthrax48, +30)
        screen.blit(line1[0], line1[1])
        screen.blit(line2[0], line2[1])
    if total_time == 240:
        sound_title_2.play()
    if 240 <= total_time <= 400:    # logo 2
        if total_time >= 310:
            logo2_alpha -= 4
        title2_pic.set_alpha(logo2_alpha)
        if one_time("title2_pic_render"):
            title2_pic_rec = pygame.transform.scale(title2_pic, (title2_size_width/2, title2_size_height/2)).get_rect()
            title2_pic_rec.center = (width/2, (height/2))
        screen.blit(pygame.transform.scale(title2_pic, (title2_size_width/2, title2_size_height/2)), (title2_pic_rec))    



    # language select menu
    if total_time == 450:
        sound_swap.play()
    if total_time >= 450 and not lang_selected2: # lang select
        if one_time("lang_sel_render"):
            lang_sel = font_mindustry(2).render(langs.selected_language.text_lang_select[0], True, (255, 255, 255))
            lang_sel_rec = lang_sel.get_rect()
            lang_sel_rec.center = (width/2, height/7)
        screen.blit(lang_sel, lang_sel_rec)
        pygame.draw.rect(screen, (255, 214, 99), ((width-(width/1.75))/2, (height/7)+(height/15), width/1.75, height/200)) # underline
        if one_time("lang_con_render"):
            lang_con = font_mindustry(3).render(langs.selected_language.text_lang_continue[0], True, (255, 214, 99))
            lang_conW, lang_conH = lang_con.get_size()
            lang_conOL = pygame.Rect(0, 0, lang_conW+lang0W/4, lang0H+lang0H/2)
            lang_conOL.center = ((width-(lang_conW+width*0.03)+lang_conW/2), (height*(9/10)+lang_conH/2))
        if lang_selected1: # show continue button and highlight
            screen.blit(lang_con, (width-(lang_conW+width*0.03), height*(9/10)))
            pygame.draw.rect(screen, (255, 214, 99), lang_conOL, 3, 4) 
            if one_time("lang_selUL2_render"):
                lang_selUL2 = pygame.Rect(0, 0, lang0H/3, lang0H*1.4)
                lang_selUL2.center = ((width/2)-(langW+lang0W*0.4)/2, Hlocation)
            pygame.draw.rect(screen, (255, 214, 99), lang_selUL2) 
        
        lang1, lang1_rec = render_langs("中文(台灣正體)", lang1_Bcolor, 3)
        lang2, lang2_rec = render_langs("中文(中国简体)", lang2_Bcolor, 4)
        lang3, lang3_rec = render_langs("English", lang3_Bcolor, 5)
        lang4, lang4_rec = render_langs("Deutsch", lang4_Bcolor, 6)
        lang5, lang5_rec = render_langs("Burgerishkiy", lang5_Bcolor, 7)
        lang6, lang6_rec = render_langs("Bruhwtf", lang6_Bcolor, 8)
        
        if lang1_rec.collidepoint(mouse_pos):
            lang_pressed(lang1, langs.zhTW, lang1_Bcolor, 3)
            lang1_Bcolor = 255, 214, 99
        elif lang2_rec.collidepoint(mouse_pos):
            lang_pressed(lang2, langs.zhCN, lang2_Bcolor, 4)
            lang2_Bcolor = 255, 214, 99
        elif lang3_rec.collidepoint(mouse_pos): 
            lang_pressed(lang3, langs.EN, lang3_Bcolor, 5)
            lang3_Bcolor = 255, 214, 99
        elif lang4_rec.collidepoint(mouse_pos): 
            lang_pressed(lang4, langs.DE, lang4_Bcolor, 6)
            lang4_Bcolor = 255, 214, 99
        elif lang5_rec.collidepoint(mouse_pos): 
            lang_pressed(lang5, langs.BURGER, lang5_Bcolor, 7)
            lang5_Bcolor = 255, 214, 99
        elif lang6_rec.collidepoint(mouse_pos): 
            lang_pressed(lang6, langs.BRUH, lang6_Bcolor, 8)
            lang6_Bcolor = 255, 214, 99
        elif lang_conOL.collidepoint(mouse_pos):
            for i in [sound_clickBURGER, sound_clickBRUH, sound_click]:
                i.stop()
            sound_swap.play()
            lang_selected2 = True
            total_time = 0
    
    if not lang_selected2:
        total_time += 1 # time +1
    pygame.display.flip()   # update frame
    fps_clock.tick(fps)


#========== game loop ==========#
while lang_selected2:
    mouse_pos = (-255, -255)
    screen.fill((0, 0, 0))

    #----- events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: # quit
            pygame.quit()
            sys.exit()


    #----- start screen
    if one_time("game_tile1_render"): # load all things in start screen 
        game_title1 = font_mindustry(3).render(langs.selected_language.text_title1[0], True, (255, 214, 99)) # title 1
        game_title1W, game_title1H = game_title1.get_size()
        game_title1_rec = game_title1.get_rect()
        game_title1_rec.center = (width/2, height/8) # get title 1 center to position
        game_title2 = font_mindustry(1.6).render(langs.selected_language.text_title2[0], True, (255, 255, 255)) # title 2
        game_title2W, game_title2H = game_title2.get_size()
        game_title2_rec = game_title2.get_rect()
        game_title2_rec.center = (width/2, (height/8)+(game_title1H)+(game_title1H/2))# get title 2 center to position
        game_start = font_mindustry(3).render(langs.selected_language.text_play[0], True, (255, 255, 255)) # start button
        game_startW, game_startH = game_start.get_size()
        game_start_rec = game_start.get_rect()
        game_start_rec.center = (width/2, height*7/8) # get start button center to position
        start_screen_bgW, start_screen_bgH = start_screen_bg.get_size()
        start_screen_bg = pygame.transform.scale(start_screen_bg, (start_screen_bgW*12, start_screen_bgH*12)) # scale background
        start_screen_bg_rec = start_screen_bg.get_rect()
        start_screen_bg_rec.center = (width/2, height/2)  # get background center to position  
        start_coreW, start_coreH = start_core.get_size()
        start_core = pygame.transform.scale(start_core, (start_coreW*12, start_coreH*12)) # scale core
        velocity_x = velocity_y = 0 # set velocity variables
        offset = [0, 0] # offset variable for core shake
        inter = [0, 0]  # inter foce variable for core pulling back to center
        shake = 10 # shake variable for shake cooldwon
        start_center = (width/2, height/2)
        core_ang = 0 # variable for core angle

    #----- core spin and shake
    core_ang -= 0.1 # spins core
    if core_ang == -360:
        core_ang = 0
    rotated_start_core = pygame.transform.rotate(start_core, core_ang)
    shake -= 1 # shake cooldown
    if shake == 0:
        shake = 10
    inter[0] = (offset[0])/2 # inter force to make sure not flies away
    inter[1] = (offset[1])/2
    if shake == 10: # create offset
        offset[0] += random.randint(int(-10-inter[0]), int(10-inter[0]))
        offset[1] += random.randint(int(-10-inter[1]), int(10-inter[1]))
    end_center = (width/2)+offset[0], (height/2)+offset[1] # find end point
    if shake >= 5: # deceleration
        acc_x = shake
        acc_y = shake
    else: # acceleration
        acc_x = ((10-shake)+velocity_x/shake)+shake
        acc_y = ((10-shake)+velocity_y/shake)+shake
    distance_x = start_center[0]-end_center[0] # get x distance
    distance_y = start_center[1]-end_center[1] # get y distance
    velocity_x = (distance_x/(acc_x)) # get x velocity
    velocity_y = (distance_y/(acc_y)) # get y velocity
    rotated_start_core_rec = rotated_start_core.get_rect(center = (start_center[0]-velocity_x, start_center[1]-velocity_y))# apply velocity
    start_center = rotated_start_core_rec.center # get new start point
    
    #----- rendering
    screen.blit(start_screen_bg, start_screen_bg_rec)   # background
    drawbloom(20, 80, 10, (start_center), (25,25,25))  # draw bloom
    screen.blit(rotated_start_core, rotated_start_core_rec) # draw core
    render_game_title() # draw game title



    if title_delay:
        total_time += 1 # time + 1
    pygame.display.flip()   # update frame
    fps_clock.tick(fps)
