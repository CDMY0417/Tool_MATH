def valid_triangle_sides(sides: list[float]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c
