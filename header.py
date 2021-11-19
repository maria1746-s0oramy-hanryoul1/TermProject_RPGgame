import pygame
import sys

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 500))
background = pygame.image.load("real_image/back.jpg")

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
        self.right = True
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 5
        self.neg = 1 # 점프할때 씀

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
        self.x = 50
        self.y = 410
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = True
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.health -= 1
        self.neg = 1 
        #font1 = pygame.font.SysFont('comicsans', 100)
        #text = font1.render('-5', 1, (255,0,0))
        #screen.blit(text, (400 - (text.get_width()/2),200))
        broken_heart = pygame.image.load('real_image/broken_heart.png') #충돌 시 하트 -1 이미지
        screen.blit(broken_heart, (400 - (broken_heart.get_width()/2), 50))
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
        self.vel = 8 * self.facing

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
        self.mon_health = 10
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
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.mon_health)), 10))
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
        if self.mon_health > 0:
            self.mon_health -= 1
        else:
            self.visible = False 
        
#여자 닌자 2_1, 2_2, 2_3 으로 클래스 추가 
class Monster2_1(object):
    walkRight = [pygame.image.load('real_image/NR.png'), pygame.image.load('real_image/NR.png'), pygame.image.load('real_image/NR1.png'), pygame.image.load('real_image/NR2.png'), pygame.image.load('real_image/NR3.png'), pygame.image.load('real_image/NR4.png'), pygame.image.load('real_image/NR5.png'), pygame.image.load('real_image/NR6.png'), pygame.image.load('real_image/NR7.png'), pygame.image.load('real_image/NR8.png'), pygame.image.load('real_image/NR9.png')]
    walkLeft = [pygame.image.load('real_image/NL.png'), pygame.image.load('real_image/NL.png'), pygame.image.load('real_image/NL1.png'), pygame.image.load('real_image/NL2.png'), pygame.image.load('real_image/NL3.png'), pygame.image.load('real_image/NL4.png'), pygame.image.load('real_image/NL5.png'), pygame.image.load('real_image/NL6.png'), pygame.image.load('real_image/NL7.png'), pygame.image.load('real_image/NL8.png'), pygame.image.load('real_image/NL9.png')]

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
        self.mon_health = 10  # 적의 수명 
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
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.mon_health)), 10))
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
        if self.mon_health > 0:
            self.mon_health -= 1
            
        else:
            self.visible = False

class Monster2_2(object):
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
        self.mon_health = 10  # 적의 수명 
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
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.mon_health)), 10))
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
        if self.mon_health > 0:
            self.mon_health -= 1
            
        else:
            self.visible = False

class Monster2_3(object):
    walkRight = [pygame.image.load('real_image/jattackR0.png'), pygame.image.load('real_image/jattackR0.png'), pygame.image.load('real_image/jattackR1.png'), pygame.image.load('real_image/jattackR2.png'), pygame.image.load('real_image/jattackR3.png'), pygame.image.load('real_image/jattackR4.png'), pygame.image.load('real_image/jattackR5.png'), pygame.image.load('real_image/jattackR6.png'), pygame.image.load('real_image/jattackR7.png'), pygame.image.load('real_image/jattackR8.png'), pygame.image.load('real_image/jattackR9.png')]
    walkLeft = [pygame.image.load('real_image/jattackL0.png'), pygame.image.load('real_image/jattackL0.png'), pygame.image.load('real_image/jattackL1.png'), pygame.image.load('real_image/jattackL2.png'), pygame.image.load('real_image/jattackL3.png'), pygame.image.load('real_image/jattackL4.png'), pygame.image.load('real_image/jattackL5.png'), pygame.image.load('real_image/jattackL6.png'), pygame.image.load('real_image/jattackL7.png'), pygame.image.load('real_image/jattackL8.png'), pygame.image.load('real_image/jattackL9.png')]

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
        self.mon_health = 10  # 적의 수명 
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
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.mon_health)), 10))
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
        if self.mon_health > 0:
            self.mon_health -= 1
            
        else:
            self.visible = False


class Monster3(object):
    walkRight = [pygame.image.load('real_image/nnr.png'), pygame.image.load('real_image/nnr0.png'), pygame.image.load('real_image/nnr0.png'), pygame.image.load('real_image/nnr1.png'), pygame.image.load('real_image/nnr2.png'), pygame.image.load('real_image/nnr3.png'), pygame.image.load('real_image/nnr4.png'), pygame.image.load('real_image/nnr5.png'), pygame.image.load('real_image/nnr6.png')]
    walkLeft = [pygame.image.load('real_image/nnl.png'), pygame.image.load('real_image/nnl0.png'), pygame.image.load('real_image/nnl0.png'), pygame.image.load('real_image/nnl1.png'), pygame.image.load('real_image/nnl2.png'), pygame.image.load('real_image/nnl3.png'), pygame.image.load('real_image/nnl4.png'), pygame.image.load('real_image/nnl5.png'), pygame.image.load('real_image/nnl6.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.mon_health = 10
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
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.mon_health)), 10))
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
        if self.mon_health > 0:
            self.mon_health -= 1
        else:
            self.visible = False

man = Player(50, 410, 64, 64) # 시작 X축, y축, 가로 이동범위, 높이 이동범위