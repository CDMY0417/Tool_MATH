def evaluate_piecewise_function(x: float, a: float, b: float) -> float:
    if x <= 3:
        return 9 - 2 * x
    else:
        return a * x + b
