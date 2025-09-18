def factorial_division(n: int, divisor: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product // divisor
