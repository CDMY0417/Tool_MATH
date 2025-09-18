def expand_polynomial_product(coefficients1: tuple, coefficients2: tuple):
    (a, b, c) = coefficients1
    (d, e) = coefficients2
    x2_coeff = a * d
    x_coeff = a * e + b * d
    constant = b * e + c * d
    return (x2_coeff, x_coeff, constant)
