import pygame as pg
from utils import *


class Vector(object):
    def __init__(self, x, y, integer=False):
        if integer:
            self.x = int(x)
            self.y = int(y)
        else:
            self.x = x
            self.y = y
        self.integer = integer

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
        if self.integer:
            self.x = int(self.x)
            self.y = int(self.y)

    def reset(self, vec = None):
        if vec is not None:
            self.x = vec.x
            self.y = vec.y
            if self.integer:
                self.x = int(self.x)
                self.y = int(self.y)
        else:
            self.x = 0
            self.y = 0

    def multiply(self, num):
        self.x *= num
        self.y *= num
        if self.integer:
            self.x = int(self.x)
            self.y = int(self.y)


class Captor(Vector):
    def __init__(self, x, y, length=20):
        super().__init__(x, y)
        self.length = length

    def get_distance(self, car, grid):
        """
        :param car:
        :param grid:
        :return: True when obstacle else false
        """
        x_end_cap = int(car.position.x + self.x * self.length)
        y_end_cap = int(car.position.y + self.y * self.length)
        return True if not grid[y_end_cap][x_end_cap] else False


class Car(object):

    def __init__(self, x, y, vx, vy, img):
        self.accel = Vector(0, 0)
        self.speed = Vector(vx, vy)
        self.position = Vector(x, y, True)
        self.size = 15
        self.friction = 0.8
        self._accel_sensible = 3
        self.captors = [Captor(-1, 0), Captor(-1, 1), Captor(0, 1), Captor(1, 1), Captor(1, 0), Captor(1, -1),
                        Captor(0, -1), Captor(-1, -1)]
        self.distance_captor = None
        if isinstance(img, str):
            self.surface = pg.image.load(img).convert()

    def get_distance_from_captor(self, grid):
        if isinstance(self.captors, list):
            self.distance_captor = [c.get_distance(self, grid) for c in self.captors]
        else:
            self.distance_captor = [self.captors.get_distance(self, grid)]
        return self.distance_captor

    def display(self, screen):
        screen.blit(self.surface, (self.position.x, self.position.y))

    def update_position(self):
        self.position.add(self.speed)

    def update_speed(self):
        self.speed.add(self.accel)

    def speed_friction(self):
        self.speed.multiply(self.friction)

    def update_accel(self, direction):
        if direction <= 80:
            print(" turn ")
            self.accel.add(Vector(x=(direction-79.5)*-2, y=0))
        else:
            print(" accel ")
            self.accel.add(Vector(x=0, y=(direction-81.5)*-2))
        self.accel.multiply(self._accel_sensible)

    def stop_accel(self):
        self.accel.reset()

    def isdead(self, grid):
        return True if not (grid[int(self.position.y)][int(self.position.x)]
                            and grid[int(self.position.y + self.size)][int(self.position.x)]
                            and grid[int(self.position.y)][int(self.position.x + self.size)]
                            and grid[int(self.position.y + self.size)][int(self.position.x + self.size)])\
            else False


    def __str__(self):
        return f"""POS : ({self.position.x}, {self.position.y}) // SPE: ({self.speed.x}, {self.speed.y}) //  ACC: ({self.accel.x}, {self.accel.y})D_C: {self.distance_captor}"""
