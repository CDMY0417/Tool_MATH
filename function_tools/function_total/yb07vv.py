def add_scaled_equations(eq1_coeffs: tuple, eq2_coeffs: tuple, scale1: float, scale2: float):
    return (scale1 * eq1_coeffs[0] + scale2 * eq2_coeffs[0], scale1 * eq1_coeffs[1] + scale2 * eq2_coeffs[1])
