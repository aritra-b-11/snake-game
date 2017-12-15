import pygame, sys
from pygame.locals import *
from random import randint
from random import choice

pygame.init()
pixel = 20
width_mult, height_mult = 40, 20
width, height = pixel*width_mult, pixel*height_mult

myfont = pygame.font.SysFont("monospace", 16)
pygame.display.set_caption("Snake")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0)
blue= (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode((width,height))

snakeBodyImg = pygame.image.load('snake_head.jpg')
snakeBodyImg = pygame.transform.scale(snakeBodyImg,(pixel,pixel))

snakeHeadImgLeft = pygame.image.load('snake-head-left.png')
snakeHeadImgLeft = pygame.transform.scale(snakeHeadImgLeft,(pixel,pixel))
snakeHeadImgRight = pygame.transform.flip(snakeHeadImgLeft,1,0)
snakeHeadImgDown =  pygame.transform.rotate(snakeHeadImgLeft,90)
snakeHeadImgUp =  pygame.transform.rotate(snakeHeadImgLeft,270)

snakeHeadImg = snakeHeadImgRight
snakeHeadX = width_mult*pixel*0.5
snakeHeadY = height_mult*pixel*0.5

geccoImg = pygame.image.load('small-gecco.jpg')
geccoImg = pygame.transform.scale(geccoImg,(pixel,pixel))
geccoX= randint(2,width_mult-2)*pixel
geccoY= randint(2,height_mult-2)*pixel

#print geccoY,geccoX

speed = pixel * 1
direction = 'right'
FPS = speed * 0.25
fpsClock = pygame.time.Clock()

score = 0

#pygame.mixer.music.load('snake.mp3')
#pygame.mixer.music.play(-1, 0.0)


length = 3
direction_array=[]
position_array_X = []
position_array_Y = []

for i in range(length-1):
    direction_array.append(direction)

while True:
    DISPLAYSURF.fill(white)
    # print "body",snakeBodyImg.get_rect()
    # print "head",snakeHeadImg.get_rect()
    # print "food",geccoImg.get_rect()
    topEdge = pygame.draw.rect(DISPLAYSURF, red, (0,0,width,pixel))
    bottomEdge = pygame.draw.rect(DISPLAYSURF, red, (0,height-pixel,width,pixel))
    leftEdge = pygame.draw.rect(DISPLAYSURF, red, (0,0,pixel,height))
    rightEdge = pygame.draw.rect(DISPLAYSURF, red, (width-pixel,0,pixel,height))
#    print snakeHeadX,snakeHeadY
    if(direction == 'right'):
        snakeHeadX += speed
        if(snakeHeadX > width-pixel):
            snakeHeadX = pixel
            #print "right"
    elif(direction == 'left'):
        snakeHeadX -= speed
        if(snakeHeadX < pixel):
            snakeHeadX = width-pixel
            #print "left"
    elif(direction == 'up'):
        snakeHeadY -=speed
        if(snakeHeadY < pixel):
            snakeHeadY = height-pixel
            #print "up"
    elif(direction == 'down'):
        snakeHeadY += speed
        if(snakeHeadY > height-pixel):
            snakeHeadY = pixel
            #print "down"
    DISPLAYSURF.blit(snakeHeadImg, (snakeHeadX,snakeHeadY))
    DISPLAYSURF.blit(geccoImg, (geccoX,geccoY))
    if(snakeHeadX==geccoX and snakeHeadY==geccoY):
        length += 1
        score += 1
        direction_array.append(direction)
        geccoX= choice([i for i in range(1,width_mult-1) if i*pixel not in position_array_X])*pixel
        geccoY= choice([i for i in range(1,height_mult-1) if i*pixel not in position_array_Y])*pixel
        # chose a rand number excluding the position array
        # print geccoY,geccoX
    pivotX=snakeHeadX
    pivotY=snakeHeadY
    position_array_X = []
    position_array_Y = []
    # print geccoX,geccoY
    for i in range(length-1):
        if(direction_array[i]=='right'):
            pivotX -= pixel
        elif(direction_array[i]=='left'):
            pivotX += pixel
        elif(direction_array[i]=='up'):
            pivotY += pixel
        elif(direction_array[i]=='down'):
            pivotY -= pixel
        position_array_X.append(pivotX)
        position_array_Y.append(pivotY)
        DISPLAYSURF.blit(snakeBodyImg, (pivotX,pivotY))
        # print "position", position_array
    #print snakeHeadX,snakeHeadY
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                direction = 'right'
                snakeHeadImg = snakeHeadImgRight
            elif event.key==pygame.K_LEFT:
                direction = 'left'
                snakeHeadImg = snakeHeadImgLeft
            elif event.key==pygame.K_UP:
                direction = 'up'
                snakeHeadImg = snakeHeadImgUp
            elif event.key==pygame.K_DOWN:
                direction = 'down'
                snakeHeadImg = snakeHeadImgDown
    scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
    DISPLAYSURF.blit(scoretext, (5, 5))
    direction_array=direction_array[::-1]
    direction_array.append(direction)
    direction_array=direction_array[::-1]
    del(direction_array[len(direction_array)-1])
    pygame.display.update()
    fpsClock.tick(FPS)


