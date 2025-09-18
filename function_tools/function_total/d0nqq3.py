def count_integer_pairs(integer_set: set) -> int:
    n = len(integer_set)
    return n * (n - 1) // 2
