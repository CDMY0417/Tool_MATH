def complex_addition(c1: tuple[float, float], c2: tuple[float, float]) -> tuple[float, float]:
    real_part = c1[0] + c2[0]
    imaginary_part = c1[1] + c2[1]
    return (real_part, imaginary_part)
