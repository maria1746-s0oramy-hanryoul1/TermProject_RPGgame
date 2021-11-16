import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500)) 
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 1")

walkRight = [pygame.image.load('real_image/br1.png'), pygame.image.load('real_image/br2.png'), pygame.image.load('real_image/br3.png'), pygame.image.load('real_image/br4.png'), pygame.image.load('real_image/br5.png'), pygame.image.load('real_image/br6.png'), pygame.image.load('real_image/br7.png'), pygame.image.load('real_image/br8.png'), pygame.image.load('real_image/br9.png')]
walkLeft = [pygame.image.load('real_image/bl1.png'), pygame.image.load('real_image/bl2.png'), pygame.image.load('real_image/bl3.png'), pygame.image.load('real_image/bl4.png'), pygame.image.load('real_image/bl5.png'), pygame.image.load('real_image/bl6.png'), pygame.image.load('real_image/bl7.png'), pygame.image.load('real_image/bl8.png'), pygame.image.load('real_image/bl9.png')]
bg = pygame.image.load("real_image/back1.png")
char = pygame.image.load('real_image/br1.png')


clock = pygame.time.Clock() 

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0 
        self.standing = True

    def draw(self, screen):
        
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left :   
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

class attack(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color 
        self.facing = facing
        self.vel = 8 * facing 

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class monster(object):
    walkRight = [pygame.image.load('real_image/Dr1.png'), pygame.image.load('real_image/Dr2.png'), pygame.image.load('real_image/Dr3.png'), pygame.image.load('real_image/Dr4.png'), pygame.image.load('real_image/Dr5.png'), pygame.image.load('real_image/Dr6.png'), pygame.image.load('real_image/Dr7.png'), pygame.image.load('real_image/Dr8.png'), pygame.image.load('real_image/Dr9.png'), pygame.image.load('real_image/Dr10.png'), pygame.image.load('real_image/Dr11.png')]
    walkLeft = [pygame.image.load('real_image/DL1.png'), pygame.image.load('real_image/DL2.png'), pygame.image.load('real_image/DL3.png'), pygame.image.load('real_image/DL4.png'), pygame.image.load('real_image/DL5.png'), pygame.image.load('real_image/DL6.png'), pygame.image.load('real_image/DL7.png'), pygame.image.load('real_image/DL8.png'), pygame.image.load('real_image/DL9.png'), pygame.image.load('real_image/DL10.png'), pygame.image.load('real_image/DL11.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            screen.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

def redrawGamescreendow():
    screen.blit(bg, (0, 0))
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen) 

    pygame.display.update()

#main loop
man = player(50, 400, 64, 64)
goblin = monster(50, 410, 64, 64, 700)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel 
        else:
            bullets.pop(bullets.index(bullet)) 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(attack(round(man.x + man.width // 2), round(man.y + man.height //2), 6, (0,0,0), facing)) 

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

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0 
    else:
        if man.jumpCount >= -10 :
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else: 
            man.isJump = False
            man.jumpCount = 10

    redrawGamescreendow() 

pygame.quit() 