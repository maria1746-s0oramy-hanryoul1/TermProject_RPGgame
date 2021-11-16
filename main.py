# call header & stage 1,2,3
from header import *
from stage1 import *
from stage2 import *
from stage3 import *

score = 0
health = 0

# start game 
def start_menu():
    # running = True
    title_font = pygame.font.SysFont('Maplestory Bold.ttf', 60)  
    while True:
        screen.blit(background, (0, 0))  
        # move Label To screen
        menu_label = title_font.render('<Press Enter To Begin>', True, (0, 0, 0))  
        screen.blit(menu_label, (170, 90))
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

    death_font = pygame.font.SysFont('Maplestory Bold.ttf', 180)
    death_option_font = pygame.font.SysFont('Maplestory Bold.ttf', 65)
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
        screen.blit(death_label, (140, 50))
        screen.blit(death_option, (210, 200))
        #screen.blit(score_label, (225, 75))
        pygame.display.update()

def main_loop() :   
    global score     
    global health
    health, score = stage1(score)
    if health == 0 : death_screen()
    health, score = stage2(score)
    if health == 0 : death_screen()
    health, score = stage3(score)
    if health == 0 : death_screen()
    if health > 0 : 
        print("MISSION COMPLETE")   # 임시방편 / mission complete도 death와 start 처럼 함수로  만들어야 함 
    print(score)
    pygame.quit()

start_menu() 
