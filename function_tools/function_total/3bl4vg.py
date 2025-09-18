def quadratic_formula_complex(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant)**0.5) / (2*a)
    if discriminant < 0:
        return (real_part, imaginary_part)
    else:
        return (real_part + imaginary_part, real_part - imaginary_part)
