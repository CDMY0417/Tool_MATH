def quadratic_formula(a: float, b: float, c: float):
    from math import sqrt
    discriminant = b**2 - 4*a*c
    x1 = (-b + sqrt(discriminant)) / (2*a)
    x2 = (-b - sqrt(discriminant)) / (2*a)
    return x1, x2
