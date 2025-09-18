def complex_product(c1: tuple[float, float], c2: tuple[float, float]) -> tuple[float, float]:
    real1, imag1 = c1
    real2, imag2 = c2
    real_part = real1 * real2 - imag1 * imag2
    imag_part = real1 * imag2 + imag1 * real2
    return real_part, imag_part
