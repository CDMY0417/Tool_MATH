def quadratic_factors(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    sqrt_d = int(discriminant**0.5)
    if sqrt_d * sqrt_d != discriminant:
        return None, None
    m = (-b + sqrt_d) // (2*a)
    n = (-b - sqrt_d) // (2*a)
    return m, n
