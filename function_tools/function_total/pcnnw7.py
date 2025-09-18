def count_integers_divisible_by_k(start: int, end: int, k: int):
    return (end // k) - (start // k) + 1
