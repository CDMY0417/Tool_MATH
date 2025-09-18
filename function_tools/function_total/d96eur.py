def sum_fractions(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    numerator1, denominator1 = frac1
    numerator2, denominator2 = frac2
    common_denominator = denominator1 * denominator2
    new_numerator = numerator1 * denominator2 + numerator2 * denominator1
    return (new_numerator, common_denominator)
