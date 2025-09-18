def quadratic_factors(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    sqrt_d = d**0.5
    if sqrt_d.is_integer():
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return ((a, x1), (a, x2))
    return None
