def factorial_product(start: int, end: int) -> int:
    product = 1
    for i in range(start, end - 1, -1):
        product *= i
    return product
