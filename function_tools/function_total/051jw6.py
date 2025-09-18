def calculate_combinations(n: int, k: int) -> int:
    from math import factorial
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))
