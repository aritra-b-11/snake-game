import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
pixel = 30
width_mult, height_mult = 40, 20
width, height = pixel*width_mult, pixel*height_mult

pygame.display.set_caption("Snake")

FPS = pixel
fpsClock = pygame.time.Clock()

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
geccoX= randint(0,width_mult)*pixel
geccoY= randint(0,height_mult)*pixel

low = pixel * 0.2
mid = pixel * 0.4
high = pixel * 0.6
speed = low
direction = 'right'

length = 3
direction_array=[]
for i in range(length):
    direction_array.append(direction)

while True:
    DISPLAYSURF.fill(red)
    if(direction == 'right'):
        snakeHeadX += speed
        if(snakeHeadX >= width-pixel):
            snakeHeadX = pixel
    elif(direction == 'left'):
        snakeHeadX -= speed
        if(snakeHeadX <= pixel):
            snakeHeadX = width-pixel
    elif(direction == 'up'):
        snakeHeadY -=speed
        if(snakeHeadY <= pixel):
            snakeHeadY = height-pixel
    elif(direction == 'down'):
        snakeHeadY += speed
        if(snakeHeadY >= height-pixel):
            snakeHeadY = pixel
    DISPLAYSURF.blit(snakeHeadImg, (snakeHeadX,snakeHeadY))
    DISPLAYSURF.blit(geccoImg, (geccoX,geccoY))
    if(snakeHeadX==geccoX and snakeHeadY==geccoY):
        length += 1
        geccoX= randint(0,width_mult)*pixel
        geccoY= randint(0,height_mult)*pixel
    pivotX=snakeHeadX
    pivotY=snakeHeadY
    for i in range(length):
        if(direction_array[i]=="right"):
            pivotX -= pixel
        elif(direction_array[i]=="left"):
            pivotX += pixel
        elif(direction_array[i]=="up"):
            pivotY -= pixel
        elif(direction_array[i]=="down"):
            pivotY += pixel
        DISPLAYSURF.blit(snakeBodyImg, (pivotX,pivotY))
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
            direction_array.append(direction)
            del(direction_array[len(direction_array)-1])
    pygame.display.update()
    fpsClock.tick(FPS)
