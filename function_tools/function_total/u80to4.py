def complex_division(num_real: float, num_imag: float, denom_real: float, denom_imag: float):
    denom_conjugate_real = denom_real
    denom_conjugate_imag = -denom_imag
    denom_magnitude_squared = denom_real**2 + denom_imag**2
    real_part = (num_real * denom_conjugate_real + num_imag * denom_conjugate_imag) / denom_magnitude_squared
    imag_part = (num_imag * denom_conjugate_real - num_real * denom_conjugate_imag) / denom_magnitude_squared
    return real_part, imag_part
