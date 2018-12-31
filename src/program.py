from src.vector import Vector


def main():
    v1 = Vector([-0.221, 7.437])
    print(v1.magnitude())

    v2 = Vector([8.813, -1.331, -6.247])
    print(v2.magnitude())

    v3 = Vector([5.581, -2.136])
    print(v3.normalize())

    v4 = Vector([1.996, 3.108, -4.554])
    print(v4.normalize())


if __name__ == '__main__':
    main()

