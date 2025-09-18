def add_fractions(num1: int, den1: int, num2: int, den2: int):
    from math import gcd
    common_denominator = den1 * den2
    numerator1 = num1 * den2
    numerator2 = num2 * den1
    sum_numerator = numerator1 + numerator2
    common_factor = gcd(sum_numerator, common_denominator)
    return sum_numerator // common_factor, common_denominator // common_factor
