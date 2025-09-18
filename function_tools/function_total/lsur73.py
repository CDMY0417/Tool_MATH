def divide_fractions(numerator: tuple[int, int], denominator: tuple[int, int]) -> tuple[int, int]:
    return (numerator[0] * denominator[1], numerator[1] * denominator[0])
