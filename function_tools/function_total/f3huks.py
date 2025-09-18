def factor_out_term(expr: str, term: str):
    from sympy import symbols, factor
    x = symbols(term)
    factored_expr = factor(expr, x)
    return factored_expr
