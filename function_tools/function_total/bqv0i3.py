def complex_multiply(z1: tuple[float, float], z2: tuple[float, float]) -> tuple[float, float]:
    real1, imag1 = z1
    real2, imag2 = z2
    real_part = real1 * real2 - imag1 * imag2
    imag_part = real1 * imag2 + imag1 * real2
    return (real_part, imag_part)
