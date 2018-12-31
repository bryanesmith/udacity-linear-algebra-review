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

    def test_magnitude_1(self):
        v1 = Vector([-0.221, 7.437])
        self.assertAlmostEquals(v1.magnitude(), 7.440282924728065)

    def test_magnitude_2(self):
        v1 = Vector([8.813, -1.331, -6.247])
        self.assertAlmostEquals(v1.magnitude(), 10.884187567292289)

    def test_normalize_1(self):
        v1 = Vector([5.581, -2.136])
        self.__almostEqual(v1.normalize().coordinates, [0.9339352140866403, -0.35744232526233])

    def test_normalize_2(self):
        v1 = Vector([1.996, 3.108, -4.554])
        self.__almostEqual(v1.normalize().coordinates, [0.3404012959433014, 0.5300437012984873, -0.7766470449528029])


if __name__ == '__main__':
    unittest.main()