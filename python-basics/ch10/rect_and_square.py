class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        self.length = side_length
        self.width = side_length

r = Rectangle(1.0, 2.0)
s = Square(2.0)

print(r.area(), s.area())