pi = 3.14


def areaTriangulo(a, b):
    if b <= 0 or a <= 0:
        return -1
    return b * a ** 2


def areaCirculo(r):
    if r <= 0:
        return -1
    return pi * r ** 2


def areaQuadrado(ld1, ld2 = None):
    if ld1 <= 0 or ld2 <= 0:
        return -1
    if ld2 is None:
        return ld1 * ld1
    return ld1 * ld2
