def perfect_squares_below_n(n: int) -> list[int]:
    return [i * i for i in range(1, int(n**0.5) + 1)]
