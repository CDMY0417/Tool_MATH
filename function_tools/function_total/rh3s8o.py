def rationalize_denominator(numerator: tuple, denominator: tuple) -> tuple:
    a, b = denominator
    n1, n2 = numerator
    denominator_new = (a**2 - b**2)
    num1 = n1 * a - n2 * b
    num2 = n2 * a - n1 * b
    return (num1, num2, denominator_new)
