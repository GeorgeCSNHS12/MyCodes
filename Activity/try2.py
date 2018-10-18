# import random

# class Point3D:

#     def __init__ ( self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#     def __str__ (self):
#         return "({},{})".format(self.x, self.y)
#     def __add__ (self, q):
#         some = Point3D(self.x + q.x, self.y + q.y)
#         return some

# p = Point3D(3, 4)
# q = Point3D(1, 2)

# print(p + q)

class Person:
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__ (self):
        return "{} {}".format(self.firstname, self.lastname)

class Student(Person):

    def __init__(self, firstname="", lastname="", school = ""):
        super().__init__(firstname, lastname)
        self.school = school
    
    def __str__(self):
        return "{}, [{}]".format(super().__str__(), self.school)

george = Student("George William", "Sison", "CAMHI")
print()

if __name__ == "__main__":

    george = Person("George William", "Sison")
    print(george)