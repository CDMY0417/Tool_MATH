def subtract_polynomials(p1: str, p2: str) -> str:
    from sympy import simplify
    return str(simplify(f'({p1}) - ({p2})'))
