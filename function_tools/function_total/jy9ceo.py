def sum_of_powers(bases: list[int], exponent: int) -> int:
    return sum(base ** exponent for base in bases)
