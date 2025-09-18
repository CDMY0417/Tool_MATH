def solve_linear_equation(a: int, b: int, c: int, d: int):
    if a == c:
        return None if b != d else 'Infinite solutions'
    return (d - b) / (a - c)
