def not_valid_triangle(sides: tuple) -> bool:
    a, b, c = sorted(sides)
    return a + b <= c
