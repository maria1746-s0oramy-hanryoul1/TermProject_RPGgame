"""Character moving level 3 _HR (10/11)"""

import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 3")
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("TermProject_RPGgame\image/back3.png")
    img_chara = [
 
        pygame.image.load("TermProject_RPGgame\image/mychr6.png"),
        pygame.image.load("TermProject_RPGgame\image/mychr7.png")
    ]
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))

        x = tmr%160
        for i in range(1):
            screen.blit(img_bg, [i*60-x, -130])
        screen.blit(img_chara[tmr%2], [124, 235])
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()