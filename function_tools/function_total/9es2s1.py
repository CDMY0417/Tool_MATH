def evaluate_f(x: float) -> float:
    inv_x = 1 / x
    return inv_x + inv_x / (1 + inv_x)
