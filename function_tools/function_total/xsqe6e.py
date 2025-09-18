def substitute_and_solve(equation: str, substitution: str):
    from sympy import sympify, solve
    expr = sympify(equation)
    substitution_expr = sympify(substitution)
    result = solve(expr.subs(substitution_expr), dict=True)
    return result
