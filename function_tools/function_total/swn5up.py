def solve_quadratic_inequality(a: float, b: float, c: float) -> tuple:
    from math import sqrt
    if a == 0:
        if b == 0:
            return (-float('inf'), float('inf')) if c >= 0 else ()
        return ((-c/b, float('inf')),) if b > 0 else ((float('inf'), -c/b),)
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return () if a > 0 else (-float('inf'), float('inf'))
    root1 = (-b - sqrt(discriminant)) / (2*a)
    root2 = (-b + sqrt(discriminant)) / (2*a)
    if a < 0:
        return (min(root1, root2), max(root1, root2))
    else:
        return ((-float('inf'), min(root1, root2)), (max(root1, root2), float('inf')))
