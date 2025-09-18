def harmonic_sum(n_start: int, n_end: int):
    total = 0
    for i in range(n_start, n_end + 1):
        total += 1/i
    return total
