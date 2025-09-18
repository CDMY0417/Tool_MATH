def simplify_polynomial_expression(expr1: str, expr2: str) -> str:
    from sympy import simplify
    result = simplify(expr1 + '-' + expr2)
    return str(result)
