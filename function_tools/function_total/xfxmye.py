def solve_quadratic(a: float, b: float, c: float):
    delta = b**2 - 4*a*c
    if delta >= 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return (root1, root2)
    return ()
