from math import factorial
def binomial_coefficient(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))
