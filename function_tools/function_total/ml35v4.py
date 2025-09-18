def solve_linear_equation(a: int, b: int) -> float:
    if a == 0:
        return None if b != 0 else 'infinite solutions'
    return -b / a
