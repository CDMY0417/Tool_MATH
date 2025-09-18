def next_multiple(n: int, m: int):
    return n if n % m == 0 else n + (m - n % m)
