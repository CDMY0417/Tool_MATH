def compose_rational_functions(a1: int, b1: int, c1: int, d1: int, a2: int, b2: int, c2: int, d2: int):
    numerator = a2 * a1 + b2 * c1
    denominator = a2 * b1 + b2 * d1 - c2 * a1 - d2 * c1
    return (numerator, denominator)
