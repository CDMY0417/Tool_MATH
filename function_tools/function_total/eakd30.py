def solve_quadratic(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No real roots
    elif discriminant == 0:
        return [-b / (2*a)]  # One real root
    else:
        sqrt_discriminant = discriminant**0.5
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return [root1, root2]
