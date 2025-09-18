def rationalize_denominator(a: float, b: float):
    numerator = b - (a ** 0.5)
    denominator = (a ** 0.5 + b) * (b - (a ** 0.5))
    return numerator / denominator
