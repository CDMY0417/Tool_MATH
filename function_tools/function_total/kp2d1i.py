def evaluate_polynomial_at_point(roots: list[int], x: int) -> int:
    result = 1
    for root in roots:
        result *= (x - root)
    return result
