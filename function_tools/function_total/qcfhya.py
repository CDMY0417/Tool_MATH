def simplify_expression(expression: str) -> str:
    import sympy as sp
    simplified = sp.simplify(expression)
    return str(simplified)
