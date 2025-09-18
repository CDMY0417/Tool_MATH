def is_pythagorean_triple(sides: tuple[int, int, int]) -> bool:
    a, b, c = sorted(sides)
    return a * a + b * b == c * c
