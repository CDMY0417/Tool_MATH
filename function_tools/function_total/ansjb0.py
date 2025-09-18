def cross_product(vec1: tuple, vec2: tuple) -> tuple:
    x1, y1, z1 = vec1
    x2, y2, z2 = vec2
    return (y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2)
