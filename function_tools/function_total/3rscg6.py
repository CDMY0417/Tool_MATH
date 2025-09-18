def extract_coefficient(expression: str, variables: tuple[str, ...]) -> int:
    import sympy
    expr = sympy.sympify(expression)
    term = sympy.Mul(*(sympy.symbols(var) for var in variables))
    return expr.coeff(term)
