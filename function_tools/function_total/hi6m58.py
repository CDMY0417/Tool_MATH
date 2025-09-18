def solve_quadratic_equation(a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None  # No real roots
    sqrt_discriminant = discriminant ** 0.5
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2
