def solve_linear_equation(a: int, b: int, c: int) -> float:
    if a == 0:
        return None if b != c else float('inf')  # No solution or infinite solutions
    return (c - b) / a
