def find_polynomial_from_roots(roots: list[float]) -> list[float]:
    coefficients = [1]
    for root in roots:
        coefficients = [c - root * coefficients[i] if i > 0 else c for i, c in enumerate([0] + coefficients)]
    return coefficients
