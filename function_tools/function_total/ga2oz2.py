def polynomial_degree(expr: str) -> int:
    from sympy import sympify, degree
    expr_sympy = sympify(expr)
    return degree(expr_sympy)
