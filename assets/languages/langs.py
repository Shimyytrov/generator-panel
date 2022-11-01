import json

settings = {}
with open('./assets/saves/settings.json', 'r') as settings_json:
    settings = json.load(settings_json)

class zhCN:
    # Quit confirm
    text_quit = ["退出"]
    text_quitMSG = ["您确定要退出吗？"]
    
    # Title1
    text_intro1 = ["希米特罗夫"]
    text_intro2 = ["出品"]

    # Language window
    text_lang = ["中文(中国简体)"]
    text_lang_select = ["选择你的语言"]
    text_lang_continue = ["按此继续"]

    # Start Screen
    text_play = ["按此开始"]
    text_title1 = ["希米特罗夫"]
    text_title2 = ["发电机控制台"]
    text_ini = ["设定"]

    # Settings
    text_return = ["返回"]
    text_graINI = ["图形设定"]
    text_langINI = ["语言"]
    text_soundINI = ["声音设定"]
    text_resetINI = ["重置设定"]

    text_gra_DynamicLight = ["动态照明"]
    text_gra_Bloom = ["高光效果"]
    text_gra_PlayerAnimation = ["玩家动画"]
    text_gra_Particles = ["粒子效果"]
    text_gra_CameraShake = ["画面抖动"]
    text_gra_EnvAnimation = ["环境动画"]

    text_sound_Sound = ["声音"]
    text_sound_Music = ["音乐"]

    text_reset = ["重置会把设定设回默认.", "确定要重置吗?"]
    text_reset_confirm = ["确定"]

    # Endings
    text_meltdown = ["熔毁"]
    text_meltdownDES = ["发电机温度超出了可承受的极限(4000°C)！整座 ", "设施发生了一场巨大的爆炸，并且摧毁了 ", "整个设施以及周边的环境。 ", "提示：记得检查冷冻液是否开启，以及是否有管道破裂。"]
    text_freezedown = ["冻毁"]
    text_freezedownDES = ["由于温度过低(-4000°C)，一个黑洞产生了，并 ", "摧毁了整个设施，灾害甚至蔓延到整个 ", "世界。 ", "“游戏结束，伙计，游戏结束！” ", "提示：记得随时检查两个发电机的温度，并在适当时机关闭或开启冷冻液。"]
    text_blackout = ["设施停电"]
    text_blackoutDES = ["由于发电机的能源用尽，没有能量继续泵动颜料， ", "设施无法再继续产生电力，游戏结束。 ", "提示：记得及时维修运输燃料的管道！"]

class zhTW:
    # Quit confirm
    text_quit = ["退出"]
    text_quitMSG = ["你確定要退出嗎？"]
    
    # Title1
    text_intro1 = ["希米特羅夫"]
    text_intro2 = ["出品"]
    
    # Language window
    text_lang = ["中文(台灣正體)"]
    text_lang_select = ["選擇你的語言"]
    text_lang_continue = ["按此繼續"]
    
    # Start Screen
    text_play = ["按此開始"]
    text_title1 = ["希米特羅夫"]
    text_title2 = ["發電機控制臺"]
    text_ini = ["設定"]
    text_resetINI = ["重設設定"]

    # Settings
    text_return = ["返回"]
    text_graINI = ["圖形設定"]
    text_langINI = ["語言"]
    text_soundINI = ["聲音設定"]

    text_gra_DynamicLight = ["動態照明"]
    text_gra_Bloom = ["高光效果"]
    text_gra_PlayerAnimation = ["玩家動畫"]
    text_gra_Particles = ["粒子效果"]
    text_gra_CameraShake = ["畫面抖動"]
    text_gra_EnvAnimation = ["環境動畫"]

    text_sound_Sound = ["聲音"]
    text_sound_Music = ["音樂"]

    text_reset = ["重設會把所有設定設回預設.", "你確定要重設嗎?"]
    text_reset_confirm = ["確定"]

    # Endings
    text_meltdown = ["熔毀"]
    text_meltdownDES = ["發電機溫度超出了可承受的極限(4000°C)！整座 ", "設施發生了一場巨大的爆炸，並且摧毀了 ", "整個設施以及周邊的環境。 ", "提示：記得檢查冷凍液是否開啟，以及是否有管道破裂。"]
    text_freezedown = ["凍毀"]
    text_freezedownDES = ["由於溫度過低(-4000°C)，一個黑洞產生了，並 ", "摧毀了整個設施，災害甚至蔓延到整個 ", "世界。 ", "“遊戲結束，夥計，遊戲結束！” ", "提示：記得隨時檢查兩個發電機的溫度，並在適當時機關閉或開啟冷凍液。"]
    text_blackout = ["設施停電"]
    text_blackoutDES = ["由於發電機的能源用盡，沒有能量繼續泵動顏料， ", "設施無法再繼續產生電力，遊戲結束。 ", "提示：記得及時維修運輸燃料的管道！"]

