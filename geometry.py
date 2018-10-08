import math

side = 0
def triangle_perimeter (a, b, c):
    return float((a + b + c) / 2)
def triangle_heronsarea (a, b, c):
    side = triangle_perimeter(a, b, c)
    return math.sqrt(side * (side - a) * (side - b) * (side - c))
