def product_of_sequence(n: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
