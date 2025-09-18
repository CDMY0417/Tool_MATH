def multiples_in_range(n: int, start: int, end: int) -> list:
    return [x for x in range(start, end + 1) if x % n == 0]
