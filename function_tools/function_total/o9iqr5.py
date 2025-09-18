def sum_of_powers(start: int, end: int):
    return sum(2**i for i in range(start, end + 1))
