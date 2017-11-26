import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake")

FPS = 30
fpsClock = pygame.time.Clock()
pixel = 50

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0)
blue= (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode((width,height),0,32)
snakeHeadImg = pygame.image.load('snake_head.jpg')
snakeHeadImg = pygame.transform.scale(snakeHeadImg,(pixel,pixel))
snakeX = randint(0,width-pixel)
snakeY = randint(0,height-pixel)
speed = 5
direction = 'right'

while True:
    DISPLAYSURF.fill(white)
    if(direction=='right'):
        snakeX += speed
        if(snakeX >= width-pixel):
            snakeX = pixel
        elif(direction=='left'):
            snakeX -= speed
            if(snakeX <= pixel):
                snakeX = width-pixel
        elif(direction=='top'):
            snakeY +=speed
            if(snakeY >= height-pixel):
                snakeY = pixel
        elif(direction=='bottom'):
            snakeY -= speed
            if(snakeY <=pixel):
                snakeY = height-pixel
        else:
            print "No known direction"

    DISPLAYSURF.blit(snakeHeadImg, (snakeX,snakeY))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

