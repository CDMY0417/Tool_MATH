def evaluate_polynomial_at(a: float, b: float, roots: list[float], x: float) -> float:
    result = a * x + b
    for root in roots:
        result *= (x - root)
    return result
