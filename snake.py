import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
pixel = 30
width_mult, height_mult = 40, 20
width, height = pixel*width_mult, pixel*height_mult

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
for i in range(length-1):
    direction_array.append(direction)

while True:
    DISPLAYSURF.fill(white)
#    print snakeHeadX,snakeHeadY
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
        geccoX= randint(2,width_mult-2)*pixel
        geccoY= randint(2,height_mult-2)*pixel
#        print geccoY,geccoX
        score += 1
        direction_array.append(direction)
    pivotX=snakeHeadX
    pivotY=snakeHeadY
    for i in range(length-1):
        if(direction_array[i]=='right'):
            pivotX -= pixel
        elif(direction_array[i]=='left'):
            pivotX += pixel
        elif(direction_array[i]=='up'):
            pivotY += pixel
        elif(direction_array[i]=='down'):
            pivotY -= pixel
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
    direction_array=direction_array[::-1]
    direction_array.append(direction)
    direction_array=direction_array[::-1]
    del(direction_array[len(direction_array)-1])
    pygame.display.update()
    fpsClock.tick(FPS)


