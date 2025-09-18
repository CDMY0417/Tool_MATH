def polynomial_from_roots(roots: list[float]) -> list[float]:
    n = len(roots)
    coeffs = [1] + [0] * n
    for r in roots:
        for i in range(len(coeffs) - 1, 0, -1):
            coeffs[i] -= r * coeffs[i - 1]
    coeffs[-1] *= (-1) ** n
    return coeffs
