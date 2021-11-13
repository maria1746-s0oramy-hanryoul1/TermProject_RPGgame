import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 1")

walkRight = [pygame.image.load('real_image/br1.png'), pygame.image.load('real_image/br2.png'), pygame.image.load('real_image/br3.png'), pygame.image.load('real_image/br4.png'), pygame.image.load('real_image/br5.png'), pygame.image.load('real_image/br6.png'), pygame.image.load('real_image/br7.png'), pygame.image.load('real_image/br8.png'), pygame.image.load('real_image/br9.png')]
walkLeft = [pygame.image.load('real_image/bl1.png'), pygame.image.load('real_image/bl2.png'), pygame.image.load('real_image/bl3.png'), pygame.image.load('real_image/bl4.png'), pygame.image.load('real_image/bl5.png'), pygame.image.load('real_image/bl6.png'), pygame.image.load('real_image/bl7.png'), pygame.image.load('real_image/bl8.png'), pygame.image.load('real_image/bl9.png')]
background = pygame.image.load("real_image/back1.png")
char = pygame.image.load('real_image/br1.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')

music = pygame.mixer.music.load('sound/backsound.wav')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('comicsans', 30, True)


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.JumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        screen.blit(text, (400 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                


class attack(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)


class monster(object):
    walkRight = [pygame.image.load('real_image/NR.png'), pygame.image.load('real_image/NR.png'), pygame.image.load('real_image/NR1.png'), pygame.image.load('real_image/NR2.png'), pygame.image.load('real_image/NR3.png'), pygame.image.load('real_image/NR4.png'), pygame.image.load('real_image/NR5.png'), pygame.image.load('real_image/NR6.png'), pygame.image.load('real_image/NR7.png'), pygame.image.load('real_image/NR8.png'), pygame.image.load('real_image/NR9.png')]
    walkLeft = [pygame.image.load('real_image/NL.png'), pygame.image.load('real_image/NL.png'), pygame.image.load('real_image/NL1.png'), pygame.image.load('real_image/NL2.png'), pygame.image.load('real_image/NL3.png'), pygame.image.load('real_image/NL4.png'), pygame.image.load('real_image/NL5.png'), pygame.image.load('real_image/NL6.png'), pygame.image.load('real_image/NL7.png'), pygame.image.load('real_image/NL8.png'), pygame.image.load('real_image/NL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.gameover = False

    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


man = player(60, 410, 64, 64)
goblin = monster(100, 410, 64, 64, 700)
bullets = []
score = 0        

def redrawGamescreen():
    screen.blit(background, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    screen.blit(text, (620, 20))
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    
    pygame.display.update()

# Death screen
def death_screen(player):  # Pass in player object for access to final score

    # Death screen music start
    pygame.mixer.music.load('sound/death_theme.mp3')  # Load in death screen song
    pygame.mixer.music.play(-1)  # Start playing theme song
    pygame.mixer.music.set_volume(.2)

    # Fonts initialized
    death_font = pygame.font.SysFont('comicsans', 180)
    death_option_font = pygame.font.SysFont('comicsans', 65)
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
        screen.blit(death_label, (30, 50))
        screen.blit(death_option, (100, 200))
        #screen.blit(score_label, (225, 75))
        pygame.display.update()


# Start Menu Loop
def start_menu():
    pygame.mixer.music.play(-1)  
    pygame.mixer.music.set_volume(.2)
    # running = True
    title_font = pygame.font.SysFont('comicsans', 60)  # Create font object
    while True:
        screen.blit(background, (0, 0))  # move Background To screen
        menu_label = title_font.render('Press Enter To Begin', True, (0, 0, 0))  # Create Text Label
        screen.blit(menu_label, (105, 50))  # move Label To screen
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # If space is pressed, start game
                    main_loop()  
                    pygame.mixer.music.stop()
                    death_screen(player)
                    # running = False  # After main_loop (player loses), the game quits

# mainloop
def main_loop() :   
    global score 
    shootLoop = 0
    
    # run = True
    while True:
        clock.tick(80)

        if goblin.visible == True:      # 몬스터가 보이고 플레이어랑 맞았을 경우 점수 -5
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    man.hit()
                    score -= 5

        if score <= -10:
            death_screen(player)

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
            
        for bullet in bullets:      # 플레이어의 공격이 몬스터에 맞았을 경우 점수 +1
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # 키 입력 대기
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            bulletSound.play()
            if man.left:        # 총알 나가는 방향 조절
                facing = -1
            else:
                facing = 1
                
            if len(bullets) < 5:
                bullets.append(attack(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10


        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

        redrawGamescreen()



#게임 시작
start_menu()