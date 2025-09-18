def solve_quadratic_inequality(a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return (min(root1, root2), max(root1, root2))
