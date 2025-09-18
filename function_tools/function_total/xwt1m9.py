def match_polynomial_coefficients(coefficients1: tuple, coefficients2: tuple):
    return [(coefficients1[i] - coefficients2[i]) for i in range(min(len(coefficients1), len(coefficients2)))]
