import pygame as pg
import numpy as np
import random
from pygame.locals import *
import time
from classes import *

SCREENRECT = pg.Rect(0, 0, 640, 480)

if __name__ == '__main__':
    # Initialize pygame

    pg.init()
    screen = pg.display.set_mode((640, 480))

    random.seed(a=55555)
    cars = [Car(random.randint(0,640),random.randint(0,480),random.random()*2,random.random()*2) for i in range(5)]
    for c in cars:
        c.display()

    time.sleep(5)

screen = pygame.display.set_mode((640, 480))
    >> > player = pygame.image.load('player.bmp').convert()
    >> > background = pygame.image.load('background.bmp').convert()
    >> > screen.blit(background, (0, 0))
    >> > objects = []
    >> > for x in range(10):  # create 10 objects</i>
        ...
        o = GameObject(player, x * 40, x)
    ...
    objects.append(o)
    >> > while 1:
        ...
        for event in pygame.event.get():
            ...
        if event.type in (QUIT, KEYDOWN):
            ...
        sys.exit()
    ...
    for o in objects:
        ...
        screen.blit(background, o.pos, o.pos)
    ...
    for o in objects:
        ...
        o.move()
    ...
    screen.blit(o.image, o.pos)
    ...
    pygame.display.update()
    ...
    pygame.time.delay(100)


