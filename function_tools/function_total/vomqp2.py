def expand_polynomial_product(a: float, b: float, c: float, d: float):
    return [1, a + d, b + a * d, c + b * d, c * d]
