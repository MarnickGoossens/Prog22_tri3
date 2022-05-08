class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        string = f"Rectangle(width={self.width}, heigth={self.height})"
        return string

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        a = self.width * self.height
        return a

    def get_perimeter(self):
        p = 2 * self.width + 2 * self.height
        return p

    def get_diagonal(self):
        d = (self.width**2 + self.height**2) ** 0.5
        return d

    def get_picture(self):
        string = ""
        for rows in range(self.height):
            stri = f"\n" + "*" * self.width
            string += stri
        return string

    def get_amount_inside(self, shape):
        breedte = self.width // shape.width
        hoogte = self.height // shape.height
        aantal = breedte * hoogte
        if aantal == 0:
            return "Shape did not fit"
        return aantal


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def __repr__(self):
        string = f"Square(side={self.width})"
        return string

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)


class Diamond(Rectangle):
    pass
