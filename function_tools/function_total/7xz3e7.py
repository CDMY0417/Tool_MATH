def quadratic_roots(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)
    elif discriminant == 0:
        return (-b / (2*a),)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