class EN:
    # Quit confirm
    text_quit = ["QUIT"]
    text_quitMSG = ["Are you sure?"]
    
    # Title1
    text_intro1 = ["PRODUCED BY"]
    text_intro2 = ["Shimyytrov Studio"]
    
    # Language window
    text_lang = ["English"]
    text_lang_select = ["Select Your Language"]
    text_lang_continue = ["Continue"]

    # Start Screen
    text_play = ["Press to Start"]
    text_title1 = ["Shimyytrov's"]
    text_title2 = ["Generator Panel"]
    text_ini = ["Settings"]
    text_resetINI = ["Reset Settings"]
    
    # Settings
    text_return = ["Return"]
    text_graINI = ["Graphics Setting"]
    text_langINI = ["Languages"]
    text_soundINI = ["Sound Settings"]

    text_gra_DynamicLight = ["Dynamic Light"]
    text_gra_Bloom = ["Bloom"]
    text_gra_PlayerAnimation = ["Player Animation"]
    text_gra_Particles = ["Particles"]
    text_gra_CameraShake = ["Camera Shake"]
    text_gra_EnvAnimation = ["Environment Animation"]

    text_sound_Sound = ["Sound"]
    text_sound_Music = ["Music"]

    text_reset = ["Reseting will makes your settings back to default.", "Are you sure you want to do that?"]
    text_reset_confirm = ["Confirmed"]

    # Endings
    text_meltdown = ["Meltdown"]
    text_meltdownDES = ["The generator temperature is beyond the acceptable limit(4000°C)!", "A huge explosion occurred in the whole facility. For the result,", "the facility and the surrounding have been destroyed.", "Hint: Remember to check if the coolant is activated and if there are no broken pipes."]
    text_freezedown = ["Freezedown"]
    text_freezedownDES = ["Due to the low temperature(-4000°C), a black hole was created,", "and destroyed the whole facility. The disaster even spread to the whole world.", "“Game over, man, game over!” ", "Hint: Remember to check the temperature of both generators at all times,", "and turn off or turn on the coolant when appropriate."]
    text_blackout = ["Facility-wide Blackout"]
    text_blackoutDES = ["With the generator running out of energy, there is no energy to continue pumping the paint,", "Game over.", "Hint: Remember to repair the pipes that transport fuel!"]

class DE:
    # Quit confirm
    text_quit = ["Verlassen"]
    text_quitMSG = ["Bist du dir sicher?"]
    
    # Title1
    text_intro1 = ["PRODUZIERT VON"]
    text_intro2 = ["Schmitrov Studio"]
    
    # Language window
    text_lang = ["Deutsch"]
    text_lang_select = ["Wähle deine Sprache"]
    text_lang_continue = ["Fortsetzen"]

    # Start Screen
    text_play = ["Zum Starten Drücken"]
    text_title1 = ["Schmitrov"]
    text_title2 = ["Generator-Bedienfeld"]
    text_ini = ["Einstellungen"]
    text_resetINI = ["Reset Settings(need translation)"]

    # Settings
    text_return = ["Zurückkehren"]
    text_graINI = ["Grafikeinstellungen"]
    text_langINI = ["Sprachen"]
    text_soundINI = ["Toneinstellungen"]

    text_gra_DynamicLight = ["Dynamisches Licht"]
    text_gra_Bloom = ["Bloom"]
    text_gra_PlayerAnimation = ["Spieleranimation"]
    text_gra_Particles = ["Partikel"]
    text_gra_CameraShake = ["Kamerawackeln"]
    text_gra_EnvAnimation = ["Umgebungsanimation"]

    text_sound_Sound = ["Klang"]
    text_sound_Music = ["Musik"]

    text_reset = ["Durch das Zurücksetzen werden Ihre Einstellungen", "auf die Standardeinstellungen zurückgesetzt.", "Sind Sie sicher, dass Sie das tun möchten?"]
    text_reset_confirm = ["Bestätigt"]
    
    # Endings
    text_meltdown = ["Kernschmelze"]
    text_meltdownDES = ["Die Generatortemperatur liegt außerhalb der zulässigen Grenze(4000 °C)!", "In der gesamten Anlage ereignete sich eine riesige Explosion.", "Dafür wurden die Anlage und die Umgebung zerstört.", "Hinweis: Denken Sie daran, zu prüfen, ob das Kühlmittel", "aktiviert ist und ob es keine gebrochenen Rohre gibt."]
    text_freezedown = ["Kerneinfriere(Kern Einfrieren)"]
    text_freezedownDES = ["Aufgrund der niedrigen Temperatur(-4000 ° C) wurde ein Schwarzes Loch geschaffen,", "Es zerstörte die ganze Anlage. Die Katastrophe breitete sich sogar auf", "der ganzen Welt aus.", "“Game over, mann, game over!” ", "Hinweis: Denken Sie daran, die Temperatur beider Generatoren jederzeit", "zu überprüfen und gegebenenfalls das Kühlmittel aus- oder einzuschalten."]
    text_blackout = ["Anlagenweiter Blackout"]
    text_blackoutDES = ["Wenn der Generator keine Energie mehr hat, gibt es keine Energie, um die Farbe weiter zu pumpen,", "Spiel vorbei.", "Hinweis: Denken Sie daran, die Rohre zu reparieren, die Kraftstoff transportieren!"]

