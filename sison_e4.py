# filename      : sison_e4.py
# author        : George William Sison
# description   : This is a python program that prints an Area and Perimeter
#                 of a Triangle.

from Exercise.geometry import triangle_perimeter
from Exercise.geometry import triangle_heronsarea

inputtedNumbers = input("\nEnter the side lengths of a triangle : ")

sides = str(inputtedNumbers).split(",")

perimeter = (triangle_perimeter(float(sides[0]), float(sides[1]), float(sides[2]))) * 2
area = triangle_heronsarea(float(sides[0]), float(sides[1]), float(sides[2]))

print("Perimeter : {:.2f}".format(perimeter))
print("Area : {:.2f}\n".format(area))