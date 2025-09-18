def factor_quadratic_equation(b: int, c: int):
    for p in range(-abs(c), abs(c) + 1):
        q = b - p
        if p * q == c:
            return (p, q)
    return None
