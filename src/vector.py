import numbers


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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

        if self.dimension != other.dimension:
            raise ValueError("Dimensions of unequal length")

        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)])

    # - overloading
    def __sub__(self, other):

        if self.dimension != other.dimension:
            raise ValueError("Dimensions of unequal length")

        return Vector([x-y for x,y in zip(self.coordinates, other.coordinates)])

    # * overloading
    def __mul__(self, other):

        if isinstance(other, numbers.Number):
            return Vector([x * other for x in self.coordinates])

        else:
            raise TypeError("Unsupported type: {}".format(type(other)).__name__)
