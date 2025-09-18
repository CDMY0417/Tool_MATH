def complex_multiply(complex1: tuple[float, float], complex2: tuple[float, float]) -> tuple[float, float]:
    real_part = complex1[0] * complex2[0] - complex1[1] * complex2[1]
    imaginary_part = complex1[0] * complex2[1] + complex1[1] * complex2[0]
    return (real_part, imaginary_part)
