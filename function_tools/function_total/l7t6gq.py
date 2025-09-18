def product_of_consecutive_integers(start: int, n: int):
    product = 1
    for i in range(n):
        product *= (start + i)
    return product
