import numbers
from functools import reduce
from math import sqrt, acos, degrees
from decimal import Decimal


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    # + overloading
    def __add__(self, other):
        self.__assert_equal_dimension(other)
        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)])

    # - overloading
    def __sub__(self, other):
        self.__assert_equal_dimension(other)
        return Vector([x-y for x,y in zip(self.coordinates, other.coordinates)])

    # * overloading
    def __mul__(self, other):

        if isinstance(other, numbers.Number):
            return Vector([x * Decimal(other) for x in self.coordinates])

        else:
            raise TypeError("Unsupported type: {}".format(type(other)).__name__)

    # private: check for equal dimensions
    def __assert_equal_dimension(self, other: 'Vector'):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions of unequal length: {} vs {}".format(self.dimension, other.dimension))

    # magnitude of the vector
    def magnitude(self):
        total = reduce((lambda x,y: x + y ** 2), self.coordinates, 0)
        return Decimal(sqrt(total))

    # finds unit vector in same direction as this vector
    def normalize(self):
        try:
            return self * (1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    # finds dot product of two vectors
    def dot_product(self, other: 'Vector'):
        self.__assert_equal_dimension(other)
        return sum([x*y for x, y in zip(self.coordinates, other.coordinates)])

    # finds angle between two vectors
    def angle_radians(self, other: 'Vector'):
        return acos(self.dot_product(other) / (self.magnitude() * other.magnitude()))

    def angle_degrees(self, other: 'Vector'):
        return degrees(self.angle_radians(other))
