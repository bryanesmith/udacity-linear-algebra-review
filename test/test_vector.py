import unittest
from src.vector import Vector
from decimal import Decimal


# Helper method
def arr2dec(arr):
    return [Decimal(x) for x in arr]


class TestVector(unittest.TestCase):

    # Helper method
    def assertVectorsAlmostEqual(self, vec1, vec2):
        self.assertEqual(len(vec1), len(vec2))
        for idx in range(0, len(vec1)):
            self.assertAlmostEqual(vec1[idx], vec2[idx])

    def test_add(self):
        v1 = Vector([8.218, -9.341])
        v2 = Vector([-1.129, 2.111])
        v3 = v1 + v2
        self.assertVectorsAlmostEqual(v3.coordinates, arr2dec([7.089, -7.23]))

    def test_subtract(self):
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])
        v3 = v1 - v2
        self.assertVectorsAlmostEqual(v3.coordinates, arr2dec([15.342, 7.337]))

    def test_multiply_scalar(self):
        v1 = Vector([1.671, -1.012, -0.318]) * 7.41
        self.assertVectorsAlmostEqual(v1.coordinates, arr2dec([12.38211, -7.49892, -2.35638]))

    def test_magnitude(self):
        v1 = Vector([-0.221, 7.437])
        self.assertAlmostEqual(v1.magnitude(), Decimal(7.440282924728065))

        v2 = Vector([8.813, -1.331, -6.247])
        self.assertAlmostEqual(v2.magnitude(), Decimal(10.884187567292289))

    def test_normalize(self):
        v1 = Vector([5.581, -2.136])
        self.assertVectorsAlmostEqual(v1.normalize().coordinates, arr2dec([0.9339352140866403, -0.35744232526233]))

        v2 = Vector([1.996, 3.108, -4.554])
        self.assertVectorsAlmostEqual(v2.normalize().coordinates, arr2dec([0.3404012959433014, 0.5300437012984873, -0.7766470449528029]))

    def test_dot_product(self):
        v1 = Vector([7.887, 4.138])
        v2 = Vector([-8.802, 6.776])
        self.assertAlmostEqual(v1.dot_product(v2), Decimal(-41.382286))

        v3 = Vector([-5.955, -4.904, -1.874])
        v4 = Vector([-4.496, -8.755, 7.103])
        self.assertAlmostEqual(v3.dot_product(v4), Decimal(56.397178000000004))

    def test_angle_radians(self):
        v5 = Vector([3.183, -7.627])
        v6 = Vector([-2.668, 5.319])
        self.assertAlmostEqual(v5.angle_radians(v6), Decimal(3.0720263098372476))

    def test_angle_degress(self):
        v7 = Vector([7.35, 0.221, 5.188])
        v8 = Vector([2.751, 8.259, 3.985])
        self.assertAlmostEqual(v7.angle_degrees(v8), Decimal(60.27581120523091))

    def test_parallel(self):
        self.assertTrue(Vector([-7.579, -7.88]).is_parallel(Vector([22.737,23.64])))
        self.assertFalse(Vector([-2.029, 9.97, 4.172]).is_parallel(Vector([-9.231, -6.639, -7.245])))
        self.assertFalse(Vector([-2.328, -7.284, -1.214]).is_parallel(Vector([-1.821, 1.072, -2.94])))
        self.assertTrue(Vector([2.18, 4.827]).is_parallel(Vector([0,0])))

    def test_orthogonal(self):
        self.assertFalse(Vector([-7.579, -7.88]).is_orthogonal(Vector([22.737,23.64])))
        self.assertFalse(Vector([-2.029, 9.97, 4.172]).is_orthogonal(Vector([-9.231, -6.639, -7.245])))
        self.assertTrue(Vector([-2.328, -7.284, -1.214]).is_orthogonal(Vector([-1.821, 1.072, -2.94])))
        self.assertTrue(Vector([2.18, 4.827]).is_orthogonal(Vector([0,0])))


if __name__ == '__main__':
    unittest.main()