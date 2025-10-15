import math


def square(side):
    area = side ** 2
    if type(side) is float or side % 1 != 0:
        return math.ceil(area)
    else:
        return int(area)


print("Площадь квадрата со сторойной 4.2: ", square(4.2))
