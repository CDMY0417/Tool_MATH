def is_equilateral_triangle(vertex1: tuple[float, float], vertex2: tuple[float, float], vertex3: tuple[float, float]) -> bool:
    from math import dist
    side1 = dist(vertex1, vertex2)
    side2 = dist(vertex2, vertex3)
    side3 = dist(vertex3, vertex1)
    return side1 == side2 == side3
