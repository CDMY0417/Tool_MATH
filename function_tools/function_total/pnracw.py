def factorial(n: int):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod
