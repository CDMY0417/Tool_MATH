def radical_sum_integer_part(p: int, q: int, r: int) -> int:
    a = p + q * (r ** 0.5)
    b = p - q * (r ** 0.5)
    return int(a + b) - 1
