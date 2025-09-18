def match_coefficients(expr1_coeffs: tuple, expr2_coeffs: tuple):
    equations = []
    for a, b in zip(expr1_coeffs, expr2_coeffs):
        equations.append(a - b)
    return equations
