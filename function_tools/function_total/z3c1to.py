def quadratic_roots(a: float, b: float, c: float):
    from cmath import sqrt
    discriminant = sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return (root1, root2)
