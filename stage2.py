# satge 2
from header import *
import pygame

clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 30, True)

bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')
music = pygame.mixer.music.load('sound/backsound.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2) 

bg = pygame.image.load("image/back2.png")
char = pygame.image.load('image/br1.png')
char_life = pygame.image.load('image/heart.png') 

def stage2() :
    global man
    man.x = 50
    ninja2_1 = Monster2_1(100, 390, 64, 64, 700) #run
    ninja2_2 = Monster2_2(300, 410, 64, 64, 700) #attack
    ninja2_3 = Monster2_3(600, 250, 64, 64, 700) #glide
    ninja2_4 = Monster2_4(200, 250, 64, 64, 700) #glide
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(33)

        # ninja2_1 
        if ninja2_1.visible == True:
            if ninja2_1.mon_health > 0 :
                if man.hitbox[1] < ninja2_1.hitbox[1] + ninja2_1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja2_1.hitbox[1] :
                    if man.hitbox[0] + man.hitbox[2] > ninja2_1.hitbox[0] and man.hitbox[0] < ninja2_1.hitbox[0] + ninja2_1.hitbox[2]:
                        man.hit()
                        
        if ninja2_1.mon_health <= 0 : 
            ninja2_1.visible = False
        
        
        for bullet in bullets:
            if ninja2_1.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_1.hitbox[1] + ninja2_1.hitbox[3] and bullet.y + bullet.radius > ninja2_1.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_1.hitbox[0] and bullet.x - bullet.radius < ninja2_1.hitbox[0] + ninja2_1.hitbox[2]:
                        hitSound.play()
                        ninja2_1.hit()
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

        if ninja2_2.mon_health <= 0 : 
            ninja2_2.visible = False


        for bullet in bullets:
            if ninja2_2.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_2.hitbox[1] + ninja2_2.hitbox[3] and bullet.y + bullet.radius > ninja2_2.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_2.hitbox[0] and bullet.x - bullet.radius < ninja2_2.hitbox[0] + ninja2_2.hitbox[2]:
                        hitSound.play()
                        ninja2_2.hit()
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

        if ninja2_3.mon_health <= 0 : 
            ninja2_3.visible = False
                

        for bullet in bullets:
            if ninja2_3.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_3.hitbox[1] + ninja2_3.hitbox[3] and bullet.y + bullet.radius > ninja2_3.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_3.hitbox[0] and bullet.x - bullet.radius < ninja2_3.hitbox[0] + ninja2_3.hitbox[2]:
                        hitSound.play()
                        ninja2_3.hit()
                        bullets.pop(bullets.index(bullet))

            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        # ninja2_4
        if ninja2_4.visible == True:
            if ninja2_4.mon_health > 0 :
                if man.hitbox[1] < ninja2_4.hitbox[1] + ninja2_4.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja2_4.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja2_4.hitbox[0] and man.hitbox[0] < ninja2_4.hitbox[0] + ninja2_4.hitbox[2]:
                        man.hit()
                    

        if ninja2_4.mon_health <= 0 : 
            ninja2_4.visible = False
                

        for bullet in bullets:
            if ninja2_4.mon_health > 0 :
                if bullet.y - bullet.radius < ninja2_4.hitbox[1] + ninja2_4.hitbox[3] and bullet.y + bullet.radius > ninja2_4.hitbox[1]:
                    if bullet.x + bullet.radius > ninja2_4.hitbox[0] and bullet.x - bullet.radius < ninja2_4.hitbox[0] + ninja2_4.hitbox[2]:
                        hitSound.play()
                        ninja2_4.hit()
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
        text = font.render('Stage: 2/3', 1, (0,0,0))
        screen.blit(text, (620, 20))
        man.draw(screen)
        ninja2_1.draw(screen)
        ninja2_2.draw(screen)
        ninja2_3.draw(screen)
        ninja2_4.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
    
        pygame.display.update()

        if man.health == 0 :
            return man.health

        if (ninja2_1.mon_health <= 0) and (ninja2_2.mon_health <= 0) and (ninja2_3.mon_health <= 0) and (ninja2_4.mon_health <= 0) :
            return man.health