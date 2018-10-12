from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi


if __name__ == "__main__":
    c = Circle(5.0)
    print("圆的面积是：", c.area())
