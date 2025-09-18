def add_fractions(num1: int, den1: int, num2: int, den2: int):
    new_num = num1 * den2 + num2 * den1
    new_den = den1 * den2
    return new_num, new_den
