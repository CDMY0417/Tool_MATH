def simplify_fraction_by_factor(numerator: int, denominator: int, factor: int):
    while numerator % factor == 0 and denominator % factor == 0:
        numerator //= factor
        denominator //= factor
    return (numerator, denominator)
