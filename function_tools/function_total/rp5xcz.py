def vieta_sum_of_roots(coefficients: list):
    # The sum of the roots for a polynomial a_n*x^n + ... + a_1*x + a_0 = 0
    # is given by -a_(n-1)/a_n according to Vieta's formulas
    if len(coefficients) < 2:
        return 0
    return -coefficients[-2] / coefficients[-1]
