from decimal import Decimal
from functools import reduce
from math import acos, degrees
from numbers import Number


class Vector(object):

    def __init__(self, coordinates: [Number]):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self) -> str:
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v: 'Vector') -> bool:
        return self.coordinates == v.coordinates

    # + overloading
    def __add__(self, other: 'Vector') -> 'Vector':
        self.__assert_equal_dimension(other)
        return Vector([x+y for x, y in zip(self.coordinates, other.coordinates)])

    # - overloading
    def __sub__(self, other: 'Vector') -> 'Vector':
        self.__assert_equal_dimension(other)
        return Vector([x-y for x, y in zip(self.coordinates, other.coordinates)])

    # * overloading
    def __mul__(self, other) -> 'Vector':

        if isinstance(other, Number):
            return Vector([x * Decimal(other) for x in self.coordinates])

        else:
            raise TypeError("Unsupported type: {}".format(type(other)).__name__)

    # private: check for equal dimensions
    def __assert_equal_dimension(self, other: 'Vector'):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions of unequal length: {} vs {}".format(self.dimension, other.dimension))

    # magnitude of the vector
    def magnitude(self) -> Decimal:
        total = reduce((lambda x, y: Decimal(x + y ** 2)), self.coordinates, 0)
        return total.sqrt()

    # finds unit vector in same direction as this vector
    def normalize(self) -> 'Vector':
        try:
            return self * (1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    # finds dot product of two vectors
    def dot_product(self, other: 'Vector') -> Decimal:
        self.__assert_equal_dimension(other)
        return sum([x*y for x, y in zip(self.coordinates, other.coordinates)])

    # finds angle in radians between two vectors
    def angle_radians(self, other: 'Vector') -> Decimal:
        return Decimal(acos(self.dot_product(other) / (self.magnitude() * other.magnitude())))

    # finds angle in degrees between two vectors
    def angle_degrees(self, other: 'Vector') -> Decimal:
        return Decimal(degrees(self.angle_radians(other)))

    # returns whether or not two vectors are parallel
    def is_parallel(self, other: 'Vector', precision=1e-10) -> bool:
        diff = self.dot_product(other).copy_abs() - (self.magnitude() * other.magnitude()).copy_abs()
        return diff.copy_abs() < precision

    # returns whether or not two vectors are orthogonal (right angles)
    def is_orthogonal(self, other: 'Vector', precision=1e-10) -> bool:
        return self.dot_product(other).copy_abs() < precision

    # Finds projection of other vector on this vector
    def projection_of(self, other: 'Vector') -> 'Vector':
        return self.normalize() * other.dot_product(self.normalize())

    # Finds the orthogonal component of another vector relative to this vector
    #   (this component is orthogonal to the project, and with the other vector form a right triangle)
    def orthogonal_component_of(self, other: 'Vector') -> 'Vector':
        return other - self.projection_of(other)