def expand_to_polynomial(roots: list[float]) -> sp.Expr:
    import sympy as sp
    x = sp.symbols('x')
    polynomial = 1
    for root in roots:
        polynomial *= (x - root)
    return sp.expand(polynomial)
