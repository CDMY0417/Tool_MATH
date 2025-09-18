def calculate_slope(equation: str) -> float:
    _, mx_b = equation.split('=')
    mx, _ = mx_b.split('+')
    return float(mx.replace('x', '').strip())
