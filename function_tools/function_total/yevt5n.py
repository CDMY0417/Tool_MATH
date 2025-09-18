def quadratic_formula_positive_solution(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        return (-b + discriminant**0.5) / (2*a)
    else:
        return None
