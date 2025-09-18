def is_on_perpendicular_bisector(z_real: float, z_imag: float, p1_real: float, p1_imag: float, p2_real: float, p2_imag: float) -> bool:
    return (z_real == (p1_real + p2_real) / 2) and (abs(z_imag - (p1_imag + p2_imag) / 2) < 1e-9)
