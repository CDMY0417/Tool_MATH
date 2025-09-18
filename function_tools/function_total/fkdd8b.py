def factorial_permutation(n: int, k: int):
    result = 1
    for i in range(k):
        result *= (n - i)
    return result
