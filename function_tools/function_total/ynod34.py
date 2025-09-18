def solve_linear_equation(a: int, b: int, c: int):
    if a == 0:
        return None if b != c else 'Infinite solutions'
    return (c - b) / a
