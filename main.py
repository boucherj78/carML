import pygame as pg
import numpy as np
import random
from pygame.locals import *
import time
from classes import *
import cv2 as cv
from Game import *


if __name__ == '__main__':
    # # Initialize pygame
    # # car_array = cv.imread('img/parcours_1.jpg', CV_LOAD_IMAGE_GRAYSCALE)
    #
    # grid = get_grid('img/parcours_1.jpg')
    # pg.init()
    # screen = pg.display.set_mode((683, 384))
    # background = pg.image.load('img/parcours_1.jpg').convert()
    #
    # # random.seed(a=12324)
    # cars = [Car(1, 1, 1 + random.random() * 5, 1 + random.random() * 5, 'img/car.jpg')
    #         for i in range(5)]
    # dead = []
    # while cars:
    #     screen.blit(background, (0, 0))
    #     print('-------------------')
    #     temp = []
    #     for c in cars:
    #         c.update_position()
    #         c.display(screen)
    #         print(c)
    #         if not c.isdead(grid):
    #             temp.append(c)
    #
    #             c.get_distance_from_captor(grid)
    #         else:
    #             dead.append(c)
    #     cars = temp
    #     pg.display.update()
    #     pg.time.delay(1000)
    for p in parcours:
        game = Game(width= 1080,height= 720,path_background=p,path_car='img/car.jpg', nb_cars=1)
        game.main_loop()