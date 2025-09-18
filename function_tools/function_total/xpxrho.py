def gcd_polynomial(p1: str, p2: str):
    import sympy as sp
    a = sp.symbols('a')
    poly1 = sp.sympify(p1)
    poly2 = sp.sympify(p2)
    return sp.gcd(poly1, poly2)
