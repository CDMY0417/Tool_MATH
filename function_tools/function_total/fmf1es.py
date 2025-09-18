def integer_base_digits(n: int, base: int) -> int:
    import math
    return int(math.log(n, base)) + 1
