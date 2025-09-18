def simplify_fraction(numerator: float, denominator: float):
    import sympy as sp
    frac = sp.Rational(numerator, denominator)
    return frac
