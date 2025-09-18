def solve_quadratic_equation(a: float, b: float, c: float):
    import math
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        root_disc = math.sqrt(discriminant)
        return [(-b + root_disc) / (2 * a), (-b - root_disc) / (2 * a)]