class BURGER:
    # Quit confirm
    text_quit = ["BURGER"]
    text_quitMSG = ["What r u doin???"]
    
    # Title1
    text_intro1 = ["Press Space to"]
    text_intro2 = ["Get a Fucking Burger"]
    
    # Language window
    text_lang = ["Burgerishkiy"]
    text_lang_select = ["Select Your Burger"]
    text_lang_continue = ["Burger?"]

    # Start Screen
    text_play = ["Press to BURGER"]
    text_title1 = ["BURGER's"]
    text_title2 = ["Fucking Raw Steak"]
    text_ini = ["HAMBURGER"]

    # Settings
    text_return = ["Press to get FREE ROBUX"]
    text_graINI = ["Big Mac - 5$"]
    text_langINI = ["Select Your Burger"]
    text_soundINI = ["MOYAI SOUND EFFECT"]
    text_resetINI = ['"oh wait how it ignore a file when commit"']

    text_gra_DynamicLight = ["Dynamic TOMATO"]
    text_gra_Bloom = ["Kaboom?"]
    text_gra_PlayerAnimation = ["Yes, Kaboom."]
    text_gra_Particles = ["Bread"]
    text_gra_CameraShake = ["Raw Steak"]
    text_gra_EnvAnimation = ["Uoi str hsu"]

    text_sound_Sound = ["PAY ME"]
    text_sound_Music = ["TRACKS N' NUTZ"]

    text_reset = ['"o so you mean we playtesting will affect the saving"', '"nah easy la, you reset the file lor"']
    text_reset_confirm = ['"well"']
    
    # Endings
    text_meltdown = ["Burgermelt"]
    text_meltdownDES = ["burger walk running burger", "hamham burburger walkk run", "Burger.", "Walking: burgerger run."]
    text_freezedown = ["Burgerfreeze"]
    text_freezedownDES = ["Burger,", "HAMBURGER", "Tomato.", "“BO'OH'O'WA'ER.” ", "Burger: Run Walk burtomager, run run ger ger hamhamgerbur."]
    text_blackout = ["Burger-wide Walking"]
    text_blackoutDES = ["Burgergertam ran out of burgers, the whole tomato and burger just ran away.", "Burger Over.", "Burger: Burh."]

