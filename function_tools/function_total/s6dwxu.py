def shift_polynomial_origin(polynomial: list[float], shift: float):
    from sympy import symbols, expand
    w = symbols('w')
    z = w + shift
    return expand(sum(coef * z**i for i, coef in enumerate(polynomial[::-1])))
