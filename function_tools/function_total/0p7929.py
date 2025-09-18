def multiples_of_n_less_than_m(n: int, m: int):
    return [i * n for i in range(1, m // n + 1)]
