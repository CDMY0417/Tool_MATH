def simplify_polynomial(expression: str):
    from sympy import simplify
    simplified_expr = simplify(expression)
    return str(simplified_expr)
