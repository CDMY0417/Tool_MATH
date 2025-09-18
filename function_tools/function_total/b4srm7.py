def subtract_polynomials(coeffs1: list[float], coeffs2: list[float]) -> list[float]:
    max_len = max(len(coeffs1), len(coeffs2))
    coeffs1 = [0]*(max_len - len(coeffs1)) + coeffs1
    coeffs2 = [0]*(max_len - len(coeffs2)) + coeffs2
    return [c1 - c2 for c1, c2 in zip(coeffs1, coeffs2)]
