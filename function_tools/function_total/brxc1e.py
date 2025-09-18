def expand_product_polynomial(constants: list[float]):
    from sympy import symbols, expand, prod
    t = symbols('t')
    expr = prod(t - c for c in constants)
    expanded_expr = expand(expr)
    return expanded_expr
