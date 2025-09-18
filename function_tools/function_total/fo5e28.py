def factor_quadratic(a: int, b: int, c: int):
    from sympy import symbols, factor
    x = symbols('x')
    expr = a*x**2 + b*x + c
    return factor(expr)
