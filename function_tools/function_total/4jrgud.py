def expand_quadratic_products(a: int, b: int, c: int, d: int, e: int, f: int):
    coeff_x4 = a * d
    coeff_x3 = a * e + b * d
    coeff_x2 = a * f + b * e + c * d
    coeff_x1 = b * f + c * e
    constant_term = c * f
    return (coeff_x4, coeff_x3, coeff_x2, coeff_x1, constant_term)
