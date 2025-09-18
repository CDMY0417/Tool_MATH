def solve_quadratic_equation(a: float, b: float, c: float):
    import cmath
    d = b**2 - 4*a*c
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    return sol1, sol2
