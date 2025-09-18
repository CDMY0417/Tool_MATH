def sum_of_fractions(numerators: tuple[float, ...], denominators: tuple[float, ...]) -> float:
    return sum(n/d for n, d in zip(numerators, denominators))
