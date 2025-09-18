def multiply_by_conjugate(numerator: int, denominator: tuple):
    a, b = denominator
    conjugate_numerator = a - b
    new_numerator = numerator * conjugate_numerator
    new_denominator = a**2 - b**2
    return (new_numerator, new_denominator)
