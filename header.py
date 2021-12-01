# 모듈 임포트
import pygame
import time
import sys

clock = pygame.time.Clock()  # clock 객체 초기화
screen = pygame.display.set_mode((800, 500))  # 그릴 화면(스크롤) 초기화 

# 배경 및 플레이어 이미지 로딩 
background = pygame.image.load("image/back.jpg")
walkRight = [pygame.image.load('image/br1.png'), pygame.image.load('image/br2.png'), pygame.image.load('image/br3.png'), pygame.image.load('image/br4.png'), pygame.image.load('image/br5.png'), pygame.image.load('image/br6.png'), pygame.image.load('image/br7.png'), pygame.image.load('image/br8.png'), pygame.image.load('image/br9.png')]
walkLeft = [pygame.image.load('image/bl1.png'), pygame.image.load('image/bl2.png'), pygame.image.load('image/bl3.png'), pygame.image.load('image/bl4.png'), pygame.image.load('image/bl5.png'), pygame.image.load('image/bl6.png'), pygame.image.load('image/bl7.png'), pygame.image.load('image/bl8.png'), pygame.image.load('image/bl9.png')]

# 플레이어 클래스 
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
        self.health = 3
        self.neg = 1 
        self.flag = 0
        self.hittime = 0

    # 플레이어 이동 함수
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

    # 몬스터 충돌 시 무적 설정   
    def hit(self) : 
        if self.flag == 0 :                     
            self.flag = 1                           
            self.hittime = time.time()              
            self.real_hit()                         
        else : 
            if time.time() - self.hittime > 3 :     
                self.flag = 0                      

    # 몬스터한테 맞는 경우
    def real_hit(self):
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
        self.neg = 1 
        self.health -= 1
    
        broken_heart = pygame.image.load('image/broken_heart.png') 
        screen.blit(broken_heart, (400 - (broken_heart.get_width()/2), 50))
        pygame.display.update()     
        pygame.time.delay(1000)

# 플레이어가 공격하는 클래스
class Attack(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * self.facing

    # 공격 이미지 그리기
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)

