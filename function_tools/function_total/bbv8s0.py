def product_of_fractions(start: int, end: int) -> float:
    product = 1.0
    for n in range(start, end + 1):
        product *= (n - 1) / n
    return product
