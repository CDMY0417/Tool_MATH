def simplify_fraction_difference(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    common_denominator = denominator1 * denominator2
    new_numerator = numerator1 * denominator2 - numerator2 * denominator1
    return new_numerator, common_denominator