# 1단계 몬스터
class Monster1_1(object):
    walkRight = [pygame.image.load('image/nbr1.png'), pygame.image.load('image/nbr2.png'), pygame.image.load('image/nbr3.png'), pygame.image.load('image/nbr4.png'), pygame.image.load('image/nbr5.png'), pygame.image.load('image/nbr6.png'), pygame.image.load('image/nbr7.png'), pygame.image.load('image/nbr8.png'), pygame.image.load('image/nbr9.png')]
    walkLeft = [pygame.image.load('image/nbl1.png'), pygame.image.load('image/nbl2.png'),pygame.image.load('image/nbl3.png'), pygame.image.load('image/nbL4.png'), pygame.image.load('image/nbl5.png'), pygame.image.load('image/nbl6.png'), pygame.image.load('image/nbl7.png'), pygame.image.load('image/nbl8.png'), pygame.image.load('image/nbl9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.mon_health = 10   
        self.visible = True

    # 몬스터 이동 
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

    # 몬스터 이동 범위 설정
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

    # 몬스터 플레이어게 공격 받는 경우
    def hit(self):
        if self.mon_health > 0:
            self.mon_health -= 1
        else:
            self.visible = False 

class Monster1_2(object):
    walkRight = [pygame.image.load('image/atR0.png'), pygame.image.load('image/atR0.png'), pygame.image.load('image/atR1.png'),pygame.image.load('image/atR2.png'), pygame.image.load('image/atR3.png'), pygame.image.load('image/atR4.png'), pygame.image.load('image/atR5.png'), pygame.image.load('image/atR6.png'), pygame.image.load('image/atR7.png'), pygame.image.load('image/atR8.png'), pygame.image.load('image/atR9.png')]
    walkLeft = [pygame.image.load('image/atL0.png'), pygame.image.load('image/atL0.png'), pygame.image.load('image/atL1.png'), pygame.image.load('image/atL2.png'),pygame.image.load('image/atL3.png'), pygame.image.load('image/atL4.png'), pygame.image.load('image/atL5.png'), pygame.image.load('image/atL6.png'), pygame.image.load('image/atL7.png'), pygame.image.load('image/atL8.png'), pygame.image.load('image/atL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
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

class Monster1_3(object):
    walkRight = [pygame.image.load('image/jpR0.png'), pygame.image.load('image/jpR0.png'), pygame.image.load('image/jpR1.png'),pygame.image.load('image/jpR2.png'), pygame.image.load('image/jpR3.png'), pygame.image.load('image/jpR4.png'), pygame.image.load('image/jpR5.png'), pygame.image.load('image/jpR6.png'), pygame.image.load('image/jpR7.png'), pygame.image.load('image/jpR8.png'), pygame.image.load('image/jpR9.png')]
    walkLeft = [pygame.image.load('image/jpL0.png'), pygame.image.load('image/jpL0.png'), pygame.image.load('image/jpL1.png'), pygame.image.load('image/jpL2.png'),pygame.image.load('image/jpL3.png'), pygame.image.load('image/jpL4.png'), pygame.image.load('image/jpL5.png'), pygame.image.load('image/jpL6.png'), pygame.image.load('image/jpL7.png'), pygame.image.load('image/jpL8.png'), pygame.image.load('image/jpL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 4
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

# 2단계 몬스터       
class Monster2_1(object):
    walkRight = [pygame.image.load('image/NR.png'), pygame.image.load('image/NR.png'), pygame.image.load('image/NR1.png'), pygame.image.load('image/NR2.png'), pygame.image.load('image/NR3.png'), pygame.image.load('image/NR4.png'), pygame.image.load('image/NR5.png'), pygame.image.load('image/NR6.png'), pygame.image.load('image/NR7.png'), pygame.image.load('image/NR8.png'), pygame.image.load('image/NR9.png')]
    walkLeft = [pygame.image.load('image/NL.png'), pygame.image.load('image/NL.png'), pygame.image.load('image/NL1.png'), pygame.image.load('image/NL2.png'), pygame.image.load('image/NL3.png'), pygame.image.load('image/NL4.png'), pygame.image.load('image/NL5.png'), pygame.image.load('image/NL6.png'), pygame.image.load('image/NL7.png'), pygame.image.load('image/NL8.png'), pygame.image.load('image/NL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.mon_health = 10  
        self.visible = True

    # 몬스터 이동
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

    # 몬스터 이동 범위 설정
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

    # 몬스터 플레이어에게 공격 받는 경우
    def hit(self):
        if self.mon_health > 0:
            self.mon_health -= 0.7
            
        else:
            self.visible = False

class Monster2_2(object):
    walkRight = [pygame.image.load('image/attackR0.png'), pygame.image.load('image/attackR0.png'), pygame.image.load('image/attackR1.png'), pygame.image.load('image/attackR2.png'), pygame.image.load('image/attackR3.png'), pygame.image.load('image/attackR4.png'), pygame.image.load('image/attackR5.png'), pygame.image.load('image/attackR6.png'), pygame.image.load('image/attackR7.png'), pygame.image.load('image/attackR8.png'), pygame.image.load('image/attackR9.png')]
    walkLeft = [pygame.image.load('image/attackL0.png'), pygame.image.load('image/attackL0.png'), pygame.image.load('image/attackL1.png'), pygame.image.load('image/attackL2.png'), pygame.image.load('image/attackL3.png'), pygame.image.load('image/attackL4.png'), pygame.image.load('image/attackL5.png'), pygame.image.load('image/attackL6.png'), pygame.image.load('image/attackL7.png'), pygame.image.load('image/attackL8.png'), pygame.image.load('image/attackL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
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
            self.mon_health -= 0.8 
        else:
            self.visible = False

class Monster2_3(object):
    walkRight = [pygame.image.load('image/2GR0.png'), pygame.image.load('image/2GR0.png'), pygame.image.load('image/2GR1.png'), pygame.image.load('image/2GR2.png'), pygame.image.load('image/2GR3.png'), pygame.image.load('image/2GR4.png'), pygame.image.load('image/2GR5.png'), pygame.image.load('image/2GR6.png'), pygame.image.load('image/2GR7.png'), pygame.image.load('image/2GR8.png'), pygame.image.load('image/2GR9.png')]
    walkLeft = [pygame.image.load('image/2GL0.png'), pygame.image.load('image/2GL0.png'), pygame.image.load('image/2GL1.png'), pygame.image.load('image/2GL2.png'), pygame.image.load('image/2GL3.png'), pygame.image.load('image/2GL4.png'), pygame.image.load('image/2GL5.png'), pygame.image.load('image/2GL6.png'), pygame.image.load('image/2GL7.png'), pygame.image.load('image/2GL8.png'), pygame.image.load('image/2GL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
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

class Monster2_4(object):
    walkRight = [pygame.image.load('image/2GR0.png'), pygame.image.load('image/2GR0.png'), pygame.image.load('image/2GR1.png'), pygame.image.load('image/2GR2.png'), pygame.image.load('image/2GR3.png'), pygame.image.load('image/2GR4.png'), pygame.image.load('image/2GR5.png'), pygame.image.load('image/2GR6.png'), pygame.image.load('image/2GR7.png'), pygame.image.load('image/2GR8.png'), pygame.image.load('image/2GR9.png')]
    walkLeft = [pygame.image.load('image/2GL0.png'), pygame.image.load('image/2GL0.png'), pygame.image.load('image/2GL1.png'), pygame.image.load('image/2GL2.png'), pygame.image.load('image/2GL3.png'), pygame.image.load('image/2GL4.png'), pygame.image.load('image/2GL5.png'), pygame.image.load('image/2GL6.png'), pygame.image.load('image/2GL7.png'), pygame.image.load('image/2GL8.png'), pygame.image.load('image/2GL9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
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
            self.mon_health -= 0.7  
        else:
            self.visible = False

# 3단계 몬스터
class Monster3_1(object):
    walkRight = [pygame.image.load('image/nnr1.png'), pygame.image.load('image/nnr2.png'), pygame.image.load('image/nnr3.png'), pygame.image.load('image/nnr4.png'), pygame.image.load('image/nnr5.png'), pygame.image.load('image/nnr6.png'), pygame.image.load('image/nnr1.png'), pygame.image.load('image/nnr2.png'), pygame.image.load('image/nnr3.png'), pygame.image.load('image/nnr4.png'), pygame.image.load('image/nnr5.png'), pygame.image.load('image/nnr6.png')]
    walkLeft = [pygame.image.load('image/nnl1.png'), pygame.image.load('image/nnl2.png'), pygame.image.load('image/nnl3.png'), pygame.image.load('image/nnl4.png'), pygame.image.load('image/nnl5.png'), pygame.image.load('image/nnl6.png'), pygame.image.load('image/nnl1.png'), pygame.image.load('image/nnl2.png'), pygame.image.load('image/nnl3.png'), pygame.image.load('image/nnl4.png'), pygame.image.load('image/nnl5.png'), pygame.image.load('image/nnl6.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 7, self.y + 30, 45, 100)
        self.mon_health = 50
        self.visible = True

    # 몬스터 이동 
    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 36:
                self.walkCount = 0

            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 100 - (2 * (50 - self.mon_health)), 10)) 
            self.hitbox = (self.x, self.y + 30, 45, 100)

    # 몬스터 이동 범위 설정
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

    # 몬스터 플레이어에게 공격 받는 경우
    def hit(self):
        if self.mon_health > 0:
            self.mon_health -= 1
        else:
            self.visible = False

class Monster3_2(object):
    walkRight = [pygame.image.load('image/rgr1.png'), pygame.image.load('image/rgr2.png'), pygame.image.load('image/rgr3.png'), pygame.image.load('image/rgr4.png'), pygame.image.load('image/rgr5.png'), pygame.image.load('image/rgr1.png'), pygame.image.load('image/rgr2.png'), pygame.image.load('image/rgr3.png'), pygame.image.load('image/rgr4.png'), pygame.image.load('image/rgr5.png')]
    walkLeft = [pygame.image.load('image/rgl1.png'), pygame.image.load('image/rgl2.png'), pygame.image.load('image/rgl3.png'), pygame.image.load('image/rgl4.png'), pygame.image.load('image/rgl5.png'), pygame.image.load('image/rgl1.png'), pygame.image.load('image/rgl2.png'), pygame.image.load('image/rgl3.png'), pygame.image.load('image/rgl4.png'), pygame.image.load('image/rgl5.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [50, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.mon_health = 10
        self.visible = True

    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 30:
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

man = Player(50, 410, 64, 64) 