def is_n_more_than_multiple(n: int, addend: int, divisor: int) -> bool:
    return (n - addend) % divisor == 0
