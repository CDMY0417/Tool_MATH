def shift_polynomial(coefficients: list[int], shift: int) -> list[int]:
    shifted_coeffs = []
    for i, c in enumerate(coefficients):
        shifted_coeffs.extend([0] * (i - len(shifted_coeffs)))
        for j in range(i+1):
            shifted_coeffs[j] += c * (shift ** (i - j))
    return shifted_coeffs
