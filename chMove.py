import pygame

pygame.init()
win = pygame.display.set_mode((800, 500)) 
pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 1")

walkRight = [pygame.image.load('real_image/chr_R1.png'), pygame.image.load('real_image/chr_R2.png')]
walkLeft = [pygame.image.load('real_image/chr_L1.png'),pygame.image.load('real_image/chr_L2.png')]
bg = pygame.image.load("real_image/back1.png")
char = pygame.image.load('real_image/chr.png')

clock = pygame.time.Clock()

x = 50 
y = 400 
width = 70
height = 80 
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0  

def game():
    global walkCount 
    win.blit(bg, (0, 0))

    if walkCount + 1 > 27:
        walkCount = 0
    
    if left :
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y)) 
        walkCount += 1
    else: 
        win.blit(char, (x,y))
    pygame.display.update()

#main loop
run = True
while run:
    clock.tick(27 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
       x -= vel
       left = True
       right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel :
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0 
    else:
        if jumpCount >= -10 :
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else: 
            isJump = False
            jumpCount = 10

    game()

pygame.quit()