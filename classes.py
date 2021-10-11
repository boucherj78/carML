import pygame as pg


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

    def reset(self, vec):
        self.x = vec.x
        self.y = vec.y
        if self.integer:
            self.x = int(self.x)
            self.y = int(self.y)

    def multiply(self, vec):
        self.x *= vec.x
        self.y *= vec.y
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
        self.speed = Vector(vx, vy)
        self.position = Vector(x, y, True)
        self.size = 50
        self.captors = [Captor(-1, 0), Captor(-1, 1), Captor(0, 1), Captor(1, 1), Captor(1, 0), Captor(1, -1),
                        Captor(0, -1), Captor(-1, -1)]
        self.distance_captor = None
        if isinstance(img, str):
            self.surface = pg.image.load(img).convert()

    def get_distance_from_captor(self, grid):
        if isinstance(self.captors, list):
            self.distance_captor = [c.get_distance(self,grid) for c in self.captors]
        else:
            self.distance_captor = [self.captors.get_distance(self, grid)]
        return self.distance_captor

    def display(self, screen):
        screen.blit(self.surface, (self.position.x, self.position.y))

    def move(self):
        self.position.add(self.speed)

    def isdead(self, grid):
        return True if not grid[int(self.position.y)][int(self.position.x)] else False

    def __str__(self):
        return f"""POS : ({self.position.x}, {self.position.y}) // SPE: ({self.speed.x}, {self.speed.y}) // D_C: {self.distance_captor}"""
