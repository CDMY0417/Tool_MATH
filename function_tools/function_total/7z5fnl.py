import sympy as sp

def solve_cubic_equation(a: int, b: int, c: int, d: int) -> list:
    x = sp.symbols('x')
    polynomial = a * x**3 + b * x**2 + c * x + d
    roots = sp.solve(polynomial, x)
    real_roots = [r.evalf() for r in roots if r.is_real]
    return real_roots
