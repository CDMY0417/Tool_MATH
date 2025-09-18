def solve_quadratic_equation(a: int, b: int, c: int) -> tuple:
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return ()  # No real roots
    sqrt_d = discriminant ** 0.5
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)
    return (root1, root2)
