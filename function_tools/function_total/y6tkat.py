def greatest_common_factor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
