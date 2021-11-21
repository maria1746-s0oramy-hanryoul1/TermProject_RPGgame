# call header & stage 1,2,3
from header import *
from stage1 import *
from stage2 import *
from stage3 import *
   
health = 0

# how to play
def game_rule():
    rule_background = pygame.image.load('image/rule.JPG')
    next_font = pygame.font.SysFont('bahnschrift', 25)
    next_label = next_font.render('Enter to Play...', True, (0, 0, 0))
    while True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_loop()

        screen.blit(rule_background, (0, 0))
        screen.blit(next_label, (15, 430))
        pygame.display.update()

# start game 
def start_menu():
    # running = True
    text_background_color = (255, 255, 255)
    title_font = pygame.font.SysFont('bahnschrift', 44)
    menu_font = pygame.font.SysFont('bahnschrift', 28)  
    while True:
        screen.blit(background, (0, 0))  
        # move Label To screen
        title_label = title_font.render('Welcome', True, (0, 0, 0))
        title2_label = title_font.render('to', True, (0, 0, 0))
        title3_label = title_font.render('\'Rescue Manekineko\'', True, (0, 0, 0))
        start_label = menu_font.render('Enter To Start', True, (0, 0, 0), text_background_color)  
        way_label = menu_font.render('Shift to see \'How to Play\'', True, (0, 0, 0), text_background_color)
        #senario_label = menu_font.render('Watch Scenario', True, (0, 0, 0), text_background_color)

        screen.blit(title_label, (135, 25))
        screen.blit(title2_label, (200, 85))
        screen.blit(title3_label, (20, 140))
        screen.blit(start_label, (10, 330))
        screen.blit(way_label,(10,380))
        #screen.blit(senario_label,(10, 390))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            #elif event.type == pygame.MOUSEBUTTONDOWN :
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_loop()
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    game_rule()
                #if event.key == pygame.K_RETURN: 
                    # 시나리오 설명 장면 
           
        # running = False  # After main_loop (player loses), the game quits

# player's death
def death_screen():  
    pygame.mixer.music.load('sound/death_theme.mp3')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.4)
    # death_screen volume 2 -> 4

    death_font = pygame.font.SysFont('bahnschrift', 100)
    death_option_font = pygame.font.SysFont('bahnschrift', 30)
    death_label = death_font.render('You Died', True, (255, 0, 0))
    death_option = death_option_font.render('ENTER To Quit', True, (0, 0, 0))

    # Death screen Loop
    #running = True
    while True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit()

        screen.blit(background, (0, 0))
        screen.blit(death_label, (30, 40))
        screen.blit(death_option, (130, 165))
        #screen.blit(score_label, (225, 75))
        pygame.display.update()
      
  
# mission clear
def success_screen():  
    pygame.mixer.music.load('sound/gameclear_2.wav')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.2)

    success_background = pygame.image.load('image/mission_clear.png')

    clear_font = pygame.font.SysFont('bahnschrift', 50)
    clear_label = clear_font.render('You got Manekineko!', True, (0, 0, 0))

    # Success screen Loop
    #running = True
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
        pygame.display.update()
      

def main_loop() :   
    global health
    health = stage1()    
    if health <= 0 : death_screen()        
    health = stage2()              
    if health <= 0 : death_screen()
    health = stage3()
    if health <= 0 : death_screen()
    
    if health > 0 : success_screen()  

start_menu() 
