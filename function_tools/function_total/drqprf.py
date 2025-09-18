def cross_product_3d(vector1: tuple[float, float, float], vector2: tuple[float, float, float]) -> tuple[float, float, float]:
    x1, y1, z1 = vector1
    x2, y2, z2 = vector2
    return (y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)
