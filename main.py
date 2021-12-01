# header & stage 1,2,3 불러오기
from pygame.constants import K_RIGHT
from header import *
from stage1 import *
from stage2 import *
from stage3 import *
   
health = 0

# 오프닝 
def start_menu():
    text_background_color = (255, 255, 255)
    title_font = pygame.font.SysFont('bahnschrift', 44)
    menu_font = pygame.font.SysFont('bahnschrift', 28)  
    while True:
        screen.blit(background, (0, 0))  
        title_label = title_font.render('Welcome to', True, (0, 0, 0))
        title2_label = title_font.render('\'Rescue Manekineko\'', True, (0, 0, 0))
        start_label = menu_font.render('Enter to \'Start\'', True, (0, 0, 0), text_background_color)  
        way_label = menu_font.render('Shift to \'How to Play\'', True, (0, 0, 0), text_background_color)
        
        screen.blit(title_label, (110, 40))
        screen.blit(title2_label, (20, 110))
        screen.blit(start_label, (10, 330))
        screen.blit(way_label,(10,380))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scenario1()
                    # main_loop()
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    game_rule()

# 게임 방법
def game_rule():
    rule_background = pygame.image.load('image/rule.JPG')
    next_font = pygame.font.SysFont('bahnschrift', 20)
    next_label = next_font.render('Enter to Play...', True, (0, 0, 0))
    while True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    scenario1()

        screen.blit(rule_background, (0, 0))
        screen.blit(next_label, (15, 430))
        pygame.display.update()

# 시나리오
def scenario1():
    scenario1 = pygame.image.load('image/scenario1.png')
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            screen.blit(scenario1, (0,0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scenario2()

def scenario2():
    scenario2 = pygame.image.load('image/scenario2.png')
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            screen.blit(scenario2, (0,0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scenairo3()

def scenairo3():
    scenario3 = pygame.image.load('image/scenario3.png')
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            screen.blit(scenario3, (0,0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scenario4()

def scenario4():
    scenario4 = pygame.image.load('image/scenario4.png')
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            screen.blit(scenario4, (0,0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scenario5()

def scenario5():
    scenario5 = pygame.image.load('image/scenario5.png')
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            screen.blit(scenario5, (0,0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_loop()
        
                   
# 스테이지 연결 이미지 
def level1():
    stage1 = pygame.image.load('image/stage1.png')
    screen.blit(stage1, (0,0))
    pygame.display.update()
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 201
                pygame.quit()
def level2():
    stage2 = pygame.image.load('image/stage2.png')
    screen.blit(stage2, (0,0))
    pygame.display.update()
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 201
                pygame.quit()
def level3():
    stage3 = pygame.image.load('image/stage3.png')
    screen.blit(stage3, (0,0))
    pygame.display.update()
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 201
                pygame.quit()

# 게임 엔딩 - 실패
def death_screen():  
    pygame.mixer.music.load('sound/death.mp3')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.4)

    death_font = pygame.font.SysFont('bahnschrift', 100)
    death_option_font = pygame.font.SysFont('bahnschrift', 30)
    death_label = death_font.render('You Died', True, (255, 0, 0))
    death_option = death_option_font.render('ENTER To Quit', True, (0, 0, 0))
    death_option2 = death_option_font.render('SPACE To Retry', True, (0, 0, 0))

    # 게임 실패 스크린 loop
    while True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sound/backsound.wav')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(.2)
                    man.health = 3
                    man.x = 50
                    main_loop()

        screen.blit(background, (0, 0))
        screen.blit(death_label, (30, 20))
        screen.blit(death_option, (130, 145))
        screen.blit(death_option2, (120, 190))
        pygame.display.update()
      
# 게임 엔딩 - 성공
def success_screen():  
    pygame.mixer.music.load('sound/gameclear.wav')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.2)

    success_background = pygame.image.load('image/mission_clear.png')

    clear_font = pygame.font.SysFont('bahnschrift', 50)
    clear_label = clear_font.render('You got Manekineko!', True, (0, 0, 0))
    quit_font = pygame.font.SysFont('bahnschrift', 24)
    quit_label = quit_font.render('Enter to Quit', True, (0, 0, 0))

    # 게임 성공 스크린 loop
    while True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit()

        screen.blit(success_background, (0, 0))
        screen.blit(clear_label, (170, 50))
        screen.blit(quit_label, (330, 460))
        pygame.display.update()

# main loop
def main_loop() :   
    global health
    level1()
    health = stage1()    
    if health <= 0 : death_screen()  
    level2()      
    health = stage2()              
    if health <= 0 : death_screen()
    level3()
    health = stage3()
    if health <= 0 : death_screen()
    if health > 0 : success_screen()  

start_menu()