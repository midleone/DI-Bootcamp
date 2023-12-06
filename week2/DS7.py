
import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other_circle):
        new_radius = self.radius + other_circle.radius
        return Circle(radius=new_radius)

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __lt__(self, other_circle):
        return self.radius < other_circle.radius

    def __le__(self, other_circle):
        return self.radius <= other_circle.radius


circle1 = Circle(radius=3)
circle2 = Circle(diameter=6)

print(circle1.diameter)
print(circle2.area)
print(str(circle1))

circle3 = circle1 + circle2
print(circle3.radius)

