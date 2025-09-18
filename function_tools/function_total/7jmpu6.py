def evaluate_piecewise_function(x: float, a: float) -> float:
    if x >= a:
        return a * x**2
    else:
        return a * x + 2 * a
