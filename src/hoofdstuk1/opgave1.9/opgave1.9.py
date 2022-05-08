class Rectangle:
    def __init__(self, x_co, y_co, width, height):
        self.x_co = x_co
        self.y_co = y_co
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
