def substitute_and_expand(polynomial: str, substitution: str):
    from sympy import expand, symbols
    y = symbols('y')
    expr = expand(polynomial.replace('x', substitution))
    return expr
