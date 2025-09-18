def compute_expression_with_squares(a: int, b: int, c: int, d: int) -> float:
    total_sum = a + b + c + d
    squares_sum = a**2 + b**2 + c**2 + d**2
    return (total_sum**2 - squares_sum) / 2
