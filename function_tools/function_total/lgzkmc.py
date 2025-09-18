def solve_quadratic_positive_root(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return max(root1, root2)
