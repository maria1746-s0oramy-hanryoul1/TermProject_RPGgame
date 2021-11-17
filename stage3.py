from header import *
import pygame


pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 3")
clock = pygame.time.Clock()
bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')
music = pygame.mixer.music.load('sound/backsound.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2) 

bg = pygame.image.load("real_image/back3.png")
char = pygame.image.load('real_image/br1.png')

font = pygame.font.SysFont('comicsans', 30, True)


def stage3(score) : 
    global man
    ninja3 = Monster3(200, 390, 64, 64, 700)
    man = Player(50, 410, 64, 64)
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(37)

        if ninja3.visible == True:
            if man.hitbox[1] < ninja3.hitbox[1] + ninja3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja3.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja3.hitbox[0] and man.hitbox[0] < ninja3.hitbox[0] + ninja3.hitbox[2]:
                    man.hit()
                    score -= 5
                    # ninja3 = Monster3(600, 410, 64, 64, 700)
                    man = Player(50, 410, 64, 64)
                    
        if ninja3.health == 0 : 
            ninja3.visible = False 

        for bullet in bullets:
            if ninja3.health > 0 :
                if bullet.y - bullet.radius < ninja3.hitbox[1] + ninja3.hitbox[3] and bullet.y + bullet.radius > ninja3.hitbox[1]:
                    if bullet.x + bullet.radius > ninja3.hitbox[0] and bullet.x - bullet.radius < ninja3.hitbox[0] + ninja3.hitbox[2]:
                        hitSound.play()
                        ninja3.hit()
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
            if bullet.y - bullet.radius < ninja3.hitbox[1] + ninja3.hitbox[3] and bullet.y + bullet.radius > ninja3.hitbox[1]:
                if bullet.x + bullet.radius > ninja3.hitbox[0] and bullet.x - bullet.radius < ninja3.hitbox[0] + ninja3.hitbox[2]:
                    hitSound.play()
                    ninja3.hit()
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
                
            if len(bullets) < 5 and ninja3.visible == True:
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
        ninja3.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        
        pygame.display.update()

        if man.health == 0 :
            return man.health, score

        if ninja3.health == 0 :
            return man.health, score