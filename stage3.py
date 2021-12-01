# stage 3
from header import *
import pygame

clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 30, True)

bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')
music = pygame.mixer.music.load('sound/backsound.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2) 

bg = pygame.image.load("image/back3.png")
char = pygame.image.load('image/bl1.png')
char_life = pygame.image.load('image/heart.png')  

def stage3() : 
    global man
    man.x = 50
    ninja3_1 = Monster3_1(400, 340, 64, 64, 700) # stage 1,2처럼 뭔지 써주세용
    ninja3_2 = Monster3_2(200, 390, 64, 64, 700) #
    ninja3_3 = Monster3_2(550, 390, 64, 64, 700) #
    ninja3_4 = Monster3_2(700, 390, 64, 64, 700) #
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(37)

        #ninja3_1
        if ninja3_1.visible == True:
            if man.hitbox[1] < ninja3_1.hitbox[1] + ninja3_1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja3_1.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja3_1.hitbox[0] and man.hitbox[0] < ninja3_1.hitbox[0] + ninja3_1.hitbox[2]:
                    man.hit()
                    
        if ninja3_1.mon_health <= 0 : 
            ninja3_1.visible = False 

        for bullet in bullets:
            if ninja3_1.mon_health > 0 :
                if bullet.y - bullet.radius < ninja3_1.hitbox[1] + ninja3_1.hitbox[3] and bullet.y + bullet.radius > ninja3_1.hitbox[1]:
                    if bullet.x + bullet.radius > ninja3_1.hitbox[0] and bullet.x - bullet.radius < ninja3_1.hitbox[0] + ninja3_1.hitbox[2]:
                        hitSound.play()
                        ninja3_1.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        #ninja3_2
        if ninja3_2.visible == True:
            if man.hitbox[1] < ninja3_2.hitbox[1] + ninja3_2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja3_2.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja3_2.hitbox[0] and man.hitbox[0] < ninja3_2.hitbox[0] + ninja3_2.hitbox[2]:
                    man.hit()
                    
        if ninja3_2.mon_health <= 0 : 
            ninja3_2.visible = False 

        for bullet in bullets:
            if ninja3_2.mon_health > 0 :
                if bullet.y - bullet.radius < ninja3_2.hitbox[1] + ninja3_2.hitbox[3] and bullet.y + bullet.radius > ninja3_2.hitbox[1]:
                    if bullet.x + bullet.radius > ninja3_2.hitbox[0] and bullet.x - bullet.radius < ninja3_2.hitbox[0] + ninja3_2.hitbox[2]:
                        hitSound.play()
                        ninja3_2.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        #ninja3_3
        if ninja3_3.visible == True:
            if man.hitbox[1] < ninja3_3.hitbox[1] + ninja3_3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja3_3.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja3_3.hitbox[0] and man.hitbox[0] < ninja3_3.hitbox[0] + ninja3_3.hitbox[2]:
                    man.hit()
                    
        if ninja3_3.mon_health <= 0 : 
            ninja3_3.visible = False 

        for bullet in bullets:
            if ninja3_3.mon_health > 0 :
                if bullet.y - bullet.radius < ninja3_3.hitbox[1] + ninja3_3.hitbox[3] and bullet.y + bullet.radius > ninja3_3.hitbox[1]:
                    if bullet.x + bullet.radius > ninja3_3.hitbox[0] and bullet.x - bullet.radius < ninja3_3.hitbox[0] + ninja3_3.hitbox[2]:
                        hitSound.play()
                        ninja3_3.hit()
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        #ninja3_4
        if ninja3_4.visible == True:
            if man.hitbox[1] < ninja3_4.hitbox[1] + ninja3_4.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja3_4.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja3_4.hitbox[0] and man.hitbox[0] < ninja3_4.hitbox[0] + ninja3_4.hitbox[2]:
                    man.hit()
                    
        if ninja3_4.mon_health <= 0 : 
            ninja3_4.visible = False 

        for bullet in bullets:
            if ninja3_4.mon_health > 0 :
                if bullet.y - bullet.radius < ninja3_4.hitbox[1] + ninja3_4.hitbox[3] and bullet.y + bullet.radius > ninja3_4.hitbox[1]:
                    if bullet.x + bullet.radius > ninja3_4.hitbox[0] and bullet.x - bullet.radius < ninja3_4.hitbox[0] + ninja3_4.hitbox[2]:
                        hitSound.play()
                        ninja3_4.hit()
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
                
            if len(bullets) < 5 :
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
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
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
                
        screen.blit(bg, (0,0))
        screen.blit(char_life, (30, 20)) 
        life = font.render('X ' + str(man.health), 1, (0,0,0))
        screen.blit(life, (65, 30))
        text = font.render('Stage: 3/3', 1, (0,0,0))
        screen.blit(text, (620, 20))
        man.draw(screen)
        ninja3_1.draw(screen)
        ninja3_2.draw(screen)
        ninja3_3.draw(screen)
        ninja3_4.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)
        
        pygame.display.update()

        if man.health == 0 :
            return man.health

        if (ninja3_1.mon_health <= 0) and (ninja3_2.mon_health <= 0) and (ninja3_3.mon_health <= 0) and (ninja3_4.mon_health <= 0) :
            return man.health