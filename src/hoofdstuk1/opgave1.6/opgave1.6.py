class safe(RuntimeError):
    pass


class Rectangle:
    def __init__(self, width, height, point):
        if width > 0:
            self.width = width
        else:
            raise safe("breedte is negatief")
        if width > 0:
            self.height = height
        else:
            raise safe("hoogte is negatief")
        self.point = point

    def __repr__(self):
        string = f"({self.point.x}, {self.point.y}): {self.width} x {self.height}"
        return string

    def omtrek(self):
        o = 2 * (self.width + self.height)
        return o

    def oppervlakte(self):
        return self.width * self.height

    def rechteronderhoek(self):
        self.point.x += self.width
        self.point.y -= self.height


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def call(self):
        string = f"x: {self.x}, y: {self.y}"
        return string
