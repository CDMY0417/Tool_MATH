def gcd_euclidean(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
