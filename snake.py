import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
pixel = 30
width_mult, height_mult = 40, 20
width, height = pixel*width_mult, pixel*height_mult
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake")

FPS = pixel
fpsClock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0)
blue= (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode((width,height))
snakeHeadImgLeft = pygame.image.load('snake-head-left.png')
snakeHeadImgLeft = pygame.transform.scale(snakeHeadImgLeft,(pixel,pixel))
snakeHeadImgRight = pygame.transform.flip(snakeHeadImgLeft,1,0)
snakeHeadImgDown =  pygame.transform.rotate(snakeHeadImgLeft,90)
snakeHeadImgUp =  pygame.transform.rotate(snakeHeadImgLeft,270)

snakeHeadImg = snakeHeadImgRight
snakeX = randint(0,width_mult)*pixel
snakeY = randint(0,height_mult)*pixel

geccoImg = pygame.image.load('small-gecco.jpg')
geccoImg = pygame.transform.scale(geccoImg,(pixel,pixel))
geccoX= randint(0,width-pixel)
geccoY= randint(0,height-pixel)

low = pixel * 0.2
mid = pixel * 0.4
high = pixel * 0.6
speed = low
direction = 'right'

while True:
    DISPLAYSURF.fill(red)
    if(direction == 'right'):
        snakeX += speed
        if(snakeX >= width-pixel):
            snakeX = pixel
    elif(direction == 'left'):
        snakeX -= speed
        if(snakeX <= pixel):
            snakeX = width-pixel
    elif(direction == 'up'):
        snakeY -=speed
        if(snakeY <= pixel):
            snakeY = height-pixel
    elif(direction == 'down'):
        snakeY += speed
        if(snakeY >= height-pixel):
            snakeY = pixel
    # keys=pygame.key.get_pressed()
    # if keys[K_RIGHT]:
    #     snakeX += speed
    #     if(snakeX >= width-pixel):
    #         snakeX = pixel
    # elif keys[K_LEFT]:
    #     snakeX -= speed
    #     if(snakeX <= pixel):
    #         snakeX = width-pixel
    # elif keys[K_UP]:
    #     snakeY -=speed
    #     if(snakeY <= pixel):
    #         snakeY = height-pixel
    # elif keys[K_DOWN]:
    #     snakeY += speed
    #     if(snakeY >= height-pixel):
    #         snakeY = pixel

    DISPLAYSURF.blit(snakeHeadImg, (snakeX,snakeY))
    DISPLAYSURF.blit(geccoImg, (geccoX,geccoY))
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
    pygame.display.update()
    fpsClock.tick(FPS)



