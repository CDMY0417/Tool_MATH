def factor_quadratic(a: int, b: int, c: int):
    discriminant = b ** 2 - 4 * a * c
    sqrt_val = int(discriminant ** 0.5)
    if discriminant >= 0 and sqrt_val ** 2 == discriminant:
        r1 = (-b + sqrt_val) // (2 * a)
        r2 = (-b - sqrt_val) // (2 * a)
        return (1, -r1, 1, -r2)
    return None
