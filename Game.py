import pygame as pg
from classes import *
from utils import *
import random


class Game(object):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        pg.init()
        try:
            self.screen = pg.display.set_mode((kwargs['width'], kwargs['height']))
            self.grid = get_grid(kwargs['path_background'])
            self.background = pg.image.load(kwargs['path_background']).convert()
            self.cars = [Car(1, 1, 0, 0, kwargs['path_car'])
                         for i in range(kwargs['nb_cars'])]

        except KeyError as e:
            print(f"Argument not defined : {e}")
            raise

        try:
            self.sleep_time = kwargs['sleep_time']
        except KeyError:
            self.sleep_time = 100
        print(self.sleep_time)

    def main_loop(self):
        dead = []
        while self.cars:
            self.screen.blit(self.background, (0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == pg.MOUSEBUTTONDOWN:
                    return

                if event.type == pg.KEYDOWN:
                    if event.scancode in (UPARROWCODE, LEFTARROWCODE, DOWNARROWCODE, RIGHTARROWCODE):
                        print(event.scancode)
                        # print(event.scancode)
                        self.cars[0].update_accel(event.scancode)
                if event.type == pg.KEYUP:
                    self.cars[0].stop_accel()
            print('-------------------')
            temp = []
            for c in self.cars:
                c.update_speed()
                c.speed_friction()
                c.update_position()
                c.display(self.screen)
                print(c)
                if not c.isdead(self.grid):
                    temp.append(c)

                    c.get_distance_from_captor(self.grid)
                else:
                    dead.append(c)
            self.cars = temp
            pg.display.update()
            pg.time.delay(self.sleep_time)
