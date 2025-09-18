def synthetic_division(coefficients: list[float], r: float):
    n = len(coefficients)
    new_coeffs = [coefficients[0]]
    for i in range(1, n):
        new_coeffs.append(coefficients[i] + new_coeffs[i-1] * r)
    return new_coeffs[:-1]
