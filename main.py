import pygame as pg
import numpy as np
import random
from pygame.locals import *
import time
from classes import *
import cv2 as cv

SCREENRECT = pg.Rect(0, 0, 683, 384)

def get_grid(img):
    im_gray = cv.imread(img, cv.IMREAD_GRAYSCALE)
    im_bw = cv.threshold(im_gray, 127, 255, cv.THRESH_BINARY)[1]
    return im_bw


if __name__ == '__main__':
    # Initialize pygame
    # car_array = cv.imread('img/parcours_1.jpg', CV_LOAD_IMAGE_GRAYSCALE)

    grid = get_grid('img/parcours_1.jpg')
    pg.init()
    screen = pg.display.set_mode((683, 384))
    background = pg.image.load('img/parcours_1.jpg').convert()

    random.seed(a=2324)
    cars = [Car(random.randint(0, 300), random.randint(0, 150), 1 + random.random() * 2, 1 + random.random() * 2, 'img/car.jpg')
            for i in range(5)]
    dead = []
    while True:
        screen.blit(background, (0, 0))
        print('-------------------')
        temp = []
        for c in cars:
            c.move()
            c.display(screen)
            if not c.isdead(grid):
                temp.append(c)
                print(c)
                c.get_distance_from_captor(grid)
            else:
                dead.append(c)
        cars = temp
        pg.display.update()
        pg.time.delay(1000)
