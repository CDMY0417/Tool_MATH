def subtract_fractions(num1: float, den1: float, num2: float, den2: float):
    common_denominator = den1 * den2
    num1 *= den2
    num2 *= den1
    result_numerator = num1 - num2
    return result_numerator, common_denominator
