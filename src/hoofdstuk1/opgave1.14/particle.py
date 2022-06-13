from random import random


class Particle:
    # Init of particle class
    def __init__(self, max_speed):
        self.pos_x = 0
        self.pos_y = 0
        self.color = (255, 255, 255)

        self.max_speed = max_speed
        self.speed_x = self.max_speed * (2 * random() - 1)
        self.speed_y = self.max_speed * (2 * random() - 1)

    # Update the x and y position of a particle based on it's x and y speed
    def update(self, interval):
        pass

    # Checks if the paramters of a particle need to be reset
    # This can be done by calling the __init__ method of the particle
    def reset(self):
        pass

    # Change the color of the particle depending on certain variables
    def set_color(self):
        pass


class Boring(Particle):
    def __init__(self, max_speed):
        Particle.__init__(self, max_speed)

    def update(self, interval):
        self.pos_x += self.speed_x * interval
        self.pos_y += self.speed_y * interval

    def reset(self):
        if self.pos_x < -1 or self.pos_y < -1:
            self.__init__(self.max_speed)
        if self.pos_x > 1 or self.pos_y > 1:
            self.__init__(self.max_speed)


class Bouncing(Particle):
    def __init__(self, max_speed):
        Particle.__init__(self, max_speed)

    def update(self, interval):
        self.pos_x += self.speed_x * interval
        self.pos_y += self.speed_y * interval

    def reset(self):
        if self.pos_x < -1 or self.pos_x > 1:
            self.speed_x *= -1
        if self.pos_y < -1 or self.pos_y > 1:
            self.speed_y *= -1

    def set_color(self):
        pass
