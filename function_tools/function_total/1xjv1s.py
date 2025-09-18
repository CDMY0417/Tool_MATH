def solve_for_coefficient(x_val: float, y_val: float, roots: list[float]) -> float:
    result = 1
    for root in roots:
        result *= (x_val - root)
    return y_val / result
