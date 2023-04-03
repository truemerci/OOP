class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return f"Figure: {self.name}, Color: {self.color}"


class Rectangle(Shape):
    def __init__(self, name, color, width, length):
        super().__init__(name, color)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def __str__(self):
        return f"Figure: {self.name}, color: {self.color}, width: {self.width}, length: {self.length}"


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return f"Figure: {self.name}, color: {self.color}, radius: {self.radius}"


class Square(Shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Figure: {self.name}, color: {self.color}, side: {self.side}"


rectangle = Rectangle("Rectangle", "red", 5, 10)
circle = Circle("Circle", "blue", 3)
square = Square("Square", "green", 4)

print(f"{rectangle}, area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
print(f"{circle}, area: {circle.area()}, perimeter: {circle.perimeter()}")
print(f"{square}, area: {square.area()}, perimeter: {square.perimeter()}")
