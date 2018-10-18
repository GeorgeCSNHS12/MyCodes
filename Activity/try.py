import math

# class Point:

#     def __init__ ( self , x = 0.0, y = 0.0):
#         self.x = x
#         self.y = y
#     def __str__ (self):
#         return "({},{})".format(self.x, self.y)

# p = Point(y=2,x=3)


class Point2D:

    def __init__ ( self , x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __eq__ ( self, p):
        return self.x == p.x and self.y == p.y
    def distance (self):
        d = math.sqrt(self.x**2 + self.y**2)
        return d

p = Point2D(1,2)
q = Point2D(1,2)
r = p

print(p is q)
print(p is r)
print(p == q)
print(p == r)