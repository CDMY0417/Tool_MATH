def floor_value_of_root(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    sqrt_d = discriminant**0.5
    root1 = (-b + sqrt_d) / (2*a)
    root2 = (-b - sqrt_d) / (2*a)
    if root1.is_integer():
        return int(root1)
    if root2.is_integer():
        return int(root2)
    return None
