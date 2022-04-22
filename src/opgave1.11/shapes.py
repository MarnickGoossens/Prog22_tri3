class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        a = self.width * self.height
        return a

    def get_perimeter(self):
        p = 2 * width + 2 * height
        return p

    def get_diagonal(self):
        d = (width**2 + height**2) ** 0.5
        return d

    def get_picture(self):
        pass

    def get_amount_inside(self):
        pass


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(width=length, height=length)

    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self, length):
        self.width = length
        self.height = length

    def set_height(self, length):
        self.width = length
        self.height = length


class Diamond(Rectangle):
    pass
