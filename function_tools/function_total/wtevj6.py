def solve_quadratic_equation(a: float, b: float, c: float):
    disc = b**2 - 4*a*c
    x1 = (-b + disc**0.5) / (2*a)
    x2 = (-b - disc**0.5) / (2*a)
    return x1, x2
