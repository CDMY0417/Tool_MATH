def factor_quadratic(a: int, b: int, c: int):
    from sympy import symbols, factor
    x = symbols('x')
    quadratic = a * x**2 + b * x + c
    factors = factor(quadratic)
    return factors