class SCH:
    # Quit confirm
    text_quit = ["Quitën"]
    text_quitMSG = ["Sind du siken?"]
    
    # Title1
    text_intro1 = ["Schmitŕov-Studio"]
    text_intro2 = ["PRODUZENTVA"]
    
    # Language window
    text_lang = ["Schmitŕov Schtora"]
    text_lang_select = ["Duzhe Schtora Pikiten"]
    text_lang_continue = ["Kontinen"]
    
    # Start Screen
    text_play = ["Zum Biginten Prasken"]
    text_title1 = ["Schmitŕov"]
    text_title2 = ["Truktonekapanëła"]
    text_ini = ["Einśtill"]

    # Settings
    text_return = ["Khaten"]
    text_graINI = ["Graphikeinśtilli"]
    text_langINI = ["Schtora"]
    text_soundINI = ["Klangeinśtilli"]
    text_resetINI = ["Das Einśtilli risen"]

    text_gra_DynamicLight = ["Deinomiknaya Liçhtiki"]
    text_gra_Bloom = ["Blühmi"]
    text_gra_PlayerAnimation = ["Śpiela-Animationi"]
    text_gra_Particles = ["Partikli"]
    text_gra_CameraShake = ["Kamerashäki"]
    text_gra_EnvAnimation = ["Enveironmentanimationi"]

    text_sound_Sound = ["Klangki"]
    text_sound_Music = ["Musiki"]

    text_reset = ["Risën weŕden duzh Einśtilli maçhenka, zum das Rośteik khaten.", "Sind du siken du deçh maçhen wollen?"]
    text_reset_confirm = ["Konfirmentva"]
    
    # Endings
    text_meltdown = ["Köśteinmelten"]
    text_meltdownDES = ["Das Temperätuŕ deŕ Truktoneka haat das akzept'betën Limit übeŕłyben!", "Din vitz Tukleinsion haat in das höłe Induska geschetentva. Füŕ das Ençhbik,", "das Induska und das Embratka haat krorruptentva.", "Hints: Zum checken jerneśten, sind das Akłafrieśkonpleitionsystemi aktivätentva, o'", "sind das Akłafrieśpeipy trorraptentva."]
    text_freezedown = ["Köśteinfriezen"]
    text_freezedownDES = ["Das öbuni Temperätuŕ bikönsen, din Bronkloçh haat schaffentvo,", "und haat das höłe Induska krorruptentvo. Das Disäska haat even das höłe Welt veŕbŕeitentvo.", "“Game over, mann, game over!”", "Hints: Zum alle Teim jerneśten, das Temperätuŕ deŕ beide Truktoneki checken,", "und das Akłafrieśkonpleitionsystemi aktiväten o' die'aktiväten wenn appropriät."]
    text_blackout = ["Höłeinduskaelektriksityinterruption"]
    text_blackoutDES = ["Bruh.", "Bruh Over.", "Bruhman: a yo wtf."]

class BRUH:
    # Quit confirm
    text_quit = ["BRUH"]
    text_quitMSG = ["Ayo WTF?"]
    
    # Title1
    text_intro1 = ["Press ALT+F4"]
    text_intro2 = ["To Get Free Robux"]
    
    # Language window
    text_lang = ["WTF is this"]
    text_lang_select = ["SAMSUNG"]
    text_lang_continue = ["Free ROBUX"]
    
    # Start Screen
    text_play = ["ÒwÓ!"]
    text_title1 = ["You've been"]
    text_title2 = ["RICKROLL'D"]
    text_ini = ["SOKOŁY"]

    # Settings
    text_return = ["RICKROLL'D"]
    text_graINI = ["KraSOKOŁY"]
    text_langINI = ["RICKROLLSOKOŁY"]
    text_soundINI = ["AyoSOKOŁY"]
    text_resetINI = ["RĘŚEŢ DĄ SOKOŁY"]

    text_gra_DynamicLight = ["DynamicRICKROLL"]
    text_gra_Bloom = ["Explosion meme"]
    text_gra_PlayerAnimation = ["/ban Schmitrovland"]
    text_gra_Particles = ["Robux"]
    text_gra_CameraShake = ["EARTHQUAKE!!!"]
    text_gra_EnvAnimation = ["/give Schmitrovland tnt 64"]

    text_sound_Sound = ["Ayo wtf?"]
    text_sound_Music = ["Earrape"]

    text_reset = ["Ayo what the fuck are you doing??", "DON'T YOU DARE DO IT!!!"]
    text_reset_confirm = ["Press me"]
    
    # Endings
    text_meltdown = ["Bruht"]
    text_meltdownDES = ["Walking: run bruhman run", "bruh do it just ruuuuuunnnnnnnnnn", "Bruhman.", "Walking: bruhman run."]
    text_freezedown = ["freEZe"]
    text_freezedownDES = ["Step-bother help im stuck in the blackhole"]
    text_blackout = ["Bruh-wide Putin Walking"]
    text_blackoutDES = ["Bruh.", "Bruh Over.", "Bruhman: a yo wtf."]


for k,v in {zhTW:"zhTW", zhCN:"zhCN", EN:"EN", DE:"DE", BURGER:"BURGER", BRUH:"BRUH", SCH:"SCH"}.items():
    if v == settings["Lang"]:
        selected_language = k
