def subtract_terms(expr1: str, expr2: str) -> str:
    import sympy as sp
    e1 = sp.sympify(expr1)
    e2 = sp.sympify(expr2)
    result = e1 - e2
    return str(result)
