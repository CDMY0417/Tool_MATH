def factor_quadratic(expr_coeffs: tuple, known_factor: tuple):
    a, b, c = expr_coeffs
    p, q = known_factor
    other_linear_coeff = a // p
    other_constant_term = c // q
    return (other_linear_coeff, other_constant_term)
