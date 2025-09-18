def telescoping_product(n: int) -> float:
    product = 8/5
    for i in range(2, n):
        product *= (3 * i + 2) / (3 * i - 1)
    return product
