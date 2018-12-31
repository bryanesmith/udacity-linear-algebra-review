import unittest
from src.vector import Vector


class TestVector(unittest.TestCase):

    def __almostEqual(self, vec1, vec2):
        self.assertEqual(len(vec1), len(vec2))
        for idx in range(0, len(vec1)):
            self.assertAlmostEqual(vec1[idx], vec2[idx])

    def test_add(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])
        v3 = v1 + v2
        self.__almostEqual(v3.coordinates, [7.089, -7.23])

    def test_subtract(self):
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])
        v3 = v1 - v2
        self.__almostEqual(v3.coordinates, [15.342, 7.337])

    def test_multiply_scalar(self):
        v1 = Vector([1.671, -1.012, -0.318]) * 7.41
        self.__almostEqual(v1.coordinates, [12.38211, -7.49892, -2.35638])


if __name__ == '__main__':
    unittest.main()