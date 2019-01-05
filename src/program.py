from src.vector import Vector


def main():
    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])
    print(v1.dot_product(v2))

    v3 = Vector([-5.955, -4.904, -1.874])
    v4 = Vector([-4.496, -8.755, 7.103])
    print(v3.dot_product(v4))

    v5 = Vector([3.183, -7.627])
    v6 = Vector([-2.668, 5.319])
    print(v5.angle_radians(v6))

    v7 = Vector([7.35, 0.221, 5.188])
    v8 = Vector([2.751, 8.259, 3.985])
    print(v7.angle_degrees(v8))

if __name__ == '__main__':
    main()

