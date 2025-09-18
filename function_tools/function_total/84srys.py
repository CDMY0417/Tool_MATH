def factorial_product(n: int, k: int) -> int:
    product = 1
    for i in range(n, n - k, -1):
        product *= i
    return product
