#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

if __name__ == '__main__':
    r = Rectangle(5, 10)
    c = Circle(3)
    print(r.area())
    print(c.area())

