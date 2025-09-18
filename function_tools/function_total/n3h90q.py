def solve_quadratic_equation(a: int, b: int, c: int):
    if a == 0:
        if b == 0:
            return [] if c != 0 else [0]
        return [-c / b]
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        return []
