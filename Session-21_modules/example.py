# module = a file containing code you want to include in your program
#          useful to break large program reusable seperate files

# print(help("modules"))

import math as m
# from math import pi

# print(m.pi)
# print(m.e)

def square(x):
    return x**2
def cube(x):
    return x**3
def circumference(radius):
    return 2*m.pi*radius
def areaOfCircle(radius):
    return m.pi*radius**2
