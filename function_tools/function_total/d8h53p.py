def product_difference_of_squares(x: float, n: int):
    numerator = 1 - x**(2**(n + 1))
    denominator = 1 - x
    return numerator / denominator
