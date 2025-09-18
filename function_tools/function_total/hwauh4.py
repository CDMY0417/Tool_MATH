def multiply_complex(z1: tuple[float, float], z2: tuple[float, float]) -> tuple[float, float]:
    a, b = z1
    c, d = z2
    real_part = a * c - b * d
    imaginary_part = a * d + b * c
    return (real_part, imaginary_part)
