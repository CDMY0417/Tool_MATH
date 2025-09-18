def match_coefficients(coefficients1: tuple, coefficients2: tuple):
    equations = []
    for c1, c2 in zip(coefficients1, coefficients2):
        equations.append(c1 == c2)
    return equations
