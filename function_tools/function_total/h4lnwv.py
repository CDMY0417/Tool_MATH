def expand_quadratic_substitution(x_expr: str, y_expr: str):
    import sympy as sp
    x = sp.symbols('x')
    # Parse the expressions
    y_sub = sp.sympify(y_expr.replace('x', f'({x_expr})'))
    # Expand the expression
    polynomial = sp.expand(y_sub)
    return polynomial
