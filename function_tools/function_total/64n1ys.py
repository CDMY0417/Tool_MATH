def subtract_fractions(numerator1: int, denominator1: int, numerator2: int, denominator2: int):
    common_denominator = denominator1 * denominator2
    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1
    final_numerator = new_numerator1 - new_numerator2
    return final_numerator, common_denominator
