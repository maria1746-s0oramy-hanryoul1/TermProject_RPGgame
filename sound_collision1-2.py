import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 2")

walkRight = [pygame.image.load('real_image/br1.png'), pygame.image.load('real_image/br2.png'), pygame.image.load('real_image/br3.png'), pygame.image.load('real_image/br4.png'), pygame.image.load('real_image/br5.png'), pygame.image.load('real_image/br6.png'), pygame.image.load('real_image/br7.png'), pygame.image.load('real_image/br8.png'), pygame.image.load('real_image/br9.png')]
walkLeft = [pygame.image.load('real_image/bl1.png'), pygame.image.load('real_image/bl2.png'), pygame.image.load('real_image/bl3.png'), pygame.image.load('real_image/bl4.png'), pygame.image.load('real_image/bl5.png'), pygame.image.load('real_image/bl6.png'), pygame.image.load('real_image/bl7.png'), pygame.image.load('real_image/bl8.png'), pygame.image.load('real_image/bl9.png')]
bg = pygame.image.load("real_image/back2.png")
char = pygame.image.load('real_image/br1.png')


clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('sound/bullet.mp3')
hitSound = pygame.mixer.Sound('sound/hit.mp3')

music = pygame.mixer.music.load('sound/backsound4.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.2) 

score = 0

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
                self.walkCount +=1
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
        self.vel = 6
        # 속도 조절로 난이도 상승
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

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
            self.health -= 0.5
            # 생명 감소 속도 조절
            
        else:
            self.visible = False
        print('hit')

        

def redrawGamescreen():
    screen.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    screen.blit(text, (620, 20))
    man.draw(screen)
    ninja_g1.draw(screen)
    ninja_g2.draw(screen)
    ninja_g3.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(50, 410, 64, 64)

ninja_g1 = monster(100, 410, 64, 64, 700)
ninja_g2 = monster(300, 410, 64, 64, 700)
ninja_g3 = monster(600, 410, 64, 64, 700)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(35)

    # ninja_g1 
    if ninja_g1.visible == True:
        if ninja_g1.health > 0 :
            if man.hitbox[1] < ninja_g1.hitbox[1] + ninja_g1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja_g1.hitbox[1] :
                if man.hitbox[0] + man.hitbox[2] > ninja_g1.hitbox[0] and man.hitbox[0] < ninja_g1.hitbox[0] + ninja_g1.hitbox[2]:
                    man.hit()
                    score -= 5
                    #ninja_g1 = monster(600, 410, 64, 64, 700)
    if ninja_g1.health == 0 : 
        ninja_g1.visible = False
    
    
    for bullet in bullets:
        if ninja_g1.health > 0 :
            if bullet.y - bullet.radius < ninja_g1.hitbox[1] + ninja_g1.hitbox[3] and bullet.y + bullet.radius > ninja_g1.hitbox[1]:
                if bullet.x + bullet.radius > ninja_g1.hitbox[0] and bullet.x - bullet.radius < ninja_g1.hitbox[0] + ninja_g1.hitbox[2]:
                    hitSound.play()
                    ninja_g1.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # ninja_g2
    if ninja_g2.visible == True:
        if ninja_g2.health > 0 :
            if man.hitbox[1] < ninja_g2.hitbox[1] + ninja_g2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja_g2.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja_g2.hitbox[0] and man.hitbox[0] < ninja_g2.hitbox[0] + ninja_g2.hitbox[2]:
                    man.hit()
                    score -= 5
                    #ninja_g2 = monster(600, 410, 64, 64, 700)
    if ninja_g2.health == 0 : 
        ninja_g2.visible = False
        

    for bullet in bullets:
        if ninja_g2.health > 0 :
            if bullet.y - bullet.radius < ninja_g2.hitbox[1] + ninja_g2.hitbox[3] and bullet.y + bullet.radius > ninja_g2.hitbox[1]:
                if bullet.x + bullet.radius > ninja_g2.hitbox[0] and bullet.x - bullet.radius < ninja_g2.hitbox[0] + ninja_g2.hitbox[2]:
                    hitSound.play()
                    ninja_g2.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
                
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # ninja_g3
    if ninja_g3.visible == True:
        if ninja_g3.health > 0 :
            if man.hitbox[1] < ninja_g3.hitbox[1] + ninja_g3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > ninja_g3.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > ninja_g3.hitbox[0] and man.hitbox[0] < ninja_g3.hitbox[0] + ninja_g3.hitbox[2]:
                    man.hit()
                    score -= 5
                    #ninja_g3 = monster(600, 410, 64, 64, 700)
    if ninja_g3.health == 0 : 
        ninja_g3.visible = False
            

    for bullet in bullets:
        if ninja_g3.health > 0 :
            if bullet.y - bullet.radius < ninja_g3.hitbox[1] + ninja_g3.hitbox[3] and bullet.y + bullet.radius > ninja_g3.hitbox[1]:
                if bullet.x + bullet.radius > ninja_g3.hitbox[0] and bullet.x - bullet.radius < ninja_g3.hitbox[0] + ninja_g3.hitbox[2]:
                    hitSound.play()
                    ninja_g3.hit()
                    score += 1
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
            
    redrawGamescreen()

pygame.quit()