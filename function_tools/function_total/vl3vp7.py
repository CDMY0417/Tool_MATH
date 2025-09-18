def count_valid_bases(n: int, remainder: int, min_base: int):
    from math import gcd, isqrt
    divisor_count = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            if i > min_base and gcd(i, remainder) == remainder:
                divisor_count += 1
            if i != n // i and n // i > min_base and gcd(n // i, remainder) == remainder:
                divisor_count += 1
    return divisor_count
