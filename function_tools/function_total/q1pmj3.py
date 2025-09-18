def factor_cubic_polynomial(leading_coeff: float, real_root: float, quadratic_coeffs: tuple):
    import sympy as sp
    x = sp.symbols('x')
    quadratic_polynomial = quadratic_coeffs[0] * x**2 + quadratic_coeffs[1] * x + quadratic_coeffs[2]
    linear_factor = leading_coeff * (x - real_root)
    return linear_factor * quadratic_polynomial
