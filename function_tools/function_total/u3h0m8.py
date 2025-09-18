def factor_quadratic(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    if root1.is_integer() and root2.is_integer():
        root1, root2 = int(root1), int(root2)
        return [(1, -root1), (1, -root2)]
    return None
