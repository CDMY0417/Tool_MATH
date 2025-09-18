def subtract_fractions(num1: int, den1: int, num2: int, den2: int) -> tuple:
    num = num1 * den2 - num2 * den1
    den = den1 * den2
    return num, den
