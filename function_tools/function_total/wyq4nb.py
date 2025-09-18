def probability_same_heads(coefficients: list[int]) -> float:
    total_square = sum(coefficients)**2
    sum_squares = sum(x**2 for x in coefficients)
    return sum_squares / total_square
