def calculate_f(a: int, b: int) -> float:
    if a + b <= 3:
        return (a * b - a + 2) / (2 * a)
    else:
        return (a * b - b - 2) / (-2 * b)
