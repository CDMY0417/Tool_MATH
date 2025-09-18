def is_relatively_prime(num1: int, num2: int) -> bool:
    from math import gcd
    return gcd(num1, num2) == 1
