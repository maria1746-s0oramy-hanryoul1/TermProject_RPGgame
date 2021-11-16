import pygame
import sys

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 500))
background = pygame.image.load("real_image/back1.png")

# player right & left run image upload
walkRight = [pygame.image.load('real_image/br1.png'), pygame.image.load('real_image/br2.png'), pygame.image.load('real_image/br3.png'), pygame.image.load('real_image/br4.png'), pygame.image.load('real_image/br5.png'), pygame.image.load('real_image/br6.png'), pygame.image.load('real_image/br7.png'), pygame.image.load('real_image/br8.png'), pygame.image.load('real_image/br9.png')]
walkLeft = [pygame.image.load('real_image/bl1.png'), pygame.image.load('real_image/bl2.png'), pygame.image.load('real_image/bl3.png'), pygame.image.load('real_image/bl4.png'), pygame.image.load('real_image/bl5.png'), pygame.image.load('real_image/bl6.png'), pygame.image.load('real_image/bl7.png'), pygame.image.load('real_image/bl8.png'), pygame.image.load('real_image/bl9.png')]

class Player(object):
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
        self.health = 5

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

     # 몬스터 한테 맞았을 경우
    def hit(self):     
        self.isJump = False
        self.JumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        self.health -= 1
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

class Attack(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)


class Monster1(object):
    walkRight = [pygame.image.load('real_image/nbr1.png'), pygame.image.load('real_image/nbr1.png'), pygame.image.load('real_image/nbr2.png'), pygame.image.load('real_image/nbr2.png'), pygame.image.load('real_image/nbr3.png'), pygame.image.load('real_image/nbr4.png'), pygame.image.load('real_image/nbr5.png'), pygame.image.load('real_image/nbr6.png'), pygame.image.load('real_image/nbr7.png'), pygame.image.load('real_image/nbr8.png'), pygame.image.load('real_image/nbr9.png')]
    walkLeft = [pygame.image.load('real_image/nbl1.png'), pygame.image.load('real_image/nbl1.png'), pygame.image.load('real_image/nbl2.png'), pygame.image.load('real_image/nbl2.png'), pygame.image.load('real_image/nbl3.png'), pygame.image.load('real_image/nbL4.png'), pygame.image.load('real_image/nbl5.png'), pygame.image.load('real_image/nbl6.png'), pygame.image.load('real_image/nbl7.png'), pygame.image.load('real_image/nbl8.png'), pygame.image.load('real_image/nbl9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        # self.end -> 50 (monmany2 참고)
        self.walkCount = 0
        self.vel = 3
        # self.vel 3 -> 4
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
            self.health -= 1
        else:
            self.visible = False 
        
        print('hit')



class Monster2(object):
    walkRight = [pygame.image.load('real_image/attackR0.png'), pygame.image.load('real_image/attackR0.png'), pygame.image.load('real_image/attackR1.png'), pygame.image.load('real_image/attackR2.png'), pygame.image.load('real_image/attackR3.png'), pygame.image.load('real_image/attackR4.png'), pygame.image.load('real_image/attackR5.png'), pygame.image.load('real_image/attackR6.png'), pygame.image.load('real_image/attackR7.png'), pygame.image.load('real_image/attackR8.png'), pygame.image.load('real_image/attackR9.png')]
    walkLeft = [pygame.image.load('real_image/attackL0.png'), pygame.image.load('real_image/attackL0.png'), pygame.image.load('real_image/attackL1.png'), pygame.image.load('real_image/attackL2.png'), pygame.image.load('real_image/attackL3.png'), pygame.image.load('real_image/attackL4.png'), pygame.image.load('real_image/attackL5.png'), pygame.image.load('real_image/attackL6.png'), pygame.image.load('real_image/attackL7.png'), pygame.image.load('real_image/attackL8.png'), pygame.image.load('real_image/attackL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
        # self.vel 3 -> 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10  # 적의 수명 
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
            self.health -= 1
            
        else:
            self.visible = False
        print('hit')        


class Monster3(object):
    walkRight = [pygame.image.load('real_image/nnr.png'), pygame.image.load('real_image/nnr0.png'), pygame.image.load('real_image/nnr0.png'), pygame.image.load('real_image/nnr1.png'), pygame.image.load('real_image/nnr2.png'), pygame.image.load('real_image/nnr3.png'), pygame.image.load('real_image/nnr4.png'), pygame.image.load('real_image/nnr5.png'), pygame.image.load('real_image/nnr6.png')]
    walkLeft = [pygame.image.load('real_image/nnl.png'), pygame.image.load('real_image/nnl0.png'), pygame.image.load('real_image/nnl0.png'), pygame.image.load('real_image/nnl1.png'), pygame.image.load('real_image/nnl2.png'), pygame.image.load('real_image/nnl3.png'), pygame.image.load('real_image/nnl4.png'), pygame.image.load('real_image/nnl5.png'), pygame.image.load('real_image/nnl6.png')]

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

    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 27:
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



man = Player(50, 410, 64, 64)