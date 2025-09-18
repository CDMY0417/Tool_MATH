def sum_of_squares_of_roots(sum_of_roots: float, sum_of_product_of_roots: float) -> float:
    square_of_sum = sum_of_roots ** 2
    return square_of_sum - 2 * sum_of_product_of_roots
