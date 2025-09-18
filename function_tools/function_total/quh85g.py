def solve_linear_inequality(a: float, b: float) -> int:
    x = b / a
    return int(x) if x == int(x) else int(x) + 1
