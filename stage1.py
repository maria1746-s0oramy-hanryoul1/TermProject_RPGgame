from header import *
import pygame
pygame.init()

pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 1")
clock = pygame.time.Clock()
bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')
music = pygame.mixer.music.load('sound/backsound2.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2)

bg = pygame.image.load("real_image/back1.png")
char = pygame.image.load('real_image/br1.png')

font = pygame.font.SysFont('comicsans', 30, True)


def stage1(score) :
    global man
    ninja1_1 = Monster1(100, 410, 64, 64, 700)
    ninja1_2 = Monster1(300, 410, 64, 64, 700)
    ninja1_3 = Monster1(600, 410, 64, 64, 700)
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(37)
        # clock 속도 27 -> 37

        # ninja1_1 
        if ninja1_1.visible == True:   # 몬스터가 보이고 플레이어랑 맞았을 경우 점수 -5
            if ninja1_1.health > 0 :
                if man.hitbox[1] < ninja1_1.hitbox[1] + ninja1_1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_1.hitbox[1] :
                    if man.hitbox[0] + man.hitbox[2] > ninja1_1.hitbox[0] and man.hitbox[0] < ninja1_1.hitbox[0] + ninja1_1.hitbox[2]:
                        man.hit()
                        score -= 5
                        

        if ninja1_1.health == 0 : 
            ninja1_1.visible = False
        
        
        for bullet in bullets:
            if ninja1_1.health > 0 :
                if bullet.y - bullet.radius < ninja1_1.hitbox[1] + ninja1_1.hitbox[3] and bullet.y + bullet.radius > ninja1_1.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_1.hitbox[0] and bullet.x - bullet.radius < ninja1_1.hitbox[0] + ninja1_1.hitbox[2]:
                        hitSound.play()
                        ninja1_1.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja1_2
        if ninja1_2.visible == True:
            if ninja1_2.health > 0 :
                if man.hitbox[1] < ninja1_2.hitbox[1] + ninja1_2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_2.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja1_2.hitbox[0] and man.hitbox[0] < ninja1_2.hitbox[0] + ninja1_2.hitbox[2]:
                        man.hit()
                        score -= 5
                        #ninja1_2 = monster(600, 410, 64, 64, 700)
        if ninja1_2.health == 0 : 
            ninja1_2.visible = False
            

        for bullet in bullets:
            if ninja1_2.health > 0 :
                if bullet.y - bullet.radius < ninja1_2.hitbox[1] + ninja1_2.hitbox[3] and bullet.y + bullet.radius > ninja1_2.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_2.hitbox[0] and bullet.x - bullet.radius < ninja1_2.hitbox[0] + ninja1_2.hitbox[2]:
                        hitSound.play()
                        ninja1_2.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
                    
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # ninja1_3
        if ninja1_3.visible == True:
            if ninja1_3.health > 0 :
                if man.hitbox[1] < ninja1_3.hitbox[1] + ninja1_3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja1_3.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > ninja1_3.hitbox[0] and man.hitbox[0] < ninja1_3.hitbox[0] + ninja1_3.hitbox[2]:
                        man.hit()
                        score -= 5
                        #ninja1_3 = monster(600, 410, 64, 64, 700)
        if ninja1_3.health == 0 : 
            ninja1_3.visible = False
                

        for bullet in bullets:
            if ninja1_3.health > 0 :
                if bullet.y - bullet.radius < ninja1_3.hitbox[1] + ninja1_3.hitbox[3] and bullet.y + bullet.radius > ninja1_3.hitbox[1]:
                    if bullet.x + bullet.radius > ninja1_3.hitbox[0] and bullet.x - bullet.radius < ninja1_3.hitbox[0] + ninja1_3.hitbox[2]:
                        hitSound.play()
                        ninja1_3.hit()
                        score += 1
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

        """    
        for bullet in bullets:
            if bullet.y - bullet.radius < ninja.hitbox[1] + ninja.hitbox[3] and bullet.y + bullet.radius >ninja.hitbox[1]:
                if bullet.x + bullet.radius >ninja.hitbox[0] and bullet.x - bullet.radius < ninja.hitbox[0] + ninja.hitbox[2]:
                    hitSound.play()
                    ninja.hit()
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
        text = font.render('Score: ' + str(score), 1, (0,0,0))
        screen.blit(text, (620, 20))
        man.draw(screen)
        ninja1_1.draw(screen)
        ninja1_2.draw(screen)
        ninja1_3.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        
        pygame.display.update()

        if man.health == 0 :
            return man.health, score

        if (ninja1_1.health == 0) and (ninja1_2.health == 0) and (ninja1_3.health == 0) :
            return man.health, score