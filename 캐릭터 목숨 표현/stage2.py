# satge 2
from header import *
import pygame


pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 2")
clock = pygame.time.Clock()
bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')
music = pygame.mixer.music.load('sound/backsound4.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2) 

bg = pygame.image.load("real_image/back2.png")
char = pygame.image.load('real_image/br1.png')
char_life = pygame.image.load('real_image/heart.png') #캐릭터 목숨 

font = pygame.font.SysFont('comicsans', 30, True)


def stage2() :
    global man
    ninja2_1 = Monster2_1(100, 410, 64, 64, 700)
    ninja2_2 = Monster2_2(300, 410, 64, 64, 700)
    ninja2_3 = Monster2_3(600, 410, 64, 64, 700)
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(37)
        # clock 35 -> 37
        # ninja2_1 
        if ninja2_1.visible == True:
            if ninja2_1.mon_health > 0 :
                if man.hitbox[1] < ninja2_1.hitbox[1] + ninja2_1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja2_1.hitbox[1] :
                    if man.hitbox[0] + man.hitbox[2] > ninja2_1.hitbox[0] and man.hitbox[0] < ninja2_1.hitbox[0] + ninja2_1.hitbox[2]:
                        man.hit()
                        # score -= 5
                        # ninja2_1 = Monster2_1(600, 410, 64, 64, 700) #캐릭터와 충돌 시 돌아가는 위치
                        
        if ninja2_1.mon_health == 0 : 
            ninja2_1.visible = False
        
        
        for bullet in bullets:
            if ninja2_1.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_1.hitbox[1] + ninja2_1.hitbox[3] and bullet.y + bullet.radius > ninja2_1.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_1.hitbox[0] and bullet.x - bullet.radius < ninja2_1.hitbox[0] + ninja2_1.hitbox[2]:
                        hitSound.play()
                        ninja2_1.hit()
                        # score += 1
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja2_2
        if ninja2_2.visible == True:
            if ninja2_2.mon_health > 0 :
                if man.hitbox[1] < ninja2_2.hitbox[1] + ninja2_2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja2_2.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja2_2.hitbox[0] and man.hitbox[0] < ninja2_2.hitbox[0] + ninja2_2.hitbox[2]:
                        man.hit()
                        # score -= 5
                        # ninja2_2 = Monster2_2(600, 410, 64, 64, 700)

        if ninja2_2.mon_health == 0 : 
            ninja2_2.visible = False
            

        for bullet in bullets:
            if ninja2_2.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_2.hitbox[1] + ninja2_2.hitbox[3] and bullet.y + bullet.radius > ninja2_2.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_2.hitbox[0] and bullet.x - bullet.radius < ninja2_2.hitbox[0] + ninja2_2.hitbox[2]:
                        hitSound.play()
                        ninja2_2.hit()
                        # score += 1
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja2_3
        if ninja2_3.visible == True:
            if ninja2_3.mon_health > 0 :
                if man.hitbox[1] < ninja2_3.hitbox[1] + ninja2_3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja2_3.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja2_3.hitbox[0] and man.hitbox[0] < ninja2_3.hitbox[0] + ninja2_3.hitbox[2]:
                        man.hit()
                        # score -= 5
                        # ninja2_3 = Monster2_3(600, 410, 64, 64, 700)

        if ninja2_3.mon_health == 0 : 
            ninja2_3.visible = False
                

        for bullet in bullets:
            if ninja2_3.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_3.hitbox[1] + ninja2_3.hitbox[3] and bullet.y + bullet.radius > ninja2_3.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_3.hitbox[0] and bullet.x - bullet.radius < ninja2_3.hitbox[0] + ninja2_3.hitbox[2]:
                        hitSound.play()
                        ninja2_3.hit()
                        # score += 1
                        bullets.pop(bullets.index(bullet))

            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if shootLoop > 0:
            shootLoop += 1
            if shootLoop == 4:
                shootLoop = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        """
        for bullet in bullets:
            if bullet.y - bullet.radius < ninja_g.hitbox[1] + ninja_g.hitbox[3] and bullet.y + bullet.radius > ninja_g.hitbox[1]:
                if bullet.x + bullet.radius > ninja_g.hitbox[0] and bullet.x - bullet.radius < ninja_g.hitbox[0] + ninja_g.hitbox[2]:
                    hitSound.play()
                    ninja_g.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        """

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
                
        screen.blit(bg, (0,0))
        screen.blit(char_life, (30, 20)) 
        # text = font.render('Score: ' + str(score), 1, (0,0,0))
        # screen.blit(text, (620, 20))
        life = font.render('X ' + str(man.health), 1, (0,0,0))
        screen.blit(life, (65, 30))
        man.draw(screen)
        ninja2_1.draw(screen)
        ninja2_2.draw(screen)
        ninja2_3.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
    
        pygame.display.update()

        if man.health == 0 :
            return man.health

        if (ninja2_1.mon_health == 0) and (ninja2_2.mon_health == 0) and (ninja2_3.mon_health == 0) :
            return man.health
        """
        if man.health == 0 :
            return man.health, score

        if (ninja2_1.mon_health == 0) and (ninja2_2.mon_health == 0) and (ninja2_3.mon_health == 0) :
            return man.health, score
        """