def factor_quadratic(a: int, b: int, c: int) -> tuple:
    from math import sqrt
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + int(sqrt(discriminant))) // (2*a)
        root2 = (-b - int(sqrt(discriminant))) // (2*a)
        return (root1, root2)
    return ()
