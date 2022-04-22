from math import pi


class shape:
    def __init__(self, x_co, y_co):
        self.x_co = x_co
        self.y_co = y_co

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(shape):
    def __init__(self, x_co, y_co, straal):
        super().__init__(x_co, y_co)
        self.straal = straal

    def area(self):
        a = (self.straal**2) * pi
        return a

    def perimeter(self):
        r = 2 * pi * self.straal
        return r


class Rectangle(shape):
    def __init__(self, x_co, y_co, width, height):
        super().__init__(x_co, y_co)
        self.width = width
        self.height = height

    def area(self):
        a = self.width * self.height
        return a

    def perimeter(self):
        r = (self.width + self.height) * 2
        return r

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
