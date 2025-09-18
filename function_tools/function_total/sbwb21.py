def expand_polynomial_product(coeffs1: tuple, coeffs2: tuple):
    a, b, c = coeffs1
    d, e = coeffs2
    return (a * d, a * e + b * d, b * e + c * d, c * e)
