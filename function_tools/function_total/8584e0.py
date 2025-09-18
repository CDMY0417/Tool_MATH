def solve_quadratic_equation(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return [] # No real roots
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return [root1, root2] if root1 != root2 else [root1]
