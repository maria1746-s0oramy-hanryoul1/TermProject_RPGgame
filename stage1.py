# stage 1
from header import *
import pygame

pygame.init() # pygame 모듈 초기화
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전")  # 윈도우 타이틀 설정
clock = pygame.time.Clock() # clock 객체 초기화 

# 폰트 설정
font = pygame.font.SysFont('comicsans', 30, True) 

# 사운드 로딩
bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')
music = pygame.mixer.music.load('sound/backsound.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2)

# 이미지 로딩
bg = pygame.image.load("image/back1.png")
char = pygame.image.load('image/br1.png')
char_life = pygame.image.load('image/heart.png') 

def stage1() :
    global man
    ninja1_1 = Monster1_1(100, 385, 64, 64, 700) #run
    ninja1_2 = Monster1_2(300, 410, 64, 64, 700) #attck
    ninja1_3 = Monster1_2(700, 410, 64, 64, 700) #attck
    ninja1_4 = Monster1_3(400, 380, 64, 64, 700) #jump
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(30)

        # ninja1_1 
        if ninja1_1.visible == True:   
            if ninja1_1.mon_health > 0 :
                if man.hitbox[1] < ninja1_1.hitbox[1] + ninja1_1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_1.hitbox[1] :
                    if man.hitbox[0] + man.hitbox[2] > ninja1_1.hitbox[0] and man.hitbox[0] < ninja1_1.hitbox[0] + ninja1_1.hitbox[2]:
                        man.hit()
                        
                        

        if ninja1_1.mon_health <= 0 : 
            ninja1_1.visible = False
        
        
        for bullet in bullets:
            if ninja1_1.mon_health > 0 :
                if bullet.y - bullet.radius < ninja1_1.hitbox[1] + ninja1_1.hitbox[3] and bullet.y + bullet.radius > ninja1_1.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_1.hitbox[0] and bullet.x - bullet.radius < ninja1_1.hitbox[0] + ninja1_1.hitbox[2]:
                        hitSound.play()
                        ninja1_1.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja1_2
        if ninja1_2.visible == True:
            if ninja1_2.mon_health > 0 :
                if man.hitbox[1] < ninja1_2.hitbox[1] + ninja1_2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_2.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja1_2.hitbox[0] and man.hitbox[0] < ninja1_2.hitbox[0] + ninja1_2.hitbox[2]:
                        man.hit()

        if ninja1_2.mon_health <= 0 : 
            ninja1_2.visible = False
            

        for bullet in bullets:
            if ninja1_2.mon_health > 0 :
                if bullet.y - bullet.radius < ninja1_2.hitbox[1] + ninja1_2.hitbox[3] and bullet.y + bullet.radius > ninja1_2.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_2.hitbox[0] and bullet.x - bullet.radius < ninja1_2.hitbox[0] + ninja1_2.hitbox[2]:
                        hitSound.play()
                        ninja1_2.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja1_3
        if ninja1_3.visible == True:
            if ninja1_3.mon_health > 0 :
                if man.hitbox[1] < ninja1_3.hitbox[1] + ninja1_3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_3.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja1_3.hitbox[0] and man.hitbox[0] < ninja1_3.hitbox[0] + ninja1_3.hitbox[2]:
                        man.hit()

        if ninja1_3.mon_health <= 0 : 
            ninja1_3.visible = False
                

        for bullet in bullets:
            if ninja1_3.mon_health > 0 :
                if bullet.y - bullet.radius < ninja1_3.hitbox[1] + ninja1_3.hitbox[3] and bullet.y + bullet.radius > ninja1_3.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_3.hitbox[0] and bullet.x - bullet.radius < ninja1_3.hitbox[0] + ninja1_3.hitbox[2]:
                        hitSound.play()
                        ninja1_3.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja1_4
        if ninja1_4.visible == True:
            if ninja1_4.mon_health > 0 :
                if man.hitbox[1] < ninja1_4.hitbox[1] + ninja1_4.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_4.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja1_4.hitbox[0] and man.hitbox[0] < ninja1_4.hitbox[0] + ninja1_4.hitbox[2]:
                        man.hit()   
                                                 

        if ninja1_4.mon_health <= 0 :
            ninja1_4.visible = False


        for bullet in bullets:
            if ninja1_4.mon_health > 0 :
                if bullet.y - bullet.radius < ninja1_4.hitbox[1] + ninja1_4.hitbox[3] and bullet.y + bullet.radius > ninja1_4.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_4.hitbox[0] and bullet.x - bullet.radius < ninja1_4.hitbox[0] + ninja1_4.hitbox[2]:
                        hitSound.play()
                        ninja1_4.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1
                
            if len(bullets) < 5:
                bullets.append(Attack(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

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
            
        if not(man.isJump): # 점프 아닐때 
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0
        else: # 점프 중일 때 
            if man.jumpCount >= -10:
                man.neg = 1
                if man.jumpCount < 0:
                    man.neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * man.neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10  
                
        screen.blit(bg, (0,0))
        screen.blit(char_life, (30, 20)) 
        life = font.render('X ' + str(man.health), 1, (0,0,0))
        screen.blit(life, (65, 30))
        text = font.render('Stage: 1/3', 1, (0,0,0))
        screen.blit(text, (620, 20))
        man.draw(screen)
        ninja1_1.draw(screen)
        ninja1_2.draw(screen)
        ninja1_3.draw(screen)
        ninja1_4.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)
        
        pygame.display.update()

        if man.health == 0 :
            return man.health

        if (ninja1_1.mon_health <= 0) and (ninja1_2.mon_health <= 0) and (ninja1_3.mon_health <= 0) and (ninja1_4.mon_health <= 0) :
            return man.health   