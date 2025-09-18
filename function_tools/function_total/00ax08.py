def factor_expression(expression: str):
    from sympy import factor, sympify
    expr = sympify(expression)
    return factor(expr)
