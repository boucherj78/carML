class Vector(object):
    def __init__(self, x, y, int=False):
        self.x = x
        self.y = y

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def reset(self,vec):
        self.x = vec.x
        self.y = vec.y

    def multiply(self,vec):
        self.x *= vec.x
        self.y *= vec.y

class Captor(Vector):
    def __init__(self,  x, y, length=1):
        super().__init__(x, y)
        self.length = length

    def get_distance(self):
        return None


class Car(object):

    def __init__(self, x, y, vx, vy):
        self.speed = Vector(x, y)
        self.position = Vector(vx, vy)
        self.size = 50
        self.captors = [Captor(-1, 0), Captor(-1, 1), Captor(0, 1), Captor(1, 1), Captor(1, 0)]

    def get_distance_from_captor(self):
        if isinstance(self.captors, list):
            return [c.get_distance() for c in self.captors]
        else:
            return [self.captors.get_distance()]


    def display(self):
        pass

    def move(self):
        self.position.add(self.speed)

