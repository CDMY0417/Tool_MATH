def expand_polynomial_product(a: int, b: int):
    x2_coeff = b - 2 * a
    x_coeff = a**2 - 2 * a * b
    constant = a * b
    return x2_coeff, x_coeff, constant
