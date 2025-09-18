def find_oblique_asymptote(numerator: str, denominator: str):
    from sympy import symbols, div, sympify
    x = symbols('x')
    num_expr, denom_expr = sympify(numerator), sympify(denominator)
    quotient, _ = div(num_expr, denom_expr)
    if quotient.as_poly().degree() == 1:
        return quotient
    return None
