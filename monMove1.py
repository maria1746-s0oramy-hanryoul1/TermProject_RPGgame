import pygame

pygame.init()
win = pygame.display.set_mode((800, 500)) 
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 1")

walkRight = [pygame.image.load('real_image/R1.png'), pygame.image.load('real_image/R2.png'), pygame.image.load('real_image/R3.png'), pygame.image.load('real_image/R4.png'), pygame.image.load('real_image/R5.png'), pygame.image.load('real_image/R6.png'), pygame.image.load('real_image/R7.png'), pygame.image.load('real_image/R8.png'), pygame.image.load('real_image/R9.png')]
walkLeft = [pygame.image.load('real_image/L1.png'), pygame.image.load('real_image/L2.png'), pygame.image.load('real_image/L3.png'), pygame.image.load('real_image/L4.png'), pygame.image.load('real_image/L5.png'), pygame.image.load('real_image/L6.png'), pygame.image.load('real_image/L7.png'), pygame.image.load('real_image/L8.png'), pygame.image.load('real_image/L9.png')]
bg = pygame.image.load("real_image/back1.png")
char = pygame.image.load('real_image/standing.png')


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

    def draw(self, win):
        
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left :   
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1 
        else: 
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color 
        self.facing = facing
        self.vel = 8 * facing 

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class mon(object):
    walkRight = [pygame.image.load('real_image/R1E.png'), pygame.image.load('real_image/R2E.png'), pygame.image.load('real_image/R3E.png'), pygame.image.load('real_image/R4E.png'), pygame.image.load('real_image/R5E.png'), pygame.image.load('real_image/R6E.png'), pygame.image.load('real_image/R7E.png'), pygame.image.load('real_image/R8E.png'), pygame.image.load('real_image/R9E.png'), pygame.image.load('real_image/R10E.png'), pygame.image.load('real_image/R11E.png')]
    walkLeft = [pygame.image.load('real_image/L1E.png'), pygame.image.load('real_image/L2E.png'), pygame.image.load('real_image/L3E.png'), pygame.image.load('real_image/L4E.png'), pygame.image.load('real_image/L5E.png'), pygame.image.load('real_image/L6E.png'), pygame.image.load('real_image/L7E.png'), pygame.image.load('real_image/L8E.png'), pygame.image.load('real_image/L9E.png'), pygame.image.load('real_image/L10E.png'), pygame.image.load('real_image/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
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

def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win) 

    pygame.display.update()

#main loop
man = player(50, 400, 64, 64)
goblin = mon(100, 410, 64, 64, 750)
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
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height //2), 6, (0,0,0), facing)) 

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

    redrawGameWindow() 

pygame.quit() 