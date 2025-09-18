def polynomial_from_roots(roots: list[float], leading_coefficient: float) -> list[float]:
    result = [leading_coefficient]
    for root in roots:
        result = [leading_coefficient * (x if i == 0 else x - root) for i, x in enumerate(result)] + [0]
    return result
