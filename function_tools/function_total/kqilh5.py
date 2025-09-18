def simplify_factor_quadratic(a: int, b: int, c: int):
    from sympy import symbols, factor
    x = symbols('x')
    expression = a*x**2 + b*x + c
    factors = factor(expression)
    return factors
