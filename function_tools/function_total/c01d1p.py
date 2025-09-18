def expand_square(component: str) -> str:
    from sympy import symbols, expand
    x = symbols('x')
    expanded_expr = expand(component)
    return str(expanded_expr)
