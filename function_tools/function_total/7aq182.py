def factor_polynomial(a: int, b: int, c: int):
    from sympy import symbols, factor
    x = symbols('x')
    polynomial = a*x**2 + b*x + c
    return factor(polynomial)
