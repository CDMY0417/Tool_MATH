def count_combinations(n: int, k: int):
    from math import factorial
    return factorial(n) // (factorial(k) * factorial(n - k))
