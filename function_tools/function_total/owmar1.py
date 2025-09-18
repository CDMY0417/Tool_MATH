def gcd_generalized_euclidean(a: int, b: int, c: int, d: int) -> int:
    while a != 0 and c != 0:
        if a > c:
            a = a - c
        else:
            c = c - a
    return max(a, c)
