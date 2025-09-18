def y_intercept_from_slope_intercept(equation: str) -> float:
    _, mx_b = equation.split('=')
    _, b = mx_b.split('+')
    return float(b.strip())
