def factor_and_find_real_roots(a: float, b: float, c: float, d: float):
    from sympy import symbols, Eq, solveset, S
    y = symbols('y')
    eq = Eq(a * y**3 + b * y**2 + c * y + d, 0)
    solutions = solveset(eq, y, domain=S.Reals)
    return list(solutions)
