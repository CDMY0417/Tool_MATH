def solve_quadratic(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2*a)]
    else:
        sqrt_disc = discriminant**0.5
        return [(-b + sqrt_disc) / (2*a), (-b - sqrt_disc) / (2*a)]
