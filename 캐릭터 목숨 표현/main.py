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
    title_font = pygame.font.SysFont('bahnschrift', 44)
    menu_font = pygame.font.SysFont('bahnschrift', 30)  
    while True:
        screen.blit(background, (0, 0))  
        # move Label To screen
        title_label = title_font.render('Welcome', True, (0, 0, 0))
        title2_label = title_font.render('to', True, (0, 0, 0))
        title3_label = title_font.render('\'Rescue Manekineko\'', True, (0, 0, 0))
        start_label = menu_font.render('Click To Start', True, (0, 0, 0), text_background_color)  
        way_label = menu_font.render('How to Play', True, (0, 0, 0), text_background_color)
        senario_label = menu_font.render('Watch Scenario', True, (0, 0, 0), text_background_color)

        screen.blit(title_label, (135, 25))
        screen.blit(title2_label, (200, 85))
        screen.blit(title3_label, (20, 140))
        screen.blit(start_label, (10, 290))
        screen.blit(way_label,(10,340))
        screen.blit(senario_label,(10, 390))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                main_loop()
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RETURN: 
                    # 게임 방법 설명 화면
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RETURN: 
                    # 시나리오 설명 장면 
                    
        # running = False  # After main_loop (player loses), the game quits

# player's death
def death_screen():  
    pygame.mixer.music.load('sound/death_theme.mp3')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.2)

    death_font = pygame.font.SysFont('bahnschrift', 100)
    death_option_font = pygame.font.SysFont('bahnschrift', 40)
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
        screen.blit(death_label, (30, 40))
        screen.blit(death_option, (50, 165))
        #screen.blit(score_label, (225, 75))
        pygame.display.update()
      
  
# mission clear
def success_screen():  
    pygame.mixer.music.load('sound/gameclear_2.wav')  
    pygame.mixer.music.play(-1) 
    pygame.mixer.music.set_volume(.2)

    background = pygame.image.load('real_image/mission_clear.png')

    clear_font = pygame.font.SysFont('bahnschrift', 50)
    clear_label = clear_font.render('You got Makekineko!', True, (0, 0, 0))

    # Success screen Loop
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
        screen.blit(clear_label, (100, 50))
        pygame.display.update()
      

def main_loop() :   
    global health
    health = stage1()    
    if health == 0 : death_screen()        
    health = stage2()              
    if health == 0 : death_screen()
    health = stage3()
    if health == 0 : death_screen()
    if health > 0 : success_screen()
        # print("MISSION COMPLETE")   # 임시방편 / mission complete도 death와 start 처럼 함수로  만들어야 함 
        # print("left health is ", health)
        # sys.exit()    

start_menu() 
