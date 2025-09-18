def evaluate_rational_function(a: float, b: float, c: float, d: float, x: float) -> bool:
    denominator = c + d * x
    if denominator == 0:
        return True
    return False
