# call header & stage 1,2,3
from header import *
from stage1 import *
from stage2 import *
from stage3 import *
   
health = 0
          
# start game 
def start_menu():
    # running = True
    text_background_color = (255, 255, 255)
    title_font = pygame.font.SysFont('bahnschrift', 45)
    menu_font = pygame.font.SysFont('bahnschrift', 35)  
    while True:
        screen.blit(background, (0, 0))  
        # move Label To screen
        title_label = title_font.render('< Welcome to \'Rescue Manekineko\' >', True, (0, 0, 0))
        start_label = menu_font.render('Press ENTER To Start', True, (0, 0, 0), text_background_color)  
        way_label = menu_font.render('How to Play', True, (0, 0, 0), text_background_color)
        senario_label = menu_font.render('Watch Scenario', True, (0, 0, 0), text_background_color)

        screen.blit(title_label, (50, 65))
        screen.blit(start_label, (230, 190))
        screen.blit(way_label,(300,250))
        screen.blit(senario_label,(270, 310))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    main_loop()
                    # running = False  # After main_loop (player loses), the game quits

# player's death
def death_screen():  
    pygame.mixer.music.load('sound/death_theme.mp3')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.2)

    death_font = pygame.font.SysFont('bahnschrift', 170)
    death_option_font = pygame.font.SysFont('bahnschrift', 50)
    death_label = death_font.render('You Died', True, (255, 0, 0))
    death_option = death_option_font.render('Press Space To Quit', True, (0, 0, 0))
    #score_label = death_option_font.render(f'Final Score: {player.score}', True, (0, 0, 0))

    # Death screen Loop
    #running = True
    while True:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sys.exit()

        screen.blit(background, (0, 0))
        screen.blit(death_label, (70, 50))
        screen.blit(death_option, (190, 200))
        #screen.blit(score_label, (225, 75))
        pygame.display.update()

def main_loop() :   
    global health
    health = stage1()    
    if health == 0 : death_screen()        
    health = stage2()              
    if health == 0 : death_screen()
    health = stage3()
    if health == 0 : death_screen()
    if health > 0 : 
        print("MISSION COMPLETE")   # 임시방편 / mission complete도 death와 start 처럼 함수로  만들어야 함 
        print("left health is ", health)
        sys.exit()    

start_menu() 
