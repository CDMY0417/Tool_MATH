def function_inverse(a: float, b: float, c: float, d: float):
    def inverse(x: float) -> float:
        return (d * x - b) / (a - c * x)
    return inverse
