def distributive_multiplication(coefficients: tuple, monomial: int):
    return tuple(coef * monomial for coef in coefficients)
