def factor_polynomial(poly: str):
    from sympy import factor, symbols
    x = symbols('x')
    return factor(poly)
