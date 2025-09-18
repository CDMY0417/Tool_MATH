def solve_quadratic(a: int, b: int, c: int):
    D = b**2 - 4*a*c
    if D < 0:
        return None
    root1 = (-b + D**0.5) / (2*a)
    root2 = (-b - D**0.5) / (2*a)
    return root1 if root1 > 0 else root2
